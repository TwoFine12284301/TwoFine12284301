#!/bin/bash

#This script will automate the process of adding commiting and pushing
#When asked directory by simply typing the directory of the file that needs to be changed will satisfy. 

#Be inside PROJECT directory 
if [ $(pwd) != ../../PROJECTS ];
 then
  cd ../../PROJECTS
  pwd
 else
  echo The Program is not inside desired file
  exit
fi

#show status
#This helps facilitate what to add
git status

#chech if $1 is empty if it is then ask for a directory
if [ -z $1 ] 
 then 
  echo "Enter a directory"
  read D1
else
 D1=$1
fi

#add to respository
git add "$D1" 

#Ask for a comment to commit
echo "Commit Comment?" 
read COMMIT

#Commit 
git commit -m "$COMMIT" 

#Push to respository
git push
 
