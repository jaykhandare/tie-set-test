#!/bin/sh
#!/bin/bash

python3 -m pip install --user --upgrade pip 

python3 -m pip install --user virtualenv 
python3 -m venv env

pip3 install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt

source env/bin/activate

python3 mlrunner.py train --project_name demo2 --learning_rate 0.02 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo2 --dataset data/MNIST/processed/testing.pt --script ml_algo_module

python3 mlrunner.py train --project_name demo1 --learning_rate 0.01 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo1 --dataset data/MNIST/processed/testing.pt --script ml_algo_module

python3 mlrunner.py train --project_name demo2 --learning_rate 0.01 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo2 --dataset data/MNIST/processed/testing.pt --script ml_algo_module

python3 mlrunner.py train --project_name demo1 --learning_rate 0.1 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo1 --dataset data/MNIST/processed/testing.pt --script ml_algo_module

python3 mlrunner.py train --project_name demo2 --learning_rate 0.08 --dataset ../data/MNIST/processed/training.pt --script ml_algo_module
python3 mlrunner.py test --project_name demo2 --dataset data/MNIST/processed/testing.pt --script ml_algo_module


python3 mlrunner.py report --project_name demo2
python3 mlrunner.py report --project_name demo1

python3 django_ui/manage.py runserver
