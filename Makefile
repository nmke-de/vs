
vs: select.sh elb.tsv
	cat select.sh > $@
	echo 'exit 0' >> $@
	echo '#EOF' >> $@
	tar cz elb.tsv >> $@
	chmod +x $@

gen: make.sh select.sh
	cat make.sh > $@
	echo 'exit 0' >> $@
	echo '#EOF' >> $@
	tar cz select.sh >> $@
	chmod +x $@

