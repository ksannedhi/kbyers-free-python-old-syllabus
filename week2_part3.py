entries_list = """*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i
*  1.1.1.0/24     157.130.10.233        0 701 1299 15169 i
*  1.1.42.0/24    157.130.10.233        0 701 9505 17408 2.1465 i
*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i
"""
entries_list_lines = entries_list.splitlines()

print(f'{"ip_prefix":25}{"as_path"}')
for entry_line in entries_list_lines:
    entry_line_list = entry_line.split()
    print(f'{entry_line_list[1]:25}{entry_line_list[4:-1]}')
