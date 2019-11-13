#!/bin/python

import os

abspath = os.path.abspath(os.path.curdir)
secPath = os.path.join(abspath, "Sektioner")
sectionsDocPath = os.path.join(secPath, "sections.tex")

# Get all files in Sections dir
sections = os.listdir(secPath)

# sort sections
sections.sort()

# Write to file sections.tex
if os.path.exists(sectionsDocPath):
    os.remove(sectionsDocPath)
with open(sectionsDocPath, 'w+') as f:
    for section in sections:
        if section[0] == '!':
            continue

        str = "\import{Sektioner/}{" + section + "}\n"
        f.write(str)
