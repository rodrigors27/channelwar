#!/usr/bin/python3.5

from pysnmp.hlapi import *

varCommunity = "C1sco"
varServer = "192.168.16.104"
varPort = 161

g = getCmd(SnmpEngine(), CommunityData(varCommunity, mpModel=1), UdpTransportTarget((varServer, varPort)), ContextData(), ObjectType(ObjectIdentity('1.2.840.10036.1.1.1.1.1')))

# this is what you get from SNMP agent
errorIndication, errorStatus, errorIndex, varBinds = next(g)
#print(varBinds)

#if not error_indication and not error_status:
# each element in this list matches a sequence of `ObjectType`
# in your request.
# In the code above you requested just a single `ObjectType`,
# thus we are taking just the first element from response
#    oid, value = var_binds[1]
#    print(oid, '=', value)
    #channel24 = value
    #print(channel24)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        #print(' = '.join([x.prettyPrint() for x in varBind]))
        #print(' = '.join([x.prettyPrint() for x in varBind]))
        parta,partb = varBind
        full = str(partb.prettyPrint())
        onlymac = full.strip('0x')
        #print(type(onlymac))
        print(onlymac)


h = getCmd(SnmpEngine(), CommunityData(varCommunity, mpModel=1), UdpTransportTarget((varServer, varPort)), ContextData(), ObjectType(ObjectIdentity('1.2.840.10036.1.1.1.1.2')))

# this is what you get from SNMP agent
errorIndication, errorStatus, errorIndex, varBinds = next(h)
#print(varBinds.ObjectName)

#if not error_indication and not error_status:
# each element in this list matches a sequence of `ObjectType`
# in your request.
# In the code above you requested just a single `ObjectType`,
# thus we are taking just the first element from response
#    oid, value = var_binds[1]
#    print(oid, '=', value)
    #channel5 = value
    #print(channel5)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        #print(' = '.join([x.prettyPrint() for x in varBind]))
        parta,partb = varBind
        full = str(partb.prettyPrint())
        onlymac = full.strip('0x')
        #print(type(onlymac))
        print(onlymac)


