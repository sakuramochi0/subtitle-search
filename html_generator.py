#!/usr/bin/env python3
import subprocess

sub_file = 'sub_mod.csv'
table_file = 'sub.html'
header_file = 'header.html'
fooder_file = 'fooder.html'
html_file = 'index.html'

# convert csv to html table
subprocess.call(['csv2html', '-o', table_file, sub_file])

with open(header_file) as f:
    header = f.read()
with open(table_file) as f:
    table = f.read()
with open(fooder_file) as f:
    fooder = f.read()
    
html = header + table + fooder
with open(html_file, 'w') as f:
    f.write(html)
