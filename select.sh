#!/bin/sh
# Change the above line if you need to.

SELF="$0"
get_data () {
	sed '1,/^#EOF$/d' < "$SELF" | tar xz -O "$1"
}

get_data elb.tsv | awk "$(D $(get_data elb.tsv | wc -l | cut -d' ' -f1))==NR{print}" | awk 'BEGIN{FS="\t"}{print $1 " " $4 ":" $5 "\t" $6}'

