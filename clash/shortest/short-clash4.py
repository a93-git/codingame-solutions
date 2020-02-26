""" Find the longest iteration of '0' in a given number """

import re
n=input()
a=re.compile(r'[0]+')
try: print(len(sorted(re.findall(a, n))[-1]))
except: print(0)