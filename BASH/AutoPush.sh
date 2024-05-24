#!/bin/bash

#Be inside PROJECT directory 
if [ $(pwd) != ../../PROJECTS ];
 then
  cd ../../PROJECTS
  pwd
 else
  echo The Program is not inside desired file
  exit
fi

if [ -z $1 ] 
 then 
  echo "Enter a directory"
  read D1
else
 D1=$1
fi

git add "$D1"
echo $(git add "$D1") 

echo "Commit Comment?" 

read COMMIT
#echo $COMMIT

git commit -m "$COMMIT" 

git push
 
