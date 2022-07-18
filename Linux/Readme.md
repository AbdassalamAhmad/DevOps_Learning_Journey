
# Linux Resources

- I've used <a href="https://www.youtube.com/playlist?list=PLlnHaYmkH6w9FfheDdNnq0ldy6aNKp_3y">**Terminal Tutorial**</a> from a YouTube course
to learn Linux basic commands.

- Then I've used <a href="https://github.com/kodekloudhub/linux-basics-course">**Linux-Basics-Course** </a>from KodeKloud GitHub Repo
<br>

### Commands I've learnt:
1. **Navigation:**
* **pwd**: Print Working Directory.
``` shell
$ pwd
```
* ls: List Files
``` shell
$ ls -l -a # List all files (and hidden) in a long format
$ ls -a ../ # list all files in the parent directory.
$ ls *.txt # lists every file ends with .txt
$ ls file* # lists all files that start with the word file.
$ ls -lt # lists all the files in the order they were modified.
```
* **cd**: Change Directory
``` shell
$ cd - # equals backspace in windows.
$ cd ..  #back one directory.
$ cd ../.. # back 2 directories.
$ cd ~ # cd back to user.
$ cd / # cd back to root (parent of all parents :) ).
```
2. **Search for help in commands:**
``` shell
$ [command] --help
$ man [command] # **preferable**
$ info [command]
```
3. **File System Commands:**
* **mkdir**: Make Directory
``` shell
$ mkdir dir{5..7} # create 3 folders (dir 5,6,7)
$ mkdir -p dir1/sub_dir1 # create a folder inside a folder (-p stands for parent directory)
```
* **touch**: Make a New File

``` shell
$ touch code.py # create a python file named code.py
$ touch code{1..5} # create 5 fiels from 1 to 5.
```
* **cp**: Copy Files & Directories
``` shell
$ cp file1.txt file2.txt # copy file1 and rename it to file2 in the same directory.
$ cp file{1..2}.txt ./dir1 # copy the two files from this directory to (./dir1)
$ cp file1.txt file2.txt ./dir1 # copy the two files from this directory to (./dir1)
$ cp *.txt ./dir1 # copy all txt files to ./dir1
$ cp -r dir1 dir2 # copy the whole directory dir1 into dir2
```
* **mv**: Move Files || Rename Files & Directories
```shell
$ mv file1.txt file2.txt # rename file1 to file2

