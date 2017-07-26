import optparse
parser=optparse.OptionParser('usage%prog-H'+\
	'<targethost>-p<targetport>')
	)
parser.add_option('-H',dest='tgtHost',type='string',\
	help='specify target host')
parser.add_option('-p',dest='tgtPort', type='int',\
	help='specify target port')
(options, args)=parser.parse_args()
tgtHost=options.tgtHost
tgtPort=options.tgtPort
if(tgtHost==None)|(tgtPort==None):
	print parser.usage
	exit(0)


import optparse
from socket import*
def connScan(tgtHost,tgtPort):
	try:
		connSkt=socket(AF_INET,SOCKET_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		print '[+]%d/tcp open'%tgtPort
		connSkt.close()
	except:
		print'[-]%d/tpc closed'%tgtPort
		def portScan(tgtHost,tgtPorts):
			try:
				tgtIP=gethostbyname(tgtHost)
			except:
				print"[-]Cannot resolve '%s':Unknown host"%tgtHost
				return
				try:
					tgtName=gethostbyaddr(tgtIP)
					print'\n[+]Scan Results for:'+tgtName[0]
				except:
					print '\n[+]Scan Results for:'+tgtIPsetdefaulttimeout(1)
					for tgtPort in tgtPorts:
						print 'Scanning port'+tgtPortconnScan(tgtHost, int(tgtPort))

import optparse
import socket
from socket import *
def connScan(tgtHost,tgtPort):
	try:
		connSkt=socket(AF_INET,SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		connSkt.send('ViolentPython\r\n')
		results=connSkt.recv(100)
		print'[+]%d/tcp open'%tgtPort
		print'[+]'+str(results)
		connSky.close()
		except:
			print'[-]