network_addr = input("Enter a network address: ")
network_addr_list = network_addr.split(".")
network_addr_list = network_addr_list[0:4]
network_addr_list[3] = str(0)
network_addr_updated = ".".join(network_addr_list)

print("{:20} {:20} {:20}".format("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX"))
print(f'{"NETWORK_NUMBER":20} {"FIRST_OCTET_BINARY":20} {"FIRST_OCTET_HEX":20}')
print(f'{network_addr_updated:20} {bin(int(network_addr_list[0])):20} {hex(int(network_addr_list[0])):20}')
