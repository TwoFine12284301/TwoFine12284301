#!/bin/bash

echo RESULTS  of IF

if [ $(pwd) = /home/twofine/PROJECTS ]; 
 then 
  echo Inside Directory PROJECTS
 else
  pwd
  echo Not Inside PROJECTS
fi


