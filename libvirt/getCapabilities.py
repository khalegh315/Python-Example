from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

caps = conn.getCapabilities()
print('Capabilities:\n'+caps)
conn.close()
exit(0)
