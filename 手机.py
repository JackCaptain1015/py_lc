import requests
import sys
import urllib.request
import json
from phone import Phone

phSearch = Phone()

head = [133,149,153,173,177,180,181,189,199,191]
end = ''
phoneArr = [];
exclude = [9118,9120,9317,9487,0,1,792,31,848,697,425,228,13,808,247,436,25,981,791,435,39,397,987,771,434,985,30,388,779,573,12,362,552,962,27,321,569,949,145,360,713,142,926,575,98,717,62,161];
for h in head:
    for i in range(0,1000):
        zero = 3-len(str(i))
        mid = str(i);
        for z in range(0,zero):
            mid = '0'+mid;
        phone = str(h) + mid + end;
        phoneArr.append(phone)
i = 0;
file = open("D:\\contact.txt","w")
for p in phoneArr:

    s = """BEGIN:VCARD
VERSION:2.1
N:;{0};;;
FN:{0}
TEL;CELL:{1}
END:VCARD
"""
    s = s.replace('{0}',str(i));
    s = s.replace('{1}',p);
    if i not in exclude:
        belong = phSearch.find(str(p))
        if belong and "杭州" in belong['city']:
            file.write(s)

    i = i+1;

file.close()

