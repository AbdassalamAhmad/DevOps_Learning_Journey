# Commands I've Learnt:
##  **1. Navigation:**
* **pwd**: Print Working Directory.
``` shell
$ pwd
```

* ls: List Files
``` shell
$ ls -l -a # List all files (and hidden) in a long format
$ ls -a ../ # list all files in the parent directory.
$ ls -R # list all files and Dirs and thier sub-directories RECURSIVELY.
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


## **2. Search for Help in Commands:**
``` shell
$ [command] --help
$ man [command] # **preferable**
$ info [command]
```


## **3. File System Commands:**
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

* **cat**: view contents of a file
```shell
$ cat file1.txt # view its contetns
$ cat > file2.txt # write contents in file2 then press (ctrl + D) to exit 
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

## **4. File System Permissions:**

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

## **5. Linux Process Management**

1. **&**: you can use this sign & to run any process in the **background**.

2. **top**: list all runing process.
```shell
$ top 
```
Note: You can press F to see all options in the command and its meaning.
![image](https://user-images.githubusercontent.com/83673888/181936458-d7905a79-e55f-4adc-92c9-6685c1b62a20.png)

3. **ps**: list running prcess in foreground 
```shell
$ ps -u <user> # display process for this specific user.
```

4. **pgrep**: list the PID of the specific program
```shell
$ pgrep top # display its PID
```

5. **fg**: Get Stopped or Background process to foreground

6. **bg**: Resume Stopped process in the background

7. **kill**: send a signal to a process using its PID.
```shell
$ kill -l # List all system signals
$ man 7 signal # Display useful info about every signal.
$ kill -9 -f $(pidof python) # kill with force python after getting its PID.
```

8. **pkill**: send a signal to a process using its name.
```shell
$ pkill firefox # kill firefox process (without using -9 because its default to terminate)
```

9. **killall**: send a signal to a process using its name and kill its all windows.
```shell
$ killall firefox # kill all windows of firefox.
```

## **6. Searching Commands**

1. **find**: find files by permissions, size, type, date, name..etc

```shell
$ find [path] [expression] [what to find]
### TESTS
$ find . -name PATTERN # find a specific name
$ find . -iname PATTERN # find a specific name and ignoring case sensitivity

$ find . - executable # find binary files only
$ find . -empty # find empty dir and files

$ find . -size 25 k # find files bigger than 25 kilobyte
$ find . -cmin N # find last file modified where N is number
### OPTIONS
$ find . -maxdepth 2 -iname *.txt # finds all files ends with txt within two sub directories

### ACTIONS
$ find . -amin N - delete # delete the last file accesed.
$ find . -amin N -exec [cmd] {} \; # execute commands on files like this
$ find . -name "*.c" -exec chmod 777 \; # this will change permissions to all files ends with .c to read write execute.
$ find . -amin N -print # print the result to terminal
$ find . -amin N -printf FILE # save the result to a file

### OPERATORS
$ find . -name *.pdf -and -type f # find all files ends with .pdf and is a file
$ find . !(-name *.pdf) # find all files that doesn't have .pdf in the end.
```
2. **locate**: search for files **fast** (similar to find but this one search in db)
```shell
$ locate -c file1.txt # count all files with the name file1.txt in all directories
```

3. **which**: search for the path of the command (where is it located in the $PATH)

```shell
$ which python # prints /usr/bin/python
```

4. **whatis**: Get a one-line description for any command.
```shell
$ whatis ls # outputs: list directory contents.
```

5. **apropos**: Search in the manual pages for the command you're looking for
```shell
$ apropos list # outputs a lot of commands including ls.
```
