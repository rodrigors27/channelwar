#!/usr/bin/python3.5

from pysnmp.hlapi import *

varCommunity = "C1sco"
varServer = "192.168.15.107"
varPort = 161

g = getCmd(SnmpEngine(), CommunityData(varCommunity, mpModel=1), UdpTransportTarget((varServer, varPort)), ContextData(), ObjectType(ObjectIdentity('1.2.840.10036.4.11.1.1.1')))

# this is what you get from SNMP agent
error_indication, error_status, error_index, var_binds = next(g)
#print(var_binds)

if not error_indication and not error_status:
# each element in this list matches a sequence of `ObjectType`
# in your request.
# In the code above you requested just a single `ObjectType`,
# thus we are taking just the first element from response
    oid, value = var_binds[0]
    #print(oid, '=', value)
    channel24 = value
    print(channel24)



h = getCmd(SnmpEngine(), CommunityData(varCommunity, mpModel=1), UdpTransportTarget((varServer, varPort)), ContextData(), ObjectType(ObjectIdentity('1.2.840.10036.4.11.1.1.2')))

# this is what you get from SNMP agent
error_indication, error_status, error_index, var_binds = next(h)
#print(var_binds)

if not error_indication and not error_status:
# each element in this list matches a sequence of `ObjectType`
# in your request.
# In the code above you requested just a single `ObjectType`,
# thus we are taking just the first element from response
    oid, value = var_binds[0]
    #print(oid, '=', value)
    channel5 = value
    print(channel5)




