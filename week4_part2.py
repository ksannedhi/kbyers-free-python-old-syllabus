'''Parse the below 'show version' data and obtain the following items (vendor, model, os_version, uptime, and serial_number).
Try to make your string parsing generic i.e. it would work for other Cisco IOS devices.

The following are reasonable strings to look for:
'Cisco IOS Software' for vendor and os_version
'bytes of memory' for model
'Processor board ID' for serial_number
' uptime is ' for uptime

Store these variables (vendor, model, os_version, uptime, and serial_number) in a dictionary. Print the dictionary to standard output when done.
Note, "Cisco IOS Software…Version 15.0(1)M4…(fc1)" is one line.

>>>>> show version data <<<<<
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
————————————————-
Device# PID SN
————————————————-
*0 CISCO881-SEC-K9 FTX1000038X

License Information for 'c880-data'
License Level: advipservices Type: Permanent
Next reboot license Level: advipservices

Configuration register is 0x2102
>>>>> end show version data <<<<<'''

import re, pprint

sh_ver = """Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
————————————————-
Device# PID SN
————————————————-
*0 CISCO881-SEC-K9 FTX1000038X

License Information for 'c880-data'
License Level: advipservices Type: Permanent
Next reboot license Level: advipservices

Configuration register is 0x2102"""

vendor_and_version = re.search(r'(\S+) IOS .*, Version (\S+), RELEASE', sh_ver).groups()
model = re.search(r'^Cisco (\S+)\s\S+\sprocessor\s*', sh_ver, flags=re.M).group(1)
ser_num = re.search(r'Processor board ID (\S+)\s*', sh_ver, flags=re.M).group(1)
up_time = re.search(r'^twb-sf-881 uptime is ([\S+\s,]+)\s$', sh_ver, flags=re.M).group(1)

cisco_dict = {'model': model, 'os_version': vendor_and_version[1],
            'serial_number': ser_num, 'vendor': vendor_and_version[0], 'uptime': up_time}

pprint.pprint(cisco_dict)
