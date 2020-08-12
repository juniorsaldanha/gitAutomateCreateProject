#!/bin/bash

function create() {
    source .envgit
    python3 .git.py $1
    cd $FILEPATH$1
    git init
    git remote add origin git@github.com:$USERNAMEGIT/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit - Started Project with Automated py script"
    git push -u origin master
    code .
}
