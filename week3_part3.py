'''The last exercise of the week is to create an IP address checker that checks the validity of an IP address. Here are the instructions:

[code lang=text]
IV. Create a script that checks the validity of an IP address. The IP address should be supplied on the command line.
A. Check that the IP address contains 4 octets.
B. The first octet must be between 1 – 223.
C. The first octet cannot be 127.
D. The IP address cannot be in the 169.254.X.X address space.
E. The last three octets must range between 0 – 255.

For output, print the IP and whether it is valid or not.
[/code]

The IP address will be supplied through the command line. 
Like we’ve done before we are going to check the number of arguments supplied and exit the script if the number of arguments is not two.
We need to import sys so that we can use sys.argv.'''

import sys

ip_addr = input("Enter and IP address: ")

valid_ip = True

octets = ip_addr.split(".")

if len(octets) != 4:
    valid_ip = False

for index, octet in enumerate(octets):
    try:
        octets[index] = int(octet)
    except ValueError:
        sys.exit()

first_octet, second_octet, thrid_octet, fourth_octet = octets

if first_octet < 0 or first_octet > 223:
    valid_ip = False

if first_octet == 127:
    valid_ip = False

if first_octet == 169 and second_octet == 255:
    valid_ip = False

for octet in (second_octet, thrid_octet, fourth_octet):
    if octet < 0 or octet > 255:
        valid_ip = False

if valid_ip == True:
    print(f"{ip_addr} IP address is valid.")
else:
    print(f"{ip_addr} IP address is not valid.")
