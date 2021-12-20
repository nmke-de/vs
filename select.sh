#!/bin/sh
# Change the above line if you need to.

SELF="$0"
get_data () {
	sed '1,/^#EOF$/d' < "$SELF" | tar xz -O "$1"
}

line $(D $(wc -l elb.tsv | cut -d' ' -f1)) from elb.tsv | awk 'BEGIN{FS="\t"}{print $1 " " $4 ":" $5 "\t" $6}'

exit 0
#EOF

