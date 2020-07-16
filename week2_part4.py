cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
cisco_ios_list = cisco_ios.split(",")
get_ver = cisco_ios_list[2].split("Version ")

print(get_ver[1])
