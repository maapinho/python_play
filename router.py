from pprint import pprint
'''
Input a destination IP and a route table as a list
Find the longest prefix match

Testing:
    argparse (to have the data on the input)
    input validation
    read from files
'''

ROUTETABLE=[["0.0.0.0/0","interface1"],
    ["10.0.0.0/16","interface 2"],
    ["10.0.0.0/8","interface3"],
    ["1.0.3.22/32","interface3"]]
IP = "1.0.3.22"


def ip_to_decimal(ip_address):
    integer=map(int,ip_address.split('.'))
    integer=list(integer)
    integer[0]=integer[0]*2**24
    integer[1]=integer[1]*2**16
    integer[2]=integer[2]*2**8
    return sum(integer)


def ip_to_bin(ip_address):
    decimal=ip_to_decimal(ip_address)
    ip_bin=bin(decimal)
    return ip_bin

def mask_to_bin(mask_str):
    mask_dec=int(mask_str)
    mask_inverted=(2**(32-mask_dec))-1
    mask_dec=ip_to_decimal('255.255.255.255')^mask_inverted
    #print('decimal mask',mask_dec)
    mask_bin=bin(mask_dec)
    #print('binay mask',mask_bin)
    return mask_bin

# Process the route table to the desired format
# prefix, mask (decimal), target

def route_table_to_bin(routetable):
    route_table_bin=[]
    for route in routetable:
        ip_mask=route[0].split('/')
        #print(ip_mask)
        route_bin=[]
        route_bin.append(ip_to_bin(ip_mask[0]))
        route_bin.append(mask_to_bin(ip_mask[1]))
        route_bin.append(route[1])
        #print(route_bin)
        route_table_bin.append(route_bin)
    #print(route_table_bin)
    return(route_table_bin)
    
def route_table_decimal(routetable):
    route_table_dec=[]
    for route in routetable:
        ip_mask=route[0].split('/')
        route_dec=[]
        route_dec.append(ip_to_decimal(ip_mask[0]))
        route_dec.append(int(mask_to_bin(ip_mask[1]),2))
        route_dec.append(route[1])
        route_table_dec.append(route_dec)
        #print (route_table_dec)
    return route_table_dec

def match_route(ip_add_bin,route):
    prefix=route[0]
    mask=route[1]
    next_hop=route[2]
    ip_masked=ip_add_bin & mask
    match = ip_masked == prefix
    route.append(match)
    #print (route)
    return match

############ PENDING #################
# check if IP string is valid. Returns true of false
#def check_ip(ip_address):
#    ip_address.split('.')
#    
#########################################

### Main

route_table=ROUTETABLE
ip_address=IP

route_table_decimal=route_table_decimal(route_table)
ip_add_dec=ip_to_decimal(ip_address)

#pprint (route_table_decimal)


############ PENDING #################
for route in route_table_decimal:
    best=-1
    i=0
    if match_route(ip_add_dec,route):
        print("trueee")
    print(route)
#####################################

#for route_bin in route_table_bin:
    #match_route(ip_add_bin,route_bin)
print()

