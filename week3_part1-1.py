'''Create an IP address converter (dotted decimal to binary).  This will be similar to what we did in class2 except:

    A. Make the IP address a command-line argument instead of prompting the user for it.
        ./binary_converter.py 10.88.17.23

    B. Simplify the script logic by using the flow-control statements that we learned in this class.

    C. Zero-pad the digits such that the binary output is always 8-binary digits long.  Strip off the leading '0b' characters.  For example,

        OLD:     0b1010
        NEW:    00001010

    D. Print to standard output using a dotted binary format.  For example,

        IP address          Binary
      10.88.17.23        00001010.01011000.00010001.00010111


    Note, you might need to use a 'while' loop and a 'break' statement for part C.
        while True:
            ...
            break       # on some condition (exit the while loop)

    Python will execute this loop again and again until the 'break' is encountered.'''

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
