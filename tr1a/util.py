import string
import sys
from typing import Union

LOWER_CHARS = string.ascii_lowercase
LOWER_SIZE = len(LOWER_CHARS)


def num2char(num: int) -> str:
    if num < LOWER_SIZE:
        return LOWER_CHARS[num]
    else:
        d, m = divmod(num, LOWER_SIZE)
        return str(d) + LOWER_CHARS[m]


def fix_arg(w1: Union[str, list], w2: str) -> str:
    w2 = w2.strip()
    lw1 = len(w1)
    lw2 = len(w2)
    if lw1 > lw2:
        lp = lw1 - lw2
        while True:
            if lp > lw2:
                w2 = w2 * 2
                lp = lp - lw2
                lw2 = len(w2)
            else:
                w2 = w2 + w2[:lp]
                break
    else:
        w2 = w2[:lw1]
    return w2


def rec_word(w1: str, w2: str) -> str:
    fix_w1 = []
    wt = ''
    for i in range(0, len(w1)):
        c = ord(w1[i])
        if ord('0') <= c <= ord('9'):
            wt = wt + chr(c)
        else:
            if wt == '':
                fix_w1.append(chr(c))
            else:
                fix_w1.append((int(wt), chr(c)))
                wt = ''
    w2 = fix_arg(fix_w1, w2)
    ret = []
    for i in range(0, len(fix_w1)):
        c1 = fix_w1[i]
        c2 = ord(w2[i])
        if isinstance(c1, str):
            cm = LOWER_CHARS.index(c1) ^ c2
            ret.append(chr(cm))
        else:
            cm = (c1[0] * LOWER_SIZE + LOWER_CHARS.index(c1[1])) ^ c2
            ret.append(chr(cm))
    return ''.join(ret)


def mix_word(w1: str, w2: str) -> str:
    w2 = fix_arg(w1, w2)
    ret = []
    for i in range(0, len(w1)):
        c1 = ord(w1[i])
        c2 = ord(w2[i])
        cm = c1 ^ c2
        ret.append(num2char(cm))
    return ''.join(ret)


def mix_file(filename: str, w2: str):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line != '':
                print(mix_word(line, w2))
        print(w2[::-1])


def rec_file(filename: str):
    with open(filename, 'r') as f:
        lines = f.readlines()
        ws = []
        for line in lines:
            line = line.strip()
            ws.append(line)
        w2 = ws[-1][::-1]
        for w1 in ws[:-1]:
            print(rec_word(w1, w2))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s <command> <filename> [<w2>]' % sys.argv[0])
    if len(sys.argv) < 4:
        k = 'fuck'
    else:
        k = sys.argv[3]
    if sys.argv[1] == 'mix':
        mix_file(sys.argv[2], k)
    else:
        rec_file(sys.argv[2])
