#!/bin/bash

## Pretend this is a working Bash script - for now, this is just a shell
## For my money, I'd actually write this in Python or Ruby
## So consider this pseudo-code for now

# --[ STEP 00 ]--
# Request login page

# --[ STEP 01 ]--
# Log into WebGoat

# --[ STEP 02 ]--
# Figure out which menu item is "Http Basics"

# --[ STEP 3 ]--
# Request the lesson for General => Http Basics

# --[ STEP 4 ]--
# Submit the attack to the General => Http Basics page
ATTACK=`echo -n "1"`

# Purposefully fail for testing purposes
#ATTACK=`echo -n "1"`

# --[ STEP 6 ]--
# Set the correct exit code
# It will return a
# - 0 (error) if the vulnerability is present
# - 1 (success) if the vulnerability is fixed (aka not present)

if [ $ATTACK -eq 1 ]
then
    # Attack successful
    echo "Attack Successful"
    exit 1
else
    # Attack failed - no vuln-00 present
    echo "vuln-00 not present"
    exit 0
f
