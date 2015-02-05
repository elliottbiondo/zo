import fnmatch
import re
from os import walk, path

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

print(all_cites)

existing_refs = set()
with open("refs.bib", 'r') as f:
    for line in f.readlines():
        if line[0] == '@':
            existing_refs.add(line.split('{')[1].split(',')[0])

print(existing_refs)
 
missing_refs = all_cites - existing_refs

print(missing_refs)


