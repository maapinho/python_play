import requests

# Set HTTP request timeout
TIMEOUT = 2

# Get the public IP address
url='http://telnetmyip.com'
r = requests.get(url,timeout=TIMEOUT)

public_ip=r.json()['ip']
print('\n\n')
print (url,':',public_ip)

# Get IP address from checkip.amazonaws.com
url='http://checkip.amazonaws.com'
r=requests.get(url,timeout=TIMEOUT)

public_ip=r.text

print (url,':',public_ip)


# Get IP address from checkip.noip.com
url='http://checkip.dyndns.org'
r=requests.get(url,timeout=TIMEOUT)
response=r.text.split(':')
response=response[1].split('<')
public_ip=response[0].strip()
print (url,':',public_ip)

