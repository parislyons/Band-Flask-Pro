#!/bin/bash

source .venv/bin/activate

if [ ! -f application/*.db ]
  then python3 create.py
  echo "Successfully created database"
fi
