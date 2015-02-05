import fnmatch
import re
from os import walk, path, getenv

tex_files = set()
for root, dirnames, filenames in walk('.'):
    for filename in fnmatch.filter(filenames, '*.tex'):
        tex_files.add(path.join(root, filename))

all_cites = set()
for tex_file in tex_files:
   with open(tex_file, 'r') as f:
       for line in f.readlines():
           if "\\cite{" in line:
              for m in re.finditer("\\cite{", line):
                  idx = m.end()
                  while line[idx] != "}":
                      idx += 1
                  all_cites.add(line[m.end():idx])

existing_refs = set()
if path.exists("refs.bib"):
    with open("refs.bib", 'r') as f:
        for line in f.readlines():
            if line[0] == '@':
                existing_refs.add(line.split('{')[1].split(',')[0])
 
missing_refs = all_cites - existing_refs

append_string = ""
added_refs = set()
with open(path.join(getenv("HOME"), "refs", "refs.bib"), 'r') as f:
    line = f.readline()
    while line != "":
        if line.strip() != "" and line.strip()[0] == '@' \
            and line.split('{')[1].split(',')[0] in missing_refs:
            ref = line.split('{')[1].split(',')[0] 
            missing_refs.remove(ref)
            added_refs.add(ref)
            append_string += line
            line = f.readline()
            while line.strip() != "" and line.strip()[0] != '@':
                if line.strip()[0] != '#':
                    append_string += line
                line = f.readline()
            append_string += "\n"
        else:
            line = f.readline()

with open("refs.bib", 'a') as f:
    f.write(append_string)
 
if len(added_refs) > 0:               
    print("The following refs were added to the local refs.bib:")
    print("====================================================================")
    for i, ar in enumerate(added_refs):
        print("{0}. {1}".format(i+1, ar))
    if len(missing_refs) > 0:
        print("")

if len(missing_refs) > 0:
    print("Refs not in parent refs.bib and were NOT added to the local refs.bib:")
    print("=========================================================================")
    for i, mr in enumerate(missing_refs):
        print("{0}. {1}".format(i+1, mr))
