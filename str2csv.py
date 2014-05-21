#!/usr/bin/env python3
# str2csv.py - append subtitle rows to the end of the subtitle data csv file 
#   input: subtitle(.str) text
#   output: csv
#     column: ep, num, start, end, chara, subtitle
#       ep: episode number
#       num: subtitle number numbered by a episode
#       start: subtitle appear at this time
#       end: subtitle disappear at this time
#       chara: character who say the subtitle (default: '')
#       subtitle: subtitle text

import sys
import re

out_file = 'sub.csv'

with open(sys.argv[1]) as f:
    text = f.read().split('\n\n')
ep = re.search(r'.+(\d{2}).srt', file).group(1)

for line in text:
    pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+(\n.+)*)')
    match = re.search(pattern, line)
    if match:
        num, start, end = match.group(1), match.group(2), match.group(3)
        for sub in match.group(4).split('\n'):
            record = '\t'.join([ep, num, start, end, sub]) + '\n'
            print(record)
            with open(out_file, 'a') as f:
                f.write(record)
