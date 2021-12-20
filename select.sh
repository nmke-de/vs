#!/bin/sh
# Change the above line if you need to.

#book="$(elb -l | cut -d'(' -f2 | tr -d ')' | line $(D 66))"
#echo $book

line $(D $(wc -l elb.tsv | cut -d' ' -f1)) from elb.tsv | awk 'BEGIN{FS="\t"}{print $1 " " $4 ":" $5 "\t" $6}'
#echo $raw
