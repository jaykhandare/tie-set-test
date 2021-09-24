#!/bin/sh
#!/bin/bash

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