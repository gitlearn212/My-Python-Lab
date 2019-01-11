import string
import random
# upper = input ("Uppercase (y/n)" : )
# lower = input ("Lowercase (y/n)" : )
# number = input("Include Numbers (y/n)" : )
# specialchars = = input ("Include Special Charactors (y/n)" : )

def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits #+ string.punctuation
    
    return '' .join(random.choice(chars) for x in range(12))
for i in range(5):
    print(randompassword())
ent = input("Press enter.....")
