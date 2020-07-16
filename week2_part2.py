'''Create an IP address converter (dotted decimal to binary):

    A. Prompt a user for an IP address in dotted decimal format.
    B. Convert this IP address to binary and display the binary result on the screen (a binary string for each octet).

    Example output:
    first_octet    second_octet     third_octet    fourth_octet
    0b1010         0b1011000        0b1010         0b10011'''

ip_addr = input("Provide an IP address: ")
ip_addr_list = ip_addr.split(".")

print(f"{'first_octet':20}{'second_octet':20}{'third_octet':20}{'fourth_octet':20}")
print(f"{bin(int(ip_addr_list[0])):20}{bin(int(ip_addr_list[1])):20}{bin(int(ip_addr_list[2])):20}{bin(int(ip_addr_list[3])):20}")
print(f"{ip_addr_list[0]:20}{ip_addr_list[1]:20}{ip_addr_list[2]:20}{ip_addr_list[3]:20}")
