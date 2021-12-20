
vs: select.sh elb.tsv
	cat select.sh > $@
	tar cz elb.tsv >> $@
	chmod +x $@

