#!/bin/bash

function create() {
    source .envgit
    python3 .git.py $1
    cd $FILEPATH$1
    git init
    git remote add origin git@github.com:$USERNAMEGIT/$1.git
    touch README.md
    git add .
    git commit -m "Commit Automated - Horas: $(date +%H:%M:%S) - $(date +%a), dia $(date +%d) de $(date +%b) de $(date +%Y)"
    git push -u origin master
    code .
}
