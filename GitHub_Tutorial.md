# G I T H U B _ T U T O R I A L

### Working in a Repository
- **Create a Repository:** *go to [Github](https://github.com/) to make a free account and create a repository.*
- **Download a repository**: ```$ git clone <url>```
  - *once you*
- **Mark changes to be included in update (1):** ```$ git add <filename>``` OR ```$ git add .``` 
  - *mark files with changes to be included in the next update, i.e. 'prep in a staging area'. The ```.``` means 'include all files in directory'.*
- **Save current state for update(2):** ```git commit -m "some message..."
  - *the final prep before updating the remote repository with your added/committed changes*
    - ```$ git -am commit "some message"```: *combines add/commit in one command*
- **Send version to Github(3):** ```$ git push```
  - *the 'Save' button of git, this sends your noted changes to the remote repository.*
- **Pull down more updated version from remote repository:** ```$ git pull```
  - ```git pull``` *requests changes from remote to local repository;* ```$ git push``` *does the opposite.*





### Github Actions / Workflow:
- Set up a new workflow for your project:
  - Github.com > Create New Workflow
  - ```project/path/ .github/workflow/ ___.yml```
- 


- Demo.yml Workflow:
```
```
