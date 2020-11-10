# G I T H U B _ T U T O R I A L

### Setting Up a Repository:
- **Create a Repository:** 
  - ```$ cd user/your-project```: *navigate to the top level of your new or existing file-tree with your project*
  - ```$ git init```: *create a new git repository (either initialize a new, empty repo, or convert an existing, unversioned project to a Git repo).*
  - ```$ git add *```: *adds ALL files to the 'staging area' for next repository update*
    - ```$ git add *.<extension>```: *adds ALL files of a certain type (e.g. ```$ git add *.py```)*
  - ```$ git commit -m "Initial project version"```: *prep for git push*
  - ```$ git branch -M main```: **
  - ```$ git remote add <name> <url>```: **
  - ```$ git push -u <name> main```: **
- **Download an Existing Repository:**
  - ```$ git clone <url>```: *if you already have a populated repository on Github.com and simply want it locally on a computer too.*
  
### Updating a Repository:
- ```$ git status```: *reports all changes not yet added/committed to the remote repository*
- **(1) Track changes to be included in update:** ```$ git add <filename>``` OR ```$ git add .``` 
  - *mark modified or new files to be included in the next update, i.e. 'prep in a staging area'. The ```.``` means 'include all files in directory'.*
- **(2) Save current state for update:** ```git commit -m "some message..."
  - *the final prep before updating the remote repository with your added/committed changes*
    - ```$ git -am commit "some message"```: *combines add/commit in one command (only if you modified files, not added new ones)*
- **(3) Send version to Github:** ```$ git push```
  - *the 'Save' button of git, this sends your noted changes to the remote repository.*
- **Pull down more updated version from remote repository:** ```$ git pull```
  - ```git pull``` *requests changes from remote to local repository;* ```$ git push``` *does the opposite. If both sides have changes, they will need to be reconciled first.*

### Branches & Merging



### Misc.
- ```.gitignore```: *a plain-text file, generally located in the root folder of the repository, that specifies files and/or folders to be ignored by git, i.e. when you push to the remote repository, those files/folders will NOT be (e.g. files that contain personal information like passwords, &c.). Each line is a pattern for a file or folder to ignore (patterns relative to that of the .gitignore file).*
  - ```.filename``` => *a literal filename to ignore*
  - ```directory/``` => *entire directories to ignore*
    - ```*``` => *wildcard * matches any 0+ characters (except '/'), e.g. ```*.log``` ignores any file with the '.log' extension.*
    - ```?``` => *matches any 1 character (except '/'), e.g. ```.page?``` ignores any files named page_.*
    - ```!``` => *prefix unignores a file, e.g. ```*.log```, ```!example.log``` (exceptions to general patterns, BUT you can't unignore something inside an ignored directory).*
    - ```**``` => *can be used to match any number of directories*
    - ```#``` => any line that starts with ```#``` are comments

### Github Actions / Workflow:
- Set up a new workflow for your project:
  - Github.com > Create New Workflow
  - ```project/path/ .github/workflow/ ___.yml```
- 


- Demo.yml Workflow:
```
```
