#!/bin/env python

import os

os.system("pandoc -i report.tex -i Sektioner/*.tex -o report.docx")
