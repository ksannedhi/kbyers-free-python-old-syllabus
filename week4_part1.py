'''The first exercise is the following:

I. Prompt a user to input an IP address.

Re-using some of the code from class3, exercise4–determine if the IP address is valid.

Continue prompting the user to re-input an IP address until a valid IP address is input.'''

while True:
    ip_addr = input("Provide an IP address: ")
    octets = ip_addr.split(".")
    valid_ip = True

    if len(octets) != 4:
        print(f'You have entered an invalid IP address {ip_addr}')
        continue

    for index, octet in enumerate(octets):
        try:
            octets[index] = int(octet)
        except ValueError:
            valid_ip = False #Doing a "continue" here is breaking the logic

    if not valid_ip:
        print(f"You have entered an invalid IP address {ip_addr}")
        continue

    first_octet, second_octet, third_octet, fourth_octet = octets

    if first_octet < 1 or first_octet == 127 or first_octet > 223:
        valid_ip = False

    if first_octet == 169 and second_octet == 254:
        valid_ip = False

    for octet in (second_octet, third_octet, fourth_octet):
        if octet < 0 or octet > 255:
            valid_ip = False

    if valid_ip:
        print(f'You have entered a valid IP address {ip_addr}')
        break
    else:
        print(f'You have entered an invalid IP address {ip_addr}')
        continue
