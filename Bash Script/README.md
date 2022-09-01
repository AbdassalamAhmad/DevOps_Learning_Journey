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
ARRAY=( 'Debian Linux' ,'Redhat Linux' Ubuntu  Linux )
# get number of elements in the array
ELEMENTS=${#ARRAY[@]} # outputs 4

# print each element in array 
for (( i=0;i<$ELEMENTS;i++)); do # foe loop like C language.
    echo ${ARRAY[${i}]}
done 
```

## 7. if/else Statement:
```bash
#!/bin/bash
#Usage:
# when running the script in a directory search for a directory called "BashScripting", If it's there print it exists otherwise print it doesn't exists.
directory="./BashScripting"
backup="/backup" # this directory we can ask for it as well if we want in the future.
# bash check if directory exists
if [ -d $directory ]; then
	echo "${directory:2:-1} directory exists"
else 
	echo "${directory:2:-1} directory does not exist"
fi
```

## 8. Nested if/else:
```bash
echo "waht is your favorite meal?: "
echo "1. taco"
echo "2. fried potatos"
echo "3. salad"
read choice

if [ $choice -eq 1 ]; then
	echo "you've chosen taco"
if [ $choice -eq 1 ]; then
	echo "you've chosen fried potato"
if [ $choice -eq 1 ]; then
	echo "you've chosen salad"
else
	echo "you should only type 1 or 2 or 3"
fi
```

## 9. Arithmetic Comparisons:

| Syntax    | Symbol        | Description 		    |
| ----------| :-----------: | :-------------------: |
| -lt 		|	< 			| less than 			|
| -gt 		|	> 			| greater than 			|
| -le 		|	<= 			| less than or equal 	|
| -ge 		|	>= 			| greater than or equal |
| -eq 		|	== 			| equal 				|
| -ne 		|	!= 			| not equal 			|

## 10. String Comparisons:
| Syntax  | Description     		|
| --------| :---------------------: |
| <       |	less than 				|
| >       |	greater than 			|
| -n s1   |	string s1 is not empty  |
| -z s1   |	string s1 is empty 		|
| =       |	equal 					|
| !=      |	not equal 				|



## 11. File Testing:
| Syntax		     | Description     		     		     		     		        |
| -------------------| :--------------------------------------------------------------: |
|-d  directoryname	 |	Check for directory existence 									|
|-e  filename	 	 |	Check for file existence 										|
|-f  filename	 	 |	Check for regular file existence not a directory 				|
|-O  filename	 	 |	True if file exists and is owned by the effective user id. 		|
|-r  filename	 	 |	Check if file is a readable 									|
|-w  filename	 	 |	Check if file is writable 										|
|-x  filename	 	 |	Check if file is executable 									|
|-s  filename	 	 |	Check if file is nonzero size 									|
| file1 -ef file2    |  Check if file1 same as file2									|
```bash
#!/bin/bash

while [ ! -e file1 ]; do
# Sleep until file1 created
	sleep 1
done
```

## 12. Loops:
- **for loop**:
```bash
#!/bin/bash

# print all of the files and dir in '/var/' dir.
for f in $( ls /var/ ); do
	echo $f
done
```
```bash
# count from 0 till 10
for ((i = 0 ; i < 10 ; i++)); do
	echo $i
done
```

- **while loop**:
```bash
#!/bin/bash

COUNT=6
# Count from 6 till 0.
while [ $COUNT -gt 0 ]; do
	echo Value of count is: $COUNT
	let COUNT=COUNT-1
done
```

```bash
#!/bin/bash
# USAGE: This bash script will locate and replace spaces with '_' in this DIR and its subdir.

DIR="."
# Controlling a loop with bash read command by redirecting STDOUT as
# a STDIN to while loop
# find will not truncate filenames containing spaces
find $DIR -type f | while read file; do
# using POSIX class [:space:] to find space in the filename
if [ "$file" = *[[:space:]]* ]; then # the file be anything(*) then space then anything(*) ; *space*
	# substitute space with "_" character and consequently rename the file
	mv "$file" `echo $file | tr ' ' '_'`
fi;
# end of while loop
done
```

- **until loop**:
```bash
#!/bin/bash

COUNT=0
# Count from 0 till 5
until [ $COUNT -gt 5 ]; do
	echo Value of count is: $COUNT
	let COUNT=COUNT+1
done
```

## 13. Functions:
```bash
#!/bin/bash
# BASH FUNCTIONS CAN BE DECLARED IN ANY ORDER
function function_B {
    echo Function B.
}
function function_A {
    echo $1
}
function function_D {
    echo Function D.
}
function function_C {
    echo $1
}
# FUNCTION CALLS
# Pass parameter to function A
function_A "Function A."
function_B
# Pass parameter to function C
function_C "Function C."
function_D
# output : 
# Function A.
# Function B.
# Function C.
# Function D.
```

## 14. Case:
```bash
#!/bin/bash

echo -n "Enter the name of a country: "
read COUNTRY

echo -n "The official language of $COUNTRY is "

case $COUNTRY in

  Lithuania) echo "Lithuanian";;

  Romania | Moldova) echo "Romanian";;

  Italy | "San Marino" | Switzerland | "Vatican City") echo "Italian";;

  *) echo "unknown";; # anything else unknown.
esac
```

## 15. Arithmetic Operations:
```bash
#!/bin/bash
 
let RESULT1=$1+$2 # Here the addition works
echo $1+$2=$RESULT1 # Outputs 7+3=10

declare -i RESULT2 # declare a numerical variable.
RESULT2=$1-$2
echo $1-$2=$RESULT2 

echo $1*$2=$(($1 * $2)) # the last expression (()) is where the multiplication happened.
echo 7 % 7 = $[ 7 % 7 ] # the last expression [] is where the modulo happened.
```