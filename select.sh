#!/bin/sh
# Change the above line if you need to.

book="$(elb -l | cut -d'(' -f2 | tr -d ')' | line $(D 66))"
echo $book

