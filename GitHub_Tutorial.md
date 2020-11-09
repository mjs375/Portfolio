# G I T H U B _ T U T O R I A L

### Working in a Repository
- **Download a repository**: ```$ git clone```
- **Mark changes to be included in update** ```$ git add <filename>``` OR ```$ git add .``` 
  - *mark files with changes to be included in the next update, i.e. 'prep in a staging area'. The ```.``` means 'include all files in directory'.*
- **Save current state for update**: ```git commit -m "some message..."
  - *the final prep before updating the remote repository with your added/committed changes*
    - ```$ git -am commit "some message"```: *combines add/commit in one command*
- **Send version to Github:** ```$ git push```
  - *the 'Save' button of git, this sends your noted changes to the remote repository.*
- **Pull down more updated version from remote repository:** ```$ git pull```
  - ```git push``` *sends changes from local to remote repository;* ```$ git pull``` *does the opposite.*





### Github Actions / Workflow:
- Set up a new workflow for your project:
  - Github.com > Create New Workflow
  - ```project/path/ .github/workflow/ ___.yml```
- 


- Demo.yml Workflow:
```
```
