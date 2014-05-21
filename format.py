#!/usr/bin/env python3
import csv
import zenhan

csv_file = 'sub.csv'
mod_file = 'sub_mod.csv'

from_chara = ['m', 'y', 'h', 'r', 'b', 's', 'o', 'k',
              'a', 'c', 'n', 'w', 'l', 'f',
              'i', 'g', 'q', 'd', 'v', 'z']
to_chara = ['愛乃めぐみ', '大森ゆうこ', '白雪ひめ', 'リボン', 'ブルー', '相楽誠司', '相楽真央', '愛乃かおり',
            'サイアーク', 'チョイアーク', 'ナマケルダ', 'ホッシーワ', 'オレスキー', 'ファントム',
            '氷川いおな', 'ぐらさん', 'クイーンミラージュ', 'ディープミラー', '増子美代', '和泉先生']
sub_chara = to_chara + ['めぐみ', 'ゆうこ', 'ひめ', '誠司', '真央', 'かおり', 'いおな', '美代',
                        'キュアラブリー', 'キュアプリンセス', 'キュアハニー', 'キュアフォーチュン',
                        'ラブリー', 'プリンセス', 'ハニー', 'フォーチュン',
                        '女性', 'チョイアークたち', 'チョイアーク', 'チョイ審判',
                        '卓真', '健太', '子どもたち']

with open(csv_file) as f:
    header = f.readline()
    rows = []
    for row in csv.reader(f):
        ep, num, start, end, chara, sub = row
        # replace abbr with full-name in chara field
        for f, t in zip(from_chara, to_chara):
            chara = chara.replace(f, t)
        # remove unnecessary '（name）' in sub field
        for c in sub_chara:
            sub = sub.replace('（{}）'.format(c), '')
        # convert zenkaku to hankaku
        sub = zenhan.z2h(sub, mode=zenhan.ASCII+zenhan.DIGIT)
        # print subs including '（name）'
            # if '（' in sub:
            # print(sub)
        rows.append([ep, num, start, end, chara, sub])
        
with open(mod_file, 'w') as f:
    f.write(header)
    csv.writer(f).writerows(rows)
