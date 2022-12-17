#! /bin/bash

file_count=$(ls -l $1 | grep -c ^[-l] )
folder_count=$(ls -l $1 | grep -c ^d )

echo "Number of files: " "$file_count"
echo "Number of folders: " "$folder_count"
