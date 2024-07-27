#!/bin/bash

#^^Shebang^^

echo "This is a shell script."

# Needs to be revised
print (){
    echo
    echo "Function has been called." 
     if [[ $3 = "" ]]; then
	echo "Arg3 has not been passed."
    elif [[ $2 = $3 ]]; then
	echo "Arg2 and Arg3 are equal."
	read -p "Please change Arg2 = " $2
    else
	echo "There is no problem about the arguments."
    fi

    let "index = 1"
    for arg in $@
	do
	    if [[ arg = ""  ]]; then
		echo "Arg$index is null."
	    else
		echo "Arg$index = $($argNum)"
	    fi
	let "index = $(( index + 1 ))"
    done
    echo
}

print xd xxd
print "xd xxd xxxd" 5+10 10
read -p "Arg1 = " arg1
read -p "Arg2 = " arg2
read -p "Arg3 = " arg3
print $arg1 $arg2 $arg3

# Exit code 0 means successful, 1 means failure. These are conventional and do not effect the program directly
# It is good to have exit code signing whether the scrip is successful or not
exit 0
