#!/bin/bash

cd .. #Be inside PROJECT directory 

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
echo $(git commit -m "$COMMIT") 

git push
echo $(git push)
 
