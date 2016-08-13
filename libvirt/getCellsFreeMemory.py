from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

nodeinfo = conn.getInfo()
memlist = conn.getCellsFreeMemory(0, nodeinfo[4])
cell = 0
for cellfreemem in memlist:
    print('Node '+str(cell)+': '+str(cellfreemem)+' bytes free memory')
    cell += 1

conn.close()
exit(0)
