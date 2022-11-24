from ncclient import manager
import re

nexus = manager.connect(
    host = 'sandbox-nxos-1.cisco.com',
	username='admin',
	password='Admin_1234!',
	allow_agent=False,
	look_for_keys=False,
	hostkey_verify=False,
	unknown_host_cb=True)

for capability in nexus.server_capabilities:
    print (capability)	