def validIPAddresses(string):
    ip_addresses = []

    for i in range(1, min(len(string), 4)):
        current_ip_addr_parts = ['','','','']

        current_ip_addr_parts[0] = string[:i]

        if not is_valid_part(current_ip_addr_parts[0]):
            continue

        for j in range(i+1, i+min(len(string)-i, 4)):
            current_ip_addr_parts[1] = string[i:j]
            if not is_valid_part(current_ip_addr_parts[1]):
                continue
            for k in range(j+1, j+min(len(string)-j, 4)):
                current_ip_addr_parts[2] = string[j:k]
                current_ip_addr_parts[3] = string[k:]

                if is_valid_part(current_ip_addr_parts[2]) and is_valid_part(current_ip_addr_parts[3]):
                    ip_addresses.append('.'.join(current_ip_addr_parts))
    # Write your code here.
    return ip_addresses


def is_valid_part(string):
    return len(string) == len(str(int(string))) and int(string) <= 255