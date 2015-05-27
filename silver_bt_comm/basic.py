MAC = '78:F7:BE:1D:9B:1D'
MAC1 = 'D0:B3:3F:77:CC:0F'

from bluetooth import *
print "performing inquiry..."
nearby_devices = discover_devices(lookup_names = True)
print "found %d devices" % len(nearby_devices)
for name, addr in nearby_devices:
     print " %s - %s" % (addr, name)
