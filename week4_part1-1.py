while True:
    ip_addr = input("Provide an IP address: ")
    valid_ip = True
    octets = ip_addr.split(".")
    if len(octets) != 4:
        print (f"Provided IP address doesn't have correct number of octets {ip_addr}")
        continue

    for index, octet in enumerate(octets):
        try:
            octets[index] = int(octet)
        except ValueError:
            valid_ip = False

    if not valid_ip:
        print(f'IP address provided is not correct {ip_addr}')
        continue

    first_octet, second_octet, third_octet, fourth_octet = octets

    if first_octet < 1 or first_octet > 223 or first_octet == 127:
        valid_ip = False

    if first_octet == 169 and second_octet == 254:
        valid_ip = False

    for octet in (second_octet, third_octet, fourth_octet):
        if octet < 0 or octet > 255:
            valid_ip = False

    if valid_ip:
        print(f"IP address provided is correct {ip_addr}")
        break
    else:
        print(f"IP address provided is not correct {ip_addr}")
        continue
