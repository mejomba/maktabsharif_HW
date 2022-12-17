#! /bin/bash

echo -n "Enter number: "
read number

while [[ "$number" != "exit" ]]; do
	echo $(( $number * $number ))
	echo -n "Enter number: "
	read number
done
