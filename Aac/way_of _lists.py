a = {} # dic
a[1] = 1 # value 1 and key is 1 
a["1"] = 2 # value "1" and key is 2 
a[1] = a[1]+2 # modifying the key of value 1 (value is 1 and key is 2 
a["a"] = a["1"]+3# a["a"] is anothe key  =a["1"]+3 we are using the xepression

print(a)
count = 0
for i in a:
    print("print's the values of the key: ",i,":",a[i])
    count+=a[i]
print(count)
