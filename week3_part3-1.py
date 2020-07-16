import sys

ip_addr = input("Provide an IP address to validate: ")

valid_ip = True

octets = ip_addr.split(".")
if len(octets) != 4:
    print(f'You have entered an invalid IP address {ip_addr}')
    sys.exit()

for index, octet in enumerate(octets):
    try:
        octets[index] = int(octet)
    except ValueError:
        print(f'You have entered an invalid IP address {ip_addr}')
        sys.exit()

first_octet, second_octet, third_octet, fourth_octet = octets

if first_octet < 1 or first_octet > 223 or first_octet == 127:
    valid_ip = False

if first_octet == 169 and second_octet == 254:
    valid_ip = False

for octet in (second_octet, third_octet, fourth_octet):
    if octet < 0 or octet > 255:
        valid_ip = False

if valid_ip:
    print(f'You have entered a valid IP address {ip_addr}')
else:
    print(f'You have entered an invalid IP address {ip_addr}')
