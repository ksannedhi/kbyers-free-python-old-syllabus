ip_addr = input("Provide an IP address: ")
ip_addr_list = ip_addr.split(".")

print(f"{'first_octet':20}{'second_octet':20}{'third_octet':20}{'fourth_octet':20}")
print(f"{bin(int(ip_addr_list[0])):20}{bin(int(ip_addr_list[1])):20}{bin(int(ip_addr_list[2])):20}{bin(int(ip_addr_list[3])):20}")
print(f"{ip_addr_list[0]:20}{ip_addr_list[1]:20}{ip_addr_list[2]:20}{ip_addr_list[3]:20}")
