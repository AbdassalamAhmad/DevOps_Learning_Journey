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