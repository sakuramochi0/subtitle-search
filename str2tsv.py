#!/usr/bin/env python3
import sys
import re
import glob

tsv_file = 'sub.tsv'

files = glob.glob('./sub/*.srt')
print(files)
for file in files:
    with open(file) as f:
        text = f.read().split('\n\n')
    ep = re.search(r'.+(\d{2}).srt', file).group(1)

    for line in text:
        match = re.search(r'(\d)+\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+)', line)
        if match:
            id, start, end, script = match.groups()
            record = '\t'.join([ep, id, start, end, script]) + '\n'
            print(record)
            with open(tsv_file, 'a') as f:
                f.write(record)
