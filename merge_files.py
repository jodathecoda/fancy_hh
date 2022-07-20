import os
import sys
import re

global cwd
cwd = os.getcwd()

all_lines = []
lines = []

for filename in os.listdir(cwd):
  #print(file)
  if filename.endswith("log"):
    f = os.path.join(cwd, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        with open(f) as file:
            lines = file.readlines()
            #lines = [line.rstrip() for line in lines]
        #f.close()
    for l in lines:
        all_lines.append(l)

f = open("merged_file.log", "x")
for al in all_lines:
    f.write(al)
f.close()





