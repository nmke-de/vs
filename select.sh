#!/bin/sh
# Change the above line if you need to.

SELF="$0"
get_data () {
	sed '1,/^#EOF$/d' < "$SELF" | tar xz -O "$1"
}

lines=$(get_data elb.tsv | wc -l | cut -d' ' -f1)
get_data elb.tsv | awk "BEGIN{FS=\"\\t\"; srand();r=int(rand()*$lines)+1} r==NR{print \$1 \" \" \$4 \":\" \$5 \"\\t\" \$6}"

