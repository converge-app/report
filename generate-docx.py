# /usr/bin/env python

import os

os.system("pandoc -i report.tex Sektioner/*.tex -o report.docx")
