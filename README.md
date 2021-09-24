# tie-set Interview Test

Coding assignment for the interview with tie-set.com

Problem statement and notes are put at https://github.com/jaykhandare/tie-set-test/tree/main/problem_statement_docs



**Steps to run the project**

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


