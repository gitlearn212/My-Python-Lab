# names = ['John', 'Paul', 'george', 'Ringo', 'suhu', 'jay', 'kav']
names = ['John', 'Paul', 'george', 'Ringo', 'suhu', 'jay', 'kav']
names_to_remove = []
for name in names:
    # if name in ['John', 'Paul']:
    if name not in ['John', 'Paul']:
        names_to_remove.append(name)
for name in names_to_remove:
    names.remove(name)
print(names)
