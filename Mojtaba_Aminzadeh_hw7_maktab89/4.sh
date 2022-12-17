#! /bin/bash

echo -n "source directory name: "
read source_directory

echo -n "file  name for copy: "
read directory

for item in "$source_directory"/*; do
	# file_name=$(echo "$item" | grep a)
	if [[ -f $item ]] && [[ $(file $item | grep -i "ascii text") ]]; then
		cat $item >> $directory
	fi
done

sort $directory | sed -n "6,10P"
