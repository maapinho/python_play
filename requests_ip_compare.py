## >>> import requests
## >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
## >>> r.status_code
## 200
## >>> r.headers['content-type']
## 'application/json; charset=utf8'
## >>> r.encoding
## 'utf-8'
## >>> r.text
## u'{"type":"User"...'
## >>> r.json()
## {u'disk_usage': 368627, u'private_gists': 484, ...}


import requests

# Set HTTP request timeout
TIMEOUT = 2

# Get the public IP address
r = requests.get('http://telnetmyip.com',timeout=TIMEOUT)

public_ip=r.json()['ip']
print('\n\n')
print ('telnetmyip.com: ',public_ip)

# Get IP address from checkip.amazonaws.com
r=requests.get('http://checkip.amazonaws.com',timeout=TIMEOUT)

public_ip=r.text

print ('checkip.amazonaws.com: ',public_ip)


# Get IP address from checkip.noip.com

r=requests.get('http://checkip.dyndns.org',timeout=TIMEOUT)
response=r.text.split(':')
response=response[1].split('<')
public_ip=response[0].strip()
print ('http://checkip.dyndns.org: ',public_ip)

