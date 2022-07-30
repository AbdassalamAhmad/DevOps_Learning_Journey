# Linux Resources

- I've used <a href="https://www.youtube.com/playlist?list=PLlnHaYmkH6w9FfheDdNnq0ldy6aNKp_3y">**Terminal Tutorial**</a> from a YouTube course
to learn Linux basic commands.

- Then I've used <a href="https://github.com/kodekloudhub/linux-basics-course">**Linux-Basics-Course**</a> from KodeKloud GitHub Repo


## Commands I've Learnt:
## 1. **Navigation:**
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
$ cd ~ # cd back to user's home directory.
$ cd / # cd back to root (parent of all parents :) ).
```


## 2. **Search for Help in Commands:**
``` shell
$ [command] --help
$ man [command] # **preferable**
$ info [command]
```


## 3. **File System Commands:**
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

* **mv**: Move || Rename Files & Directories
```shell
$ mv file1.txt file2.txt # rename file1 to file2
$ mv file1.txt file2.txt ./dir1 # move two files to dir1
```

* **rm**: Remove Files && Directories
```shell
$ rm file1.txt file2.txt # remove file1 And file2
$ rm -rf ./dir1 # remove the whole directory and its children recursively and by force.
```

* **hardlink**: It linkes the same file in two different positions and make them not dependeant on each other.
```shell
$ ln [source] [destination] # link destination file (new) in desktop -for example- to source file in a deep path.
$ #IMPORTANT NOTE: write the absolute link to the file not relative link
```

* **softlink**: like a shortcut in windows.

```shell
$ ln -s [source] [destination] # link destination file (new) in desktop -for example- to source file in a deep path.
$ #IMPORTANT NOTE: write the absolute link to the file not relative link
```

## 4. **File System Permissions:**

**rwx**: read write execute<br>
|  rwx   | rwx          | rwx      | 
| -------| :----------: | :------: |
| USER   | GROUP        | OTHERS   |

* **chmod**: Change File || Directory Mode (Permissions)
```shell
$ chmod 740 file1.txt
$ # The permissions will be rwx r-- ---
$ # It's like the binary
```
**OR**

```shell
$ chmod u+r file1.txt # add read permission to user
$ chmod g-w file1.txt # remove write permission from group
$ chmod go=wx file1.txt # set write and execute permission to group and others (no read, only write and execute)
```

## **Linux Process Management**

1. **&**: you can use this sign & to run any process in the **background**.

2. **top**: list all runing process.

```shell
$ top 
```
3. **ps**: list running prcess in foreground 

```shell
$ ps -u <user> # display process for this specific user.
```