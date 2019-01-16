
# The while loop chapter 6_1 Additional condition using Break, continue and else
# The Break will breal all the way out of the loop and skip the else 
# continue will shortcut the loop go back up the test without finishng the body of the loop 
#  Else isonly executed when the condition is False or no longer True and the loop exits normaly

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt:
        break
    if count ==3: continue
    pw = input(f'{count}) What is the secret word :')

else:
    auth = True   
print('Authorised' if auth else 'Authorisation Failed (!!! You Reached the max attempt !!!)')


