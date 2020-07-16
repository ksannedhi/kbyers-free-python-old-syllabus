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
