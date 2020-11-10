# P R O G R A M M I N G _ B A S I C S 


### Requirements.txt
- *a file that makes it easier for other users (that have downloaded your projects) to run the same Python libraries as it was written in/for. A user will encounter messages such as "No module named [...]"; download that library; then get the message again, again, again...*
  - ```$ pip install -r requirements.txt```: *command to download all the necessary libraries in a ```requirements.txt```*
- **How to Generate a Requirements.txt**:
  - ```$ pip freeze > requirements.txt```: *PIP generates the file for you– but with every library you've ever downloaded on your own computer system. (View in terminal with ```cat requirements.txt```.)*
  - 1. Install Anaconda to make a 'clean-slate' Virtual Environment: ```$ conda create -n shiny_new_env python=3.8```
    - ```$ conda env list```: _see a list of all available venv (the activated one will be denoted by a '*')_
    - ```$ conda activate [venv_name]```: _switch to that venv (note that [venv_name] appears in terminal command-line name, left of the ```$```.)_
  - 2. Now, install each package the project requires in this as-of-yet empty venv (yes, install each one again... but just you, this once, have to do it). Then, run ```$ pip freeze > requirements.txt``` once again and view the list of installs needed just for this project.

### README.md
- Answers a user's questions about installations & usage of a project, located in the root (top-leve) directory. Written in a ```.md``` or ```.markdown``` file (supports lightweight markdown).
  - Include: *project name, description (function of program, context, links for reference), visuals (screenshots/GIFs/video), installation procedure (nod to requirements.txt), usage (e.g. ```python3 manage.py runserver```), support (where to go for help), authors/acknowledgement, project status/roadmap.*


### LICENSE
