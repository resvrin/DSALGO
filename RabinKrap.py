line  = 'Thisisaword'
pattern = 'word'

p = len(pattern)

def convert(pat):
    out = 0
    for i in pat:
        out += ord(i)
    return out
def rabin(line, pattern, ):
    for i in line.split():
        #print(i)
        if len(i)  == p:
            if convert(i) == convert(pattern):
                return i
        continue
def rabin_seq(line, pattern):
    for idx in range(2, len(line)):
        i = idx - 1
        j = i - 1



print(rabin(line, pattern))
