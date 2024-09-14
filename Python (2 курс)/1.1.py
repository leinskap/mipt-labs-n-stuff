#Копытова Виктория 5
print("Задача 1")
dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
print(dna.count("A"))
print(dna.count("G"))
print(dna.count("C"))
print(dna.count("T"))
print("\n")
print("Задача 2")
dna = 'GATGGAACTTGACTACGTAAATT'
lis = list(dna)
for i in range(len(lis)):
    if lis[i]=="T":
        lis[i] = "U"
res = ""
for i in range(len(lis)):
    res+=lis[i]
print(res)
print("\n")
print("Задача 3")
dna = 'AAAACCCGGT'
lis = list(dna)
strand=""
for i in range(len(lis)):
    if lis[i]=="A":
        strand+="T"
    elif lis[i]=="T":
        strand+="A"
    elif lis[i]=="G":
        strand+="C"
    elif lis[i]=="C":
        strand+="G"
res = ""
for i in range(len(strand)):
    res+=strand[i]
print(res[::-1])
print("\n")
print("Задача 4")
dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
lis = list(dna)
lenght = len(lis)
C = dna.count("C")
G = dna.count("G")
print(round((C+G)/lenght * 100, 6))
print("\n")
print("Задача 5")
count = 0
dna1 = list('GAGCCTACTAACGGGAT')
dna2 = list('CATCGTAATGACGGCCT')
for i in range(len(dna1)):
    if dna1[i]!=dna2[i]:
        count+=1
print(count)

print("\n")
print("Задача 6")
rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
arr = [rna[i:i+3] for i in range(0, len(rna), 3)]
table = "UUU F      CUU L      AUU I      GUU V UUC F      CUC L      AUC I      GUC V UUA L      CUA L      AUA I      GUA V UUG L      CUG L      AUG M      GUG V UCU S      CCU P      ACU T      GCU A UCC S      CCC P      ACC T      GCC A UCA S      CCA P      ACA T      GCA A UCG S      CCG P      ACG T      GCG A UAU Y      CAU H      AAU N      GAU D UAC Y      CAC H      AAC N      GAC D UAA Stop CAA Q      AAA K      GAA E UAG Stop CAG Q      AAG K      GAG E UGU C      CGU R      AGU S      GGU G UGC C      CGC R      AGC S      GGC G UGA Stop CGA R      AGA R      GGA G UGG W      CGG R      AGG R      GGG G"
table = table.split()
triplets = [table[i] for i in range(0, len(table), 2)]
letters = [table[i] for i in range(1, len(table), 2)]
for i in range(len(arr)):
    x = triplets.index(arr[i])
    if letters[x] == "Stop":
        arr[i] = " "
    else: arr[i] = letters[x]
res = ""
for i in range(len(arr)):
    res+=arr[i]
print(res)

print("\n")
print("Задача 7")
dna1 = 'GATATATGCATATACTT'
dna2 = 'ATAT'
n = len(dna2)
res = []
for i in range(len(dna1)):
    dna_cut = dna1[i:]
    if dna_cut[:n] == dna2:
        res.append(i+1)
for i in res:
    print(i, end=" ")
print("\n")
print("Задача 8")
letters = ["A", "T", "C", "G"]
dnas = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']
rows = len(dnas[0])
for i in range(rows):
    s=""
    for j in range(len(dnas)):
        s+=dnas[j][i]
    number = [s.count("A"), s.count("T"), s.count("C"), s.count("G")]
    x = number.index(max(number))
    print(letters[x], end="")
print("\n")


from time import time as t
N = 10**4
r = list(range(N))
l = []
t1 = t()
for i in r:
    l.append(i)
print(t()-t1)
t1 = t()
for i in r:
    -1 in l
print(t()-t1)
d = {}
t1 = t()
for i in r:
    d[i] = i

print(t()-t1)
t1 = t()
for i in r:
    -1 in d
print(t()-t1)

N = int(input())
M = int(input())
K = int(input())

