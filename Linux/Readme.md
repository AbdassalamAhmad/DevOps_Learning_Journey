
# Linux Resources

I've used <a href="https://www.youtube.com/playlist?list=PLlnHaYmkH6w9FfheDdNnq0ldy6aNKp_3y">"Terminal Tutorial"</a> from YouTube course
to learn Linux basic commands.
<br>

### Commands I've learnt:
1. **Navigation**
* pwd: Print Working Directory.
``` shell
pwd
```
* ls: list all files (and hidden) in a long format
``` shell
ls -l -a
ls -a ../ # list all files in the parent directory.
ls *.txt # lists every file ends with .txt
ls file* # lists all files that start with the word file.
```
* cd: change directory
``` shell
cd - # equals backspace in windows.
cd ..  #back one directory.
cd ../.. # back 2 directories.
cd ~ # cd back to user.
cd / # cd back to root (parent of all parents :) ).
```
2. **Search for help in commands**
``` shell
$ [command] --help
$ man [command] (preferable)
$ info [command]
```

