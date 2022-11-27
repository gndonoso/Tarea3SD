import sys
import re
a = []
title = ""
for line in sys.stdin:
    line = re.sub(r'\W+',' ',line.strip())

    if(line[:9] == 'WikiTitle'):
        title = line[10:]
    else:
        words = line.split()

        for word in words:
            print('{}\t{}\t{}'.format(word,1,title))