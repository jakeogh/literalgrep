'''
$ hexdump madness ; cat madness ; cat madness | ./literalgrep.py --verbose "'mad\t" ; echo $?
0000000 22 22 22 27 6d 61 64 09 22 6e 65 73 73 0a
0000016
"""'mad "ness
match: b"'mad\t"
line: b'"""\'mad\t"ness'
"""'mad "ness
0
'''

