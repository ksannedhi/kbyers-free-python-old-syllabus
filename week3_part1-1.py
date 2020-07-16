import sys
ip_addr = sys.argv[1]
ip_addr_list = ip_addr.split(".")
updated_ip_addr_list = []
for octet in ip_addr_list:
    octet_in_bin = bin(int(octet))
    octet_in_bin_lstrip = octet_in_bin.lstrip("0b")
    octet_in_bin_rjust = octet_in_bin_lstrip.rjust(8, "0")
    updated_ip_addr_list.append(octet_in_bin_rjust)

print(f"{'IP address':20}{'Binary'}")
print(f'{ip_addr:20}{".".join(updated_ip_addr_list)}')
