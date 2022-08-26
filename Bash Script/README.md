# Bash Script Resources

- I've used [**bash-scripting-tutorial**](https://linuxconfig.org/bash-scripting-tutorial) to learn Bash Scripting basics.
- I've used [**Bash-Script Cheatsheet**](https://devhints.io/bash) to learn Bash Scripting basics.

# Commands I've Learned: 

## 1. Hello World Script:
```bash
#!/bin/bash
# declare STRING variable
STRING="Hello World"
# print variable on a screen
echo $STRING
```

## 2. Create Simple Backup Script:
```bash
#!/bin/bash
OF=myhome_directory_$(date +%Y%m%d).tar.gz # name of the file using date to know which date the backup created and using variables.
tar -czf $OF /home/linuxconfig # creating the backup file of the user home directory.
```

## 3. Difference Between Local and Global Variables:
```bash
#!/bin/bash
# This variable is global and can be used anywhere in this bash script
VAR="global variable"

function locvar {
# Define bash local variable
# This variable is local to bash function only
local VAR="local variable"
echo $VAR
}

echo $VAR # Outputs the "global variable"
locvar # Outputs "local variable" inside the function.
# Note the bash global variable did not change
```

