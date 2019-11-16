# Enter a file name with extention and display only the extention

filename = str(input('Enter a file name with extention: '))
f_extention = filename.split(".")
print(
    f'The extention of the file name {filename.upper()} is: {f_extention[-1]}')
