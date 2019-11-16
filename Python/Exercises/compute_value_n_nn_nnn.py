# write a program that accepts an integer and
# computes the value to n+nn+nnn _n =5 ans is 615
n = (int(input('Entaer an integer value: ')))
n1 = int("%s" % (n))
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
print(n1 + n2 + n3)
