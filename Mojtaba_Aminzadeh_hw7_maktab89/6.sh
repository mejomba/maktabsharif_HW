#! /bin/bash

echo -n "source directory name: "
read source_directory

echo -n "directory name for copy: "
read directory

for item in "$source_directory"/*; do
	file_name=$(echo "$item" | grep a)
	if [[ -f $file_name ]] && [[ $(file $file_name | grep -i "ascii text") ]]; then
		echo "find $file_name ::>>> copy to $directory"
		cp $file_name $directory
	fi
done
