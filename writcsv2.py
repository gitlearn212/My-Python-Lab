import csv

sname = 'test1'
dstor = 'testtemplate'
temp = 'test1-template'
oscust = 'P Template Base'
clu = 'serv380'
ip = '10.0.0.10'
sub = '10.0.0.0'
gw = '10.0.0.1'
fdn = '10.0.0.2'
sdn = '10.0.0.3'
tp = 'thin'
vcpu = '2'
mem = '4'
netwrk = 'plan812815'


with open('names.csv', 'w', newline = '') as csvfile:
    fieldnames = ['Name', 'Template', 'Cluster', 'Datastore', 'Customization',  'vCPU', 'Memory', 'Network', 'DiskFormat',
                     'Ipaddress', 'Netmask', 'Gateway']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name':sname, 'Template':temp, 'Cluster':clu, 'Datastore':dstor, 'Customization':oscust, 'vCPU':vcpu, 'Memory':mem, 'Network':netwrk,'DiskFormat':tp,
                     'Ipaddress':ip, 'Netmask':sub, 'Gateway':gw, })

'''
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
'''
