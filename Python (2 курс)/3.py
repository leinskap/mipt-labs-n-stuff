#1
p = 3
q = 7
n = p*q
f = (p-1)*(q-1)
e = 5
print('open', e, n)
d = 17
print('closed', d, n)
m = 19
E = pow(m, e, n)
print(pow(E, d, n))
class a:
    def __init__(self, e, n, d):
        self.e = e
        self.n = n
        self.d = d
    def encrypt(self, m):
        return(pow(m, self.e, self.n))
    def decrypt(self, m):
        return (pow(m, self.d, self.n))






class Crypto:

    def __init__(self, key):
        self.key = key
    def codify(self, m):
        c = 1
        arr = [[0, 1, 2, 3, 4, 5, 6],
               [1, 4, 0, 2, 6, 3, 5],
               [2, 0, 3, 5, 1, 6, 4],
               [3, 2, 5, 6, 0, 4, 1],
               [4, 6, 1, 0, 5, 2, 3],
               [5, 3, 6, 4, 2, 1, 0],
               [6, 5, 4, 1, 3, 0, 2]]
        for i in range(self.key - 1):
            c = arr[m][c]
        return c
m=1
A = Crypto(3)
B = Crypto(4)
mA = A.codify(m)
mB = B.codify(m)

print(mA, mB)
print(A.codify(mB), B.codify(mA))




