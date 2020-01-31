#! /usr/bin/python3

# Import libs
import urllib.request, ssl, sys

#Nagios return codes
OK       = 0
WARNING  = 1
CRITICAL = 2
UNKNOWN  = 3

#define api URL to use
#url = "https://puppet-jenkins.gre.ac.uk/job/Backup-Gitlab/lastBuild/api/json"
url = "https://puppet-jenkins.gre.ac.uk/job/Backup-Puppet-Master/lastBuild/api/json"

def main():
    returncode = checkjenkins()
    sys.exit(returncode)
    

def checkjenkins():
    
    sslcont = ssl.create_default_context()  # create new SSL context
    sslcont.check_hostname=False            # dont check hostname (needed if using default context)
    sslcont.verify_mode = ssl.CERT_NONE     # dont check cert

    # open URL with ssl context set.
    with urllib.request.urlopen(url, context=sslcont) as response:
        buildcheck = str(response.read())                  # cast to string and assign to var
        #print(buildcheck)
        response.close()                                    # close page - we're done with it now
        if buildcheck.find('\"result\":\"SUCCESS\"') != -1:
            #print("Success")
            return buildcheck
            #return buildcheck
            #return a
            return OK
        #elif buildcheck.find('\"result\":\"FAILURE\"') != -1:
        elif buildcheck.find('"executor":null')!= -1:
            print("Fail")
            return CRITICAL
        else:
            #print("Unknown")
            return UNKNOWN
        #print(buildcheck)

if __name__ == '__main__':
    main()
print(list[buildcheck])

#print(''' {"_class":"hudson.model.FreeStyleBuild","actions":[{"_class":"hudson.model.CauseAction","causes":[{"_class":"hudson.triggers.TimerTrigger$TimerTriggerCause","shortDescription":"Started by timer"}]},{},{}],"artifacts":[],"building":false,"description":null,"displayName":"#422","duration":671915,"estimatedDuration":577154,"executor":null,"fullDisplayName":"Backup-Puppet-Master #422","id":"422","keepLog":false,"number":422,"queueId":1795,"result":"SUCCESS","timestamp":1580322600911,"url":"http://puppet-jenkins.gre.ac.uk/job/Backup-Puppet-Master/422/","builtOn":"gm-pup-slave1","changeSet":{"_class":"hudson.scm.EmptyChangeLogSet","items":[],"kind":null},"culprits":[]} '''
    

