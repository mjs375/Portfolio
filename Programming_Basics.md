# P R O G R A M M I N G _ B A S I C S 

[CSS](#css) | [HTML](#html) | [License](#license) | [Readme](#readme) | [Requirements](#requirements)



### LICENSE
- Informs the user that permissions they have– can they download, modify and re-publish, &c.


### README
- ```README.md```: Answers a user's questions about installations & usage of a project, located in the root (top-leve) directory. Written in a ```.md``` or ```.markdown``` file (supports lightweight markdown).
  - Include: *project name, description (function of program, context, links for reference), visuals (screenshots/GIFs/video), installation procedure (nod to requirements.txt), usage (e.g. ```python3 manage.py runserver```), support (where to go for help), authors/acknowledgement, project status/roadmap.*
  

### Requirements
- ```Requirements.txt```: *a file that makes it easier for other users (that have downloaded your projects) to run the same Python libraries as it was written in/for. A user will encounter messages such as "No module named [...]"; download that library; then get the message again, again, again...*
  - ```$ pip install -r requirements.txt```: *command to download all the necessary libraries in a ```requirements.txt```*


### Virtual Environments
- *```venv``` module lets you create virtual environments. It is good practice to have a venv for each project, instead of installing every package you need globally, in case conflicts later arise.*
  - **Create venv:** ```$ python3 -m venv env``` (Anaconda: ```$ conda create -n venv_name python=3.8)```
  - **Activate venv:** ```$ source env/bin/activate``` (Anaconda: ```$ conda activate [venv]```
  - **Confirm you're in:** ```$ which python``` => ```.../env/bin/python``` (Anaconda: ```$ conda env list``` lists all available venv, the active one denoted by a "*").
  - **Leave VENV:** ```$ deactivate```
- **Working with VENV**:
  - **Install packages:** ```$ pip install <module>```
    - **Install specific version:** ```$ pip install MODULE==2.18.4
    - **Install latest 2.x release:** ```$ pip install MODULE>=2.0.0,<3.0.0
  - **Upgrade packages:** ```$ pip install --upgrade MODULE```
- **Create Requirements.txt:** ```$ pip freeze > requirements.txt``` *PIP generates a list of all installed packages and their versions*
- **Install all packages in a requirements.txt**: ```$ pip install -r requirements.txt```

