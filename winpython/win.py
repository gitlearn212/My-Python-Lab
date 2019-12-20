import wmi

wmi_obj = wmi.WMI()
wmi_sql = "select IPAddress, DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled = TRUE"
wmi_out = wmi_obj.query(wmi_sql)

for dev in wmi_out:
    print("IPv4Address:", dev.IPAddress[0],
          "DefaultIPGateway:", dev.DefaultIPGateway[0])
    #print("DefaultIPGateway:", dev.DefaultIPGateway[0])
