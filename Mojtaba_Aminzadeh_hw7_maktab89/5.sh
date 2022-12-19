#! /bin/bash

echo -n "directory name: "
read directory
if ! [ -d $directory ]; then
	mkdir $directory
else
echo "directory $directory exsits"
fi
