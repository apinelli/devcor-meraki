import requests
import json
import sys

base_url = "https://dashboard.meraki.com/api/v1/"
headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Cisco-Meraki-API-Key": "d77049c48fafc984f2f80714553800f9133ca084",
    }

def get_orgs():
    resp = requests.get(url = f"{base_url}/organizations", headers = headers)
    if resp.status_code == 200:
      return json.loads(resp.text)
    else:
        print(resp.status_code)
        sys.exit()

def get_networks(orgId):
    resp = requests.get(url = f"{base_url}/organizations/{orgId}/networks", headers = headers)
    if resp.status_code == 200:
      return json.loads(resp.text)
    else:
        print(resp.status_code)
        sys.exit()

def get_devices(networkId):
    resp = requests.get(url = f"{base_url}/organizations/{orgId}/networks/{networkId}/devices", headers = headers)
    if resp.status_code == 200:
      return json.loads(resp.text)
    else:
        print(resp.status_code)
        sys.exit()

def get_ssid(networkId):
    resp = requests.get(url = f"{base_url}/networks/{networkId}/wireless/ssids", headers = headers)
    if resp.status_code == 200:
      return json.loads(resp.text)
    else:
        print(resp.status_code)
        sys.exit()

# Listing all organizations:
print('List of all organizations:')
for o in get_orgs():
    print('{0:35} {1:30}'.format(o['name'], o['id']))

print('\n')
orgId = input("Do you want to know the networks for which organization ID? :")
print('\n')

# Listing all networks:
print('List of all networks in {} organization :'.format(orgId))
for n in get_networks(orgId):
    print('{0:35} {1:30}'.format(n['name'], n['id']))

print('\n')
networkId = input("Do you want to know the devices for which network ID? :")
print('\n')

# Listing all devices:
print('\n')
print('List of all devices on network {} :'.format(networkId))
print('\n')
for key, value in get_devices(networkId)[0].items():
    if key == 'name' or key == 'mac':
      print('{0:35} {1:30}'.format(key, value))

# Listing all ssids:
print('\n')
print('List of all ssids on network {} :'.format(networkId))
print('\n')
print('{0:20} {1:40} {2:20}'.format('number', 'name', 'enabled'))
for s in get_ssid(networkId):
    print('{0:5} {1:40} {2:20}'.format(s['number'], s['name'], s['enabled']))
