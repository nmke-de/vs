#!/bin/sh
# Change the above line if you need to.

#book="$(elb -l | cut -d'(' -f2 | tr -d ')' | line $(D 66))"
#echo $book

raw=`line $(D $(wc -l elb.tsv | cut -d' ' -f1)) from elb.tsv`
echo $raw
