#!/bin/sh
#!/bin/bash

# setting up virtualenv and installing required python packages
python3 -m pip install --user --upgrade pip 
python3 -m pip install --user virtualenv 
python3 -m venv env
pip3 install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt

# activating virualenv
source env/bin/activate

# train and test project demo2 with lr 0.02
python3 mlrunner.py train --project_name demo2 --learning_rate 0.02 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo2 --dataset data/MNIST/processed/testing.pt --script ml_algo_module

# train and test project demo1 with lr 0.01
python3 mlrunner.py train --project_name demo1 --learning_rate 0.01 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo1 --dataset data/MNIST/processed/testing.pt --script ml_algo_module

# train and test project demo2 with lr 0.01
python3 mlrunner.py train --project_name demo2 --learning_rate 0.01 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo2 --dataset data/MNIST/processed/testing.pt --script ml_algo_module

# train and test project demo1 with lr 0.1
python3 mlrunner.py train --project_name demo1 --learning_rate 0.1 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo1 --dataset data/MNIST/processed/testing.pt --script ml_algo_module

# train and test project demo2 with lr 0.08
python3 mlrunner.py train --project_name demo2 --learning_rate 0.08 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo2 --dataset data/MNIST/processed/testing.pt --script ml_algo_module


# creating reports for demo2 and demo1
python3 mlrunner.py report --project_name demo2
python3 mlrunner.py report --project_name demo1

# running the django server
python3 django_ui/manage.py makemigrations
python3 django_ui/manage.py migrate
python3 django_ui/manage.py runserver