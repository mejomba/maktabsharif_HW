#! /bin/bash

echo -n "Enter url: "
read url
echo -n "file name: "
read file_name

touch log.txt

wget $file_name $url

echo $(pwd)/filename >> log.txt
