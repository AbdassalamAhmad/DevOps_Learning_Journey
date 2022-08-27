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

## 4. Passing arguments and using echo:
```bash
#!/bin/bash
# use predefined variables to access passed arguments
#echo arguments to the shell
echo $1 $2 $3 ' The command was echo $1 $2 $3'

# We can also store arguments from bash command line in special array
args=("$@") # store variables in args array.
#echo arguments to the shell
echo ${args[0]} ${args[1]} ${args[2]} ' args in an array'

#use $@ to print out all arguments at once
echo $@ 'print out all args'

# use $# variable to print out
# number of arguments passed to the bash script
echo Number of arguments passed: $# '$#' 
```

## 5. Reading User Input:
```bash
#!/bin/bash
 
echo -e "Hi, please type the word: \c " # \c to write in the same line, -e to enable backslash job
read  word
echo "The word you entered is: $word"

echo -e "Can you please enter two words? \c "
read word1 word2
echo "Here is your input: \"$word1\" \"$word2\""

echo -e "How do you feel about bash scripting? \c"
read # read command now stores a reply into the default build-in variable $REPLY
echo "You said $REPLY, I'm glad to hear that! "

echo -e "What are your favorite colours ? \c"
read -a colours # -a read into an array.
echo "My favorite colours are also ${colours[0]}, ${colours[1]} and ${colours[2]}:-)"
```

## 6. Declare Simple Bash Array:
```bash
#!/bin/bash
# Declare array with 4 elements
ARRAY=( 'Debian Linux' 'Redhat Linux' Ubuntu Linux )
# get number of elements in the array
ELEMENTS=${#ARRAY[@]}

# echo each element in array 
# for loop
for (( i=0;i<$ELEMENTS;i++)); do
    echo ${ARRAY[${i}]}
done 
```