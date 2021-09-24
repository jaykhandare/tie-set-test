# tie-set Interview Test

Coding assignment for the interview with tie-set.com

**Steps to run the project are provided at the end of this page.**

Problem statement and notes are put at https://github.com/jaykhandare/tie-set-test/tree/main/problem_statement_docs

The problem statement seems to be a little ambiguous regarding the use of the machine learning algorithm.
This being my 3rd attempt at implementing a ML algorithm, it took me some time to figure out what exactly is being asked to be done in this assignment. Hence, it wasted some of the allotted time which could have been better utilized for a thorough documentation and code optimization.

Once I figured out what I needed to do, I broke down the task into the following subtasks.
1. ML algorithm implementation
2. Django UI creation
3. Integration of the above two tasks

For ML algorithm implementation: 
A sample code was provided; but the code was a simple outline which needed a lot of modifications from my side to achieve the required structural functionality of the problem statement. I had to separate "train" and "test" modules and I had to make the code portable in order for it to work on my machine which doesn't have GPU support for the Linux(WSL2) environment. Hence, I searched for packages which will run the code on the CPU. I have mentioned this in the README, for easier installation.

For Django UI creation: 
I am well versed in the Django framework. Therefore, I was pretty sure it shouldn't take me more time to achieve this task. That's why I decided to leave this task for the last day. But in order to get onto the next part, I had to create a basic skeleton website as this was kind of a prerequisite for the integration.

For Integration:
With the ML algorithm having been implemented, I started to get on collecting and formatting data to be shown on the django-ui. The main data-points to consider were "training time", "testing time", and "change in loss values". I modified the ML code, to access these points and store them in a sql database and csv files. These files and values from the database were later retrieved in the django libraries to be formatted and displayed using the "plotly" library.

Actually, I took more time for these tasks than I anticipated. Hence, I was not able to start on the unit-tests. I have included mini-tests in the ML algorithm module to verify that the data is being generated.



# Steps to run the project

1. virtualenv setup
```
    python3 -m pip install --user --upgrade pip
    python3 -m pip install --user virtualenv
    python3 -m venv env

    source env/bin/activate

```

2. install required python packages
```
    pip install -r requirements.txt

    %note: pytorch libraries torch and torchvision may require additional steps%

    following can be used to install pytorch libs which use cpu only
    
    pip3 install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

```

3. run the code[example provided below]
```
    python3 mlrunner.py train --project_name demo1 --learning_rate 0.01 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module

    python3 mlrunner.py test --project_name demo1 --dataset data/MNIST/processed/testing.pt --script ml_algo_module
    
    python3 mlrunner.py report --project_name demo2
    
    python3 django_ui/manage.py runserver
```

4. open following link in your web-browser of choice.

    http://127.0.0.1:8000/all_projects/


OR 

You can simply run the sample_run.sh file with  following command in your bash shell and open the above link in your browser.

```
./sample_run.sh
```


