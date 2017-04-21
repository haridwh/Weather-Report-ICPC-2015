from heapq import heappush, heappop, heapify
from collections import defaultdict
# berapa kali percobaan
n = int(input("Jumlah Observasi : "))
# probabilitas tiap cuaca [sunny, cloudy, rainny, foggy]
prob = [0.1, 0.2, 0.3, 0.4]
# prob = [0.9, 0.049999, 0.05, 0.000001]
# nProb = {'ss':0.81,'sc':0.0449991,'sr':0.045,'sf':0.0000009,'cs':0.0449991,'cc':0.0024999,'cr':0.00249995,'cf':0.0000005,'rs':0.045,'rc':0.00249995,'rr':0.0025,'rf':0.00000005,'fs':0.0000009,'fc':0.00000005,'fr':0.00000005,'ff':0.000000000001}

def getKey(nSize):
    key = ""
    for i in xrange(len(nSize)):
        if (nSize[i] == 0):
            key += "s"
        elif (nSize[i] == 1):
            key += "c"
        elif (nSize[i] == 2):
            key += "r"
        elif (nSize[i] == 3):
            key += "f"
    return key

# fungsi untuk perkalian data berdasar percobaan nya
def getProb(val, n):
    if n==1:
        return val
    else:
        # print nSize[0], " * ", nSize[n-1], " = ", val * prob[nSize[n-1]]
        return getProb(val * prob[nSize[n-1]], n-1)

#fungsi membuat pohon huffman
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

#menghitung hasil menggunakan hasil dari pohon huffman
def getResult(newProb):
    result = 0
    huff = encode(newProb)
    for p in huff:
        result += newProb[p[0]]*len(p[1])
    # print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])
    return result


# TAHAP INISIALISASI NILAI PROBABILITAS
nSize = []
for i in range(n):
    nSize.append(0)
sq = []
for i in range(n):
    sq.append(0)
newProb = {}
size = len(prob)**n
for i in range(size):
    val = getProb(prob[nSize[0]], n)
    newProb[getKey(nSize)] = val
    for k in range(n):
        sq[k] +=1
    size = len(prob)**n
    for j in range(n):
        size = size/4
        if size == sq[j]:
            nSize[j] += 1
            if nSize[j] >= len(prob):
                nSize[j] = 0
            sq[j] = 0

print getResult(newProb)
