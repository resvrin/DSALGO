
def seq(array, sequence):
    arridx = 0
    seqidx = 0
    while arridx < len(array) and seqidx < len(sequence):
        print(array[arridx], sequence[seqidx])
        if array[arridx] == sequence[seqidx]:
            seqidx += 1
        arridx += 1
    print( seqidx == len(sequence))

a = [5, 1, 22, 25, 6, -1, 8, 10]
s = [1, 6, -1, 10]

seq(a, s)
