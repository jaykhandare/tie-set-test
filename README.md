# tie-set
Coding assignment for the interview with Tie-set.com


steps to run the project

1. setup virtualenv

    python3 -m pip install --user --upgrade pip
    python3 -m pip install --user virtualenv
    python3 -m venv env

    source env/bin/activate

2. install required python packages

    pip install -r requirements.txt

    %note: pytorch libraries torch and torchvision may require additional steps%

    following can be used to install pytorch libs which use cpu only
    
    pip3 install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

3. run the code.

    this runs the modified version of the script provided in the problem statement
    it will also download and process datasets, but that may take some time, hence I have included the dataset in './data/MNIST' directory in the git repo itself.

    python3 ml_script.py

