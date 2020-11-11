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
  - ```$ git clone <repository_url>```: *if you already have a populated repository on Github.com and simply want it locally on a computer too.*
  
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



### Branching
- *Programmers shouldn't develop new features in a linear fashion– rather, everytime they add (develop & test) a new feature they should __branch__ their repository. That one, a working, stable copy, pre-new-feature is still available, while the new feature can be worked on independently until such time as it is ready and fully de-bugged, and then be merged back into the __main__ branch.*
  - **HEAD**: *this points to the branch that you are currently 'in'– by default, HEAD points to the main branch.*
  - **Main Branch**: *usually the default, 'master' branch which has the stable, central code.*
  - **[Feature] Branch**: *an off-shoot branch of the code, wherein programmers can develop & test new features while leaving a stable, working version of the program in the Main branch. After 'Feature' is debugged, it is merged back into the Main branch (and deleted).*
  
- **Check Branches**: ```$ git branch``` => ```* main```: _lists all the branches of your repository, with the HEAD denoted by an "*"._
- **Create New Branch**: ```$ git checkout -b <new_branch_name>```: *you will automatically be switched to the new branch as you create it. The new branch will be an exact duplicate of the one you just left... until you make changes and commit them.*
  - **Pushing a New Branch**: ```$ git push --set-upstream <remote> <branch>```: e.g. ```$ git push --set-upstream origin feature_branch```.**
- **Switch Branches**: ```$ git checkout <branch_name>```: *switch between branches and make commits to each version as usual using ```add``` & ```commit```.*
- **Merging Branches**: ```$ git merge <other_branch_name>```: *when you want to re-merge two branches, check out (switch to) the branch you want to keep (main). Solve any __merge conflicts__ that arise, then ```add``` & ```commit``` the changes to ```main```.*
  - **Delete Branch**: ```$ git branch -d <branch_name>```: *after a merge, if you are sure you don't need the merged-from branch anymore, you can permanently delete it.*
  - **Rename Branch**: ```$ git checkout <old_name>``` + ```$ git branch -m <new_name>```: *just in case, you can always keep around old branches, even if you've merged them to the ```main```. (Note: if the branch is also in the remote repository, complete the following: ```$ git push origin -u <new_name>``` + ```$ git push origin --delete <old_name>```.)*
  
### Merging
- **Merge Conflict:** *when merging a local copy and the repository code, if one thing has been changed to two different things, that presents a merge conflict– Github cannot decide which to keep, so you must choose (or re-combine) them until no conflicts exist, then re-commit the version you want.*
  - *Note: Git can usually merge different versions of the code without you the user needing to manually fix conflicts (such as pushing a local version to the remote, wherein you added a wholly new line of code). However, when the same line of code is different in the local & remote versions, Git cannot fix it without your input.*
```python
a = 1
<<<<< HEAD
b = 2
=====
b = 3
>>>>> 56782736387980937883 #(a hash representing the commit that is conflicting with your edits)
c = 3
```
- **Log History:** ```$ git log``` *to see a history of all commits on a repository (commit hash number, author, date).*
- **Reset**: ```$ git reset --hard <commit>``` *to return to all of your code as it was after a particular commit (the commit hash number found using* ```$ git log```*).*
  - ```$ git reset --hard origin/main```: *reverts your code to the version currently stored online at Github.*









### .gitignore
- ```$ touch .gitignore```: *create a plain-text file, generally located in the root folder of the repository, that specifies files and/or folders to be ignored by git, i.e. when you push to the remote repository, those files/folders will NOT be (e.g. files that contain personal information like passwords, &c.). Each line is a pattern for a file or folder to ignore (patterns relative to that of the .gitignore file).*
  - ```filename.ext``` => *a literal filename to ignore*
  - ```directory/``` => *entire directories to ignore*
    - ```*``` => *wildcard * matches any 0+ characters (except '/'), e.g. ```*.log``` ignores any file with the '.log' extension.*
    - ```?``` => *matches any 1 character (except '/'), e.g. ```.page?``` ignores any files named page_.*
    - ```!``` => *prefix unignores a file specified to be ignored by a general rule, e.g. ```*.log```, ```!example.log``` (exceptions to general patterns, BUT you can't unignore something inside an ignored directory).*
    - ```**``` => *can be used to match any number of directories*
    - ```#``` => any line that starts with ```#``` are comments
  - ```$ git rm --cached <filename>```: *removes the cached version of the file (in remote Github), does not delete local copy. This command must be entered if a file is already tracked but you want it to now be ignored.*

### Github Actions / Workflow (.yml)
- Everytime you ```$ git push``` your work to Github, certain processes can be automated by writing a ```.yml``` file. Set up a new workflow for your project:
  - Github.com > Create New Workflow | Github.com > Repository > Actions
  - ```project/path/ .github/workflow/ ___.yml```: *Create a ```.github/workflows/``` directory in your project.*
- ```.yml```/```.yaml```: *Create a file to house the workflow details.*
```yml
name: Testing   #Name the workflow
on: push  #when should the workflow run?– when pushed to repository

jobs:   #jobs to run at every push
  test_project:   #just 1 job (all jobs contain 2 components:)
    runs-on: ubuntu-latest  #which Github VM to run our code on
    steps:  #actions to take when run
    - uses: actions/checkout@v2
    - name: Run Django unit tests   #description of actions
    run: |    #commands to run on Github's server
      pip3 install --user django    #install Django
      python3 manage.py test    #run the Test.py file
```


