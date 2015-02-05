Oerview
--------

This is a barebones reference management system intended to be used in
conjunction with a git repository containing a collection of .pdf files and
corresponding BibTeX entries. I find Zotero/Mendeley/etc. to be too cumbersome.
I have implemented all the capabilities I need in < 100 lines of Python.

Motivation
----------

I read and cite a lot of papers, and therefore I desire this process to be strealined. The capabilities I value are enumerated below:

1. I want a single folder containing all my documents as .pdfs, so I can easily open them from the command line.
2. I want choose the names for the .pdfs.
3. I want a single BibTeX .bib file containing all citations.
4. I want the nicknames in the BibTeX file to match the corresponding .pdfs.
5. For any given LaTeX project, I want to be able to create a child .bib file containing only the references I need from the master.bib file.

That's it -- nothing else. I understand that by using real reference management
software I would a lot of features for free (e.g. searching, sharing,
importing citations from Elsevier, etc). They above 4 criteria take precedent
over all of these features.

Usage
-----

Setup
=====
1. Store all of your .pdfs in $HOME/refs, ideally a repository.
2. Create a single BibTeX file with all citations (nicknames matching .pdf names) in $HOME/refs/refs.bib
3. Download zo.py and alias it as 'zo': 'alias zo='python /path/to/zo.py'

Status
======

The command

>> zo status

can be run from any folder and will print out what .pdfs/citation pairs are availible, which .pdfs are missing citations, and which citations are missing .pdfs.

Making child refs.bib files
=======================

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

