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

print ('status code:',r.status_code)


public_ip=r.json()['ip']
print ('your IP address is: ',public_ip)

# Get RDAP infor from the IP address
rdap=requests.get('https://rdap.afrinic.net/rdap/ip/'+public_ip,timeout=TIMEOUT)

country=rdap.json()['country']

print('This IP address is registered in: '+country)
