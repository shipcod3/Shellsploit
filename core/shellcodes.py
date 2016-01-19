#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#
from color import *

def shellcodelist():
	print bcolors.GREEN+"""

Linux x86
===========

  linux86/exec
  linux86/binsh_spawn
  linux86/read
  linux86/chmod
  linux86/tcp_bind
  linux86/reverse_tcp


Linux x64
===========

  linux64/binsh_spawn
  linux64/read
  linux64/tcp_bind
  linux64/reverse_tcp


Linux x86/x64 [Works on both]
===========

  linux/binsh_spawn
  linux/read
  linux/tcp_bind
  linux/reverse_tcp


Linux ARM
===========

  linux_arm/exec
  linux_arm/binsh_spawn
  linux_arm/chmod
  linux_arm/reverse_tcp


Linux MIPS
===========

  linux_mips/binsh_spawn
  linux_mips/chmod
  linux_mips/tcp_bind
  


Solaris x86
===========

  solarisx86/binsh_spawn
  solarisx86/read
  solarisx86/reverse_tcp
  solarisx86/tcp_bind

Windows
===========

  windows/exec
  windows/messagebox
  windows/download&execute
  


OSX x86
===========

  osx86/tcp_bind
  osx86/binsh_spawn
  osx86/reverse_tcp


OSX x64
===========

  osx64/binsh_spawn
  osx64/reverse_tcp
  osx64/tcp_bind


FreeBSD x86
============

  FreeBSDx86/binsh_spawn
  FreeBSDx86/read
  FreeBSDx86/tcp_bind
  FreeBSDx86/reverse_tcp
  FreeBSDx86/reverse_tcp2 (through /bin/sh)
  FreeBSDx86/exec

  
FreeBSD x64
============
  
  FreeBSDx64/exec
  FreeBSDx64/binsh_spawn
  FreeBSDx64/tcp_bind
  FreeBSDx64/reverse_tcp
	""" + bcolors.ENDC