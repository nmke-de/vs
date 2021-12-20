#!/bin/sh
# Change the above line if you need to.

line $(D $(wc -l elb.tsv | cut -d' ' -f1)) from elb.tsv | awk 'BEGIN{FS="\t"}{print $1 " " $4 ":" $5 "\t" $6}'

