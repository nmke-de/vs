#!/bin/sh
# Change the above line if you need to.

SELF="$0"
get_data () {
	sed '1,/^#EOF$/d' < "$SELF" | tar xz -O "$1"
}

infile=""
outfile=""
ap_state="normal"
while [ $# -gt 0 ]; do
	[ $ap_state = "get_outfile" ] && outfile=$1 && ap_state="normal" && continue
	[ $1 = "-o" ] && [$ap_state = "normal" ] && ap_state="get_outfile" && continue
	[ $1 = "-h" ] && echo "Syntax: $0 [-h|-o Outputfile] Inputfile" && exit 0
	[ $1 = "--help" ] && echo "Syntax: $0 [--help|-h|-o Outputfile] Inputfile" && exit 0
done

test -z $infile && echo "No input file." >> /dev/stderr && exit 1

echo "Using $infile to make Verse/Selector $outfile..." >> /dev/stderr
get_data select.sh > $outfile
echo 'exit 0' >> $outfile
echo '#EOF' >> $outfile
tar cz $infile >> $outfile
chmod +x $outfile
echo "Done."

