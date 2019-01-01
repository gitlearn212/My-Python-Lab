import os, sys, difflib
os.chdir('c:/num')
#print os.getcwd()
file1=('num1.txt')
file2=('num2.txt')
file3=('num3.txt')
first=file(file1).readlines()
secon=file(file2).readlines()
for n in range(len(first)):
    lenf=len(first[n].strip())
    diff=secon[n][lenf: ].strip()
    print diff

