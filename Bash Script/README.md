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

## 10. String Comparisons
| Syntax  | Description     		|
| --------| :---------------------: |
| <       |	less than 				|
| >       |	greater than 			|
| -n s1   |	string s1 is not empty  |
| -z s1   |	string s1 is empty 		|
| =       |	equal 					|
| !=      |	not equal 				|