import fnmatch
import os

files = set()
for root, dirnames, filenames in os.walk('.'):
    for filename in fnmatch.filter(filenames, '*.pdf'):
        files.add(filename.split(".")[0])

refs = set()
with open("refs.bib", 'r') as f:
    for line in f.readlines():
        if line[0] == '@':
            refs.add(line.split('{')[1].split(',')[0])

print("\nfiles that are good to go:")
print("==============================")
for x in (files & refs):
    print x

print("\nfiles missing .bib entries:")
print("==============================")
for x in (files - refs):
    print x

print("\n.bib entries missing files:")
print("==============================")
for x in (refs - files):
    print x
