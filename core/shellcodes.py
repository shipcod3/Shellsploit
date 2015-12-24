#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

def shellcodelist():
	print """

Linux x86
===========

  linux86/egghunter		 
  linux86/binsh_spawn
  linux86/bindash_spawn
  linux86/readfile
  linux86/chmod
  linux86/reboot
  linux86/shutdown
  linux86/netcatbind
  linux86/mkdir
  linux86/rmdir
  linux86/killall
  linux86/ipv4forward
  linux86/Remoteportforward
  linux86/reverse_telnet
  linux86/add_user
  linux86/DeleteMBR
  linux86/tcp_bind
  linux86/reverse_tcp
  linux86/download&exec


Linux x64
===========

  linux64/egghunter
  linux64/binsh_spawn
  linux64/shutdown
  linux64/reboot
  linux64/mkdir
  linux64/add_map
  linux64/add_user
  linux64/read
  linux64/tcp_bind
  linux64/netcatbind
  linux64/reverse_tcp


Linux ARM
===========

  linux_arm/binsh_spawn
  linux_arm/chmod
  linux_arm/creat
  linux_arm/killall
  linux_arm/add_user
  linux_arm/reverse_tcp


Linux MIPS
===========
  
  linux_mips/add_user
  linux_mips/binsh_spawn
  linux_mips/reboot
  linux_mips/chmod
  linux_mips/tcp_bind
  linux_mips/reverse_tcp


Solaris x86
===========

  solarisx86/egghunter
  solarisx86/bindash_spawn
  solarisx86/binsh_spawn
  solarisx86/read
  solarisx86/reboot
  solarisx86/shutdown
  solarisx86/killall



Windows
===========

  windows/add_user
  windows/messagebox
  windows/download&execute
  windows/exec


OSX x86
===========

  osx86/tcp_bind
  osx86/binsh_spawn


OSX x64
===========

  osx64/binsh_spawn
  osx64/reverse_tcp
  osx64/tcp_bind


FreeBSD x86
============

  FreeBSDx86/binsh_spawn
  FreeBSDx86/reboot
  FreeBSDx86/killall
  FreeBSDx86/read
  FreeBSDx86/netcatreverse
  FreeBSDx86/reverse_tcp
  FreeBSDx86/reverse_tcp2(through /bin/sh)
  FreeBSDx86/exec
  FreeBSDx86/add_user


FreeBSD x64
============

  FreeBSDx64/binsh_spawn
  FreeBSDx64/tcp_bind
	"""