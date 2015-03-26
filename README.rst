Overview
--------

This is a barebones reference management system intended to be used in
conjunction with a folder (ostesibly a git repository) containing a collection of .pdf files and
corresponding BibTeX entries. I find zotero/Mendeley/etc. to be too cumbersome.
I have implemented all the capabilities I need in a small Python project.

Motivation
----------

I read and cite a lot of papers, and therefore I desire this process to be streamlined:

1. I want a single folder containing all my documents as .pdfs, so I can easily open them from the command line.
2. I want choose the names for the .pdfs.
3. I want a single .bib file containing all citations.
4. I want the nicknames in the .bib file to match the corresponding .pdfs.
5. For any given LaTeX project, I want to be able to create a child .bib file containing only the references I need from the master.bib file.
6. I want to be able globally grep through all of my .pdfs.

Usage
-----

Setup
=====
1. Store all of your .pdfs in $HOME/refs, ideally a repository.
2. Create a single BibTeX file with all citations (nicknames matching .pdf names) in $HOME/refs/refs.bib
3. Download zo.py and alias it as 'zo': 'alias zo='python /path/to/zo.py'

zo can then be used via the three zo subcommands: status, make, grep.

zo status
=========

The command

>> zo status

can be run from any folder and will print out what .pdfs/citation pairs are
availible, which .pdfs are missing citations, and which citations are missing
.pdfs.

zo make
=======

zo make is used for make a child .bib file from a parent .bib file for
The command

>> zo make

should be run from any directory containing LaTeX files. zo will recursively
search through this folder for .tex files, extract the nicknames of all of the
citations required. It will then look for a local refs.bib file. zo will
compare its contents to the citations from the .tex files. If any citations are
missing, zo will grab them from the $HOME/refs/refs.bib file and append them to
the local file. A message will be printed to stdout to enumerate the citations
that have been append to the local refs.bib and also any citations that were
not found in either ref.bib file. If a local refs.bib is not found a new one
will be printed using the same process.

The pathes to the project, parent .bib, and child .bib can also be specified explicitly:

optional arguments:
  -h, --help            show this help message and exit
  -j PROJECT, --project PROJECT
                        The directory contain the LaTeX project
  -p PARENT, --parent PARENT
                        A parent .bib file
  -c CHILD, --child CHILD
                        The child ref.bib file to be produced

zo grep
=======

The command

>> zo grep [any grep command options]

is used to globally search through all .pdfs. The command returns a list of
.pdfs that contain the match. This works by calling pdftotext. Any grep options
are valid.

Contributing
------------

All pull requests will be considered. However it must be understood that the one of
the fundamental tenets of this project is simplicity, so dependencies and feature bloat will be judged harsely.


Pending Features
----------------

BibTeX reads .aux and .bib files and creates .bbl files, formated in a fashion
described in the .bst file. However .bst files are a mess. There has got to be a better solution...


