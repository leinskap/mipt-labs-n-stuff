import numpy as np
def f1(digit):
    # your code here #1 max digit
    digit = str(digit)
    return int(max(digit))

if __name__ == "__main__":
    assert f1(1) == 1
    assert f1(51) == 5
    assert f1(632) == 6
    assert f1(11) == 1
    assert f1(10000) == 1
    print("1) Done!")

def f2(text):
    # your code here #2 first word
    text = text.split()
    return text[0]

if __name__ == "__main__":
    assert f2("Hello world") == "Hello"
    assert f2("a word") == "a"
    assert f2("online compiler and debugger") == "online"
    assert f2("Hi") == "Hi"
    print("2) Done!")


def f3(text, start, end):
    # your code here #3 between start and end
    text = text.split(start)
    return text[1][:-1]

if __name__ == "__main__":
    assert f3("What is >orange<", ">", "<") == "orange"
    assert f3("What is [orange]", "[", "]") == "orange"
    assert f3("What is ><", ">", "<") == ""
    assert f3("[an orange]", "[", "]") == "an orange"
    print("3) Done!")


def f4(word, first, second):
    if word.find(first+second) >=0:
        return True
    return False

if __name__ == "__main__":
    assert f4("world", "w", "o") == True
    assert f4("world", "w", "r") == False
    assert f4("world", "l", "o") == False
    assert f4("orange", "n", "g") == True
    assert f4("", "n", "g") == False
    assert f4("list", "l", "l") == False
    assert f4("world", "d", "w") == False
    print("4) Done!")

def f5(n):
    # your code here #5 end zeros
    i=0
    n = str(n)
    n=n[::-1]
    for x in n:
        if int(x)!=0:
            i = n.index(x)
            break
    return n.count('0', 0, i+1)

if __name__ == "__main__":
    assert f5(0) == 1
    assert f5(1) == 0
    assert f5(10) == 1
    assert f5(101) == 0
    assert f5(245) == 0
    assert f5(100100) == 2
    print("5) Done!")

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a=[[0]*4, [0]*4, [0]*4, [0]*4]
a=list(a)
c=0

for i in range(4):
    for j in range(4):
        a[j][i] = int(n[c])
        c+=1
print(a)

s = [
[10, 14, 13, 5, 9, 7, 0, 6, 15, 4, 11, 8, 2, 12, 1, 3],
[0, 2, 11, 6, 8, 10, 5, 13, 15, 9, 12, 7, 1, 3, 14, 4],
[9, 3, 13, 5, 7, 11, 8, 6, 2, 4, 14, 15, 12, 0, 1, 10],
[7, 8, 5, 15, 11, 3, 9, 6, 2, 12, 1, 4, 14, 0, 10, 13],
[13, 12, 5, 15, 4, 0, 10, 9, 7, 8, 3, 2, 11, 6, 1, 14]]

b=[[0]*4, [0]*4, [0]*4, [0]*4]

for i in range(4):
    for j in range(4):
        b[i][j] = s[0][a[i][j]]
print(b)

for i in range(4):
    for j in range(i):
        v=b[i].pop(0)
        b[i].append(v)
print(b)
x = [10, 7, 11, 3]
print(x[0]<<1    ^    x[1]<<1 ^ x[1] ^ x[2] ^ x[3])


d = [[0]*4, [0]*4, [0]*4, [0]*4]
c=0
for i in range(4):
    x = [0] * 4
    for j in range(4):
        x[j] = b[j][i]
    d[c][i] = x[0]<<1    ^    x[1]<<1 ^ x[1] ^ x[2] ^ x[3]
c+=1
for i in range(4):
    x = [0] * 4
    for j in range(4):
        x[j] = b[j][i]
    d[c][i] = x[0] ^(x[1]<<1) ^ x[2]<<1 ^ x[2] ^ x[3]
c+=1
for i in range(4):
    x = [0] * 4
    for j in range(4):
        x[j] = b[j][i]
    d[c][i] = x[0] ^ x[1] ^ (x[2]<<1) ^ (x[3]<<1 ^ x[3])
c+=1
for i in range(4):
    x = [0] * 4
    for j in range(4):
        x[j] = b[j][i]
    d[c][i] = (x[0]<<1 ^ x[0]) ^ x[1] ^ x[2] ^ (x[3]<<1)
print(d)



