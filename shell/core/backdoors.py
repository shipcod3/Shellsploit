from color import *

#Will be add command line params ..

def backdoorlist( require=False):
	if require != False:
		data = [
		"linux/x86/reverse_tcp",
		"linux/x64/reverse_tcp",
		"osx/x86/reverse_tcp",
		"osx/x64/reverse_tcp",
		"windows/x86/reverse_tcp",

		"php/reverse_tcp",
		"asp/reverse_tcp",
		"jsp/reverse_tcp",
		"war/reverse_tcp",

		"unix/python/reverse_tcp",
		"unix/perl/reverse_tcp",
		"unix/bash/reverse_tcp",
		"unix/ruby/reverse_tcp",
		]
		return data
	else:
		print (bcolors.GREEN+"""

Binaries
==========

  linux/x86/reverse_tcp
  linux/x64/reverse_tcp
  osx/x86/reverse_tcp
  windows/x86/reverse_tcp - [Passive]
  windows/x64/reverse_tcp - [Passive]

Web Payloads 
=============

  php/reverse_tcp - [Passive]
  asp/reverse_tcp - [Passive]
  jsp/reverse_tcp - [Passive]
  war/reverse_tcp - [Passive]

Scripting Payloads
===================

  unix/python/reverse_tcp
  unix/perl/reverse_tcp
  unix/bash/reverse_tcp
  unix/ruby/reverse_tcp


	""" + bcolors.ENDC)

