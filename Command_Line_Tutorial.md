# T E R M I N A L _ C O M M A N D S 

### Common Terminal Commands
- ```$ ls```: *__List__ all files in the current directory (prints to terminal)*
- ```$ pwd```: *__Print working directory__ prints to the terminal the current working directory, e.g.* ```user/path/folder/```.
- ```$ cd <folder>```: *__Changes directory__*
  - ```$ cd ..```: *goes 'back up' to parent directory (folder) from current. ```$ cd ../..``` would jump up 2 levels.*
  - ```$ cd ~```: *goes to home directory, e.g. ```/Users/you```*
- ```$ touch <filename>```: *create a new file, e.g. ```$ touch README.md```.*
  - ```$ open <filename>```: *__opens__ designated file in directory*
  - ```$ rm -i <file>```: *delete a file (confirmation prompt)*
- ```$ mkdir <foldername>```: *makes a __directory__*
  - ```$ rmdir <path>```: *remove an empty directory*
- ```$ cp <source> <destination>```: *copy a file to another directory, e.g. ```$ cp ~/Desktop/project/index.html ~/Documents```.*
  - ```$ cp -R ~/Desktop/project ~/Documents```: *the "-R" means recursion, and it copies a folder, and all its files and sub-folders.*
- ```$ mv <source/file.ext> <destination/>```: *__move__ a file from 'source/' to 'destination/'. The previous copy is destroyed.*
  - ```$ mv a.txt b.txt```: *__rename__ a file, moving it... to the exact same spot.*
  - ```$ clear```: *__clear__ the command-line of all previous commands*
  - ```$ man <command>```: *prints a __manual__ about the specified <command>.*
    - ```$ whatis <command>``` *prints a one-line description for <command>*
    - ```$ help [-s] <command>```: *displays a [short], helpful synopsis about <command>*
