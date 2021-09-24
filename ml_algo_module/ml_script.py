import csv
from os.path import exists
from time import time

import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable

from utils import SQL_queries


# class used to perform logistic regression analysis using torch library
class LogisticRegression(torch.nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LogisticRegression, self).__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim)

    def forward(self, x):
        outputs = self.linear(x)
        return outputs


# this class is implemented to facilitate "train" and "test" part of the ML algorithm
class ExecuteAlgorithm():

    # trained models are saved at this path after training is finished
    # they are later retrieved while testing
    # this is done for implementing a modular code structure where train and test are independently run
    model_save_path = './trained_models/'

    def __init__(self, project_name, batch_size=100):
        self.project_name = project_name
        self.batch_size = batch_size
        self.input_dim = 784
        self.output_dim = 10

        # object initiated to perform various SQL queries
        self.db_object = SQL_queries()

    # this method implements the 'train' part of the machine learning algorithm
    # it also includes additional code for calculating time neeeded to perform the training, saving loss values, and calls to db to store run information
    def train_algorithm(self, learning_rate, dataset="../data", epochs=100):
        print("training started for project {}".format(self.project_name))

        train_dataset = dsets.MNIST(
            root=dataset, train=True, transform=transforms.ToTensor(), download=True)
        train_loader = torch.utils.data.DataLoader(
            dataset=train_dataset, batch_size=self.batch_size, shuffle=True)

        model = LogisticRegression(self.input_dim, self.output_dim)
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.SGD(
            model.parameters(), lr=float(learning_rate))

        loss_items = []

        # call to store the time before training activation
        time_pre_train = time()
        # training algorithm
        for epoch in range(int(epochs)):
            print("running epoch {}".format(epoch+1))
            for _, (images, labels) in enumerate(train_loader):
                images = Variable(images.view(-1, 28 * 28))
                labels = Variable(labels)
                optimizer.zero_grad()
                outputs = model(images)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()
            loss_items.append(loss.item())
        # training ends here

        time_post_train = time()
        time_taken_to_train = time_post_train - time_pre_train

        # generating the run_id as an unique identifier
        run_id = self.project_name + "_" + str(int(time_pre_train))

        # saving loss item data in a csv file for plotting a scatter graph
        filename = "./loss_files/" + run_id + ".csv"
        loss_result_file = open(filename, "w")
        writer = csv.writer(loss_result_file)
        writer.writerow(loss_items)

        # saving trained model to be used later in testing
        filename = ExecuteAlgorithm.model_save_path + run_id + ".pth"
        torch.save(model.state_dict(), filename)

        self.db_object.add_entry(self.project_name, run_id,
                                 time_pre_train, time_taken_to_train)

        print("training finished")

    # this method implements the 'test' part of the machine learning algorithm
    # it also includes additional code for calculating time neeeded to perform the testing, and calls to db to store run information

    def test_algorithm(self, dataset="../data", epochs=100):
        # retrieving run_id for testing an incomplete entry in the database
        run_id = self.db_object.retrieve_incomplete_entry_run_id(
            project_name=self.project_name)
        print("testing instance with run_id: {}".format(run_id))

        test_dataset = dsets.MNIST(
            root=dataset, train=False, transform=transforms.ToTensor())
        test_loader = torch.utils.data.DataLoader(
            dataset=test_dataset, batch_size=self.batch_size, shuffle=False)

        model_path = ExecuteAlgorithm.model_save_path + run_id + ".pth"
        if not exists(model_path):
            print("model not trained for this project")
            return

        # loading the trained model to be test the data
        model = LogisticRegression(self.input_dim, self.output_dim)
        model.load_state_dict(torch.load(model_path))
        model.eval()

        correct, total = 0, 0

        time_pre_test = time()
        # testing
        for images, labels in test_loader:
            images = Variable(images.view(-1, 28*28))
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum()
        # testing ends here
        time_post_test = time()
        time_taken_to_test = time_post_test - time_pre_test
        accuracy = 100 * correct/total

        # call to database to update entry
        self.db_object.update_entry(run_id=run_id, update_params=(
            time_pre_test, time_taken_to_test, int(accuracy)))


""" code for testing these classes separately """
# from datetime import datetime
# executioner = ExecuteAlgorithm("demo")
# for i in range(2):
#     print("training run : {}".format(i+1),
#           " time now: ", datetime.now().time())
#     executioner.train_algorithm(learning_rate=0.01)
#     print("testing run : {}".format(i+1), " time now: ", datetime.now().time())
#     executioner.test_algorithm()

# executioner = ExecuteAlgorithm("demo2")
# for i in range(2):
#     print("training run : {}".format(i+1),
#           " time now: ", datetime.now().time())
#     executioner.train_algorithm(learning_rate=0.01)
#     print("testing run : {}".format(i+1), " time now: ", datetime.now().time())
#     executioner.test_algorithm()
