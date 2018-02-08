from collections import Counter
from string import maketrans
def super(i):
    table = {ord('0')+i:0x2070+i for i in range(10)}
    table.update({0x31:0xb9, 0x32:0xb2, 0x33:0xb3})
    return unicode(i).translate(table)
def f(n):
    def f2(n):
        for i in range(2,n+1):
            while n%i == 0:
                yield i
                n /= i
    primes = Counter(f2(n))
    return u' '.join(unicode(k)+super(v) for k,v in sorted(primes.items()))

print f(5)
print f(125)
print f(4096*3*7)
