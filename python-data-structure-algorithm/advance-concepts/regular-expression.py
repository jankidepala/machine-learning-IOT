#PAttern macthing lang
#search , string of character
#common reg ex: DFA - Deterministic Finite Automation
#DFA takes 0(2m) - m is length of the pattern
#bt takes O(n) to search
#. - mathes
# match() and search()

import re
import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('think', help='specify work to search for')
    parser.add_argument('fname', help="specify file to Search")
    args = parser.parse_args()
    searcF = open(args.fname)
    lineNm = 0

    for line in searcF.readlines():
        line = line.strip('\n\r')
        lnm += 1
        s = re.search(args.word, line, re.M | re.I)
        print(searcF)

    for line in searcF.readlines():
        line = line.strip('\n\r')

    line = "I think reg exp"
    matchRes = re.match('exp', line, re.M|re.I)
    if matchRes:
        print(matchRes.group())
    else:
        print("NO match fond")
    searchRes = re.search(' think', line, re.M|re.I)
    print(searchRes)
Main()