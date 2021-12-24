# Verse/Selector

Select a bible verse (or something similar) at random!

## Why would I want this?

I don't know. Perhaps to have something to greet you when you log in to your shell?

## Dependencies

- sh (i.e. bash
- awk (i.e. gawk)
- make (i.e. gmake)
- tar
- sed
- wc
- cat (usually included in your shell)
- chmod (usually a system utility)

If you follow *every* step of the following guide, you should also check whether you have `git` installed.

## Build

### Default Build

The default build uses the German Elberfelder Bibel as its source.

1. Get this repository: `git clone https://www.github.com/nmke-de/vs.git`
2. Do this: `cd vs`
3. Make. `make vs`
4. Put your executable wherever you want. `mv vs /path/to/wherever/you/want`

### Using a custom `.tsv`

You might want something else than the German Elberfelder Bibel. The file to use needs to be of the same format as `elb.tsv` in the repository, that is

1. the bookname,
2. short cut name of the book,
3. book number,
4. chapter number,
5. verse number,
6. verse content

in each line, tab-separated. If you use anthing comparable in scale to a bible, for example a bible, I advise you to use a script to generate the file.

Then, proceed with the following steps:

1. Get this repository: `git clone https://www.github.com/nmke-de/vs.git`
2. Do this: `cd vs`
3. Make. `make gen` – Note that you make the correct file, as `vs` will be useless for using a custom `.tsv` at this point.
4. Copy your custom `.tsv`-file into this directory (or copy `gen` to the directory with your custom `.tsv`-file and go there).
5. Do this: `./gen yourcustomfile.tsv`, but replace `yourcustomfile.tsv` with the name of your custom `.tsv`-file.
6. Put your executable wherever you want. `mv vs /path/to/wherever/you/want`

## Usage

```
vs --help

	or:

vs -h
	or:

vs [-o <Outputfile>] <Inputfile>
``` 

