import subprocess
import sys
import ansible_runner

def main():
    inventory_path = 'hosts.yml'
    inventory = ansible_runner.get_inventory(
        action='list',
        inventories=[inventory_path],
        response_format='json'
    )
    host_dict = {}
    for host in inventory[0]['_meta']['hostvars']:
        host_dict[host] = inventory[0]['_meta']['hostvars'][host]

    for group_name in inventory[0]:
        if (group_name == "_meta" or group_name == "all"):
            continue
        print(f'\nGroup: {group_name}')
        for host in inventory[0][group_name]["hosts"]:
            # print(host)
            print('Host: ', {host}, ' ----- ', 'IP info: ', host_dict[host]['ansible_host'])
    
    ping_hosts()

import subprocess

def ping_hosts():
    # Specify the inventory file
    inventory_file = "hosts.yml"

    # Run the ad-hoc command
    result = subprocess.run(['ansible', '-i', inventory_file, 'all', '-m', 'ping'], capture_output=True, text=True)

    # Print the result
    print(result.stdout)

if __name__ == "__main__":
    main()