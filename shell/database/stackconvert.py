#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


import sys
import re


def plaintext( string):
	db = re.findall("..?", string.encode("hex"))
	return "\\x"+"\\x".join(db)

def plaintextreverse( string):
	db = re.findall("..?", string.encode("hex"))
	return "\\x"+"\\x".join(db[::-1])



def PORT( port):
	from convertoffset import decimaltohex
	#I just want use my own libraries lol.
	db = []
	fixmesempai = re.findall('..?', decimaltohex(str(port)))
	for x in fixmesempai:
		if len(x) == 1:
			x = "0"+x
		db.append(x)
	return "\\x"+"\\x".join(db)



def IP( ip):
	from convertoffset import decimaltohex
	#0x101017f : 127.1.1.1
	ip = str(ip).split(".")
	db = []
	db2 = []
	for x in ip:
		db.append(decimaltohex( int(x)))
	for x in db: 
		if len(x) == 1:
			x = "0"+x
		db2.append(x)
	return "\\x"+"\\x".join(db2)


def rawSTR( string):
	db = []
	for x in string:
		db.append("\\x"+x.encode("hex"))
	return "".join(db)


def ARM( string):
	db = []
	if "/" in string:
		if len(string) % 4 == 0:
			string = string
		elif  len(string) % 4 == 1:
			string = filler( string, 4)
		elif len(string)	% 4 == 2:
			string = filler( string, 3)
		elif len(string) % 4 == 3:
			string = filler( string, 2)
		for x in range(0,len(string),4):
			db.append(ARMsplitter(string[x:x+4]))
		return "".join(db)
		
def ARMsplitter( hexdump, pushdword="None"):
	db = []
	if pushdword == "None":
		fixmesempai = re.findall('....?', hexdump)
		for x in fixmesempai[::-1]:
			first = str(x[::-1].encode("hex"))
			second = re.findall("..?", first)[::-1]
			db.append("\\x"+"\\x".join(second))
		return "".join(db)			




def stackconvertSTR( string):
	db = []
	if "/" in string:
		if len(string) % 4 == 0:
			string = string
		elif  len(string) % 4 == 1:
			string = filler( string, 4)
		elif len(string)	% 4 == 2:
			string = filler( string, 3)
		elif len(string) % 4 == 3:
			string = filler( string, 2)
		for x in range(0,len(string),4):
			db.append(splitter(string[x:x+4]))
		return "".join(db[::-1])
		#return "".join(db)
		
	#Linux_x86
	#68 PUSH DWORD
 	#6668 PUSH WORD
	if len(string) == 4:

		stack = "%s" % (string[::-1].encode('hex'))
		data = re.findall("..?", stack)
		return "\\x68\\x"+"\\x".join(data)


	elif len(string) % 4 == 0:
		for x in range(0,len(string),4):
			db.append(splitter(string[x:x+4]))
		return "".join(db) #Unix,Linux etc..
		#return "".join(db[::-1]) #Windows

	else:
		db = []
		dwordpart = string[0:(len(string)-len(string)%4)]
		wordpart = string[(len(string)-len(string)%4):len(string)]
		db.append(splitter( dwordpart))
		db.append(splitter(  wordpart, "WordTime"))
		return "".join(db)

def filler( string, number):
	string = [x for x in string]
	for x in range(0, len(string)):
		if string[x] == "/":
			string[x] = "/"*number
			break
	return "".join(string) 


def splitter( hexdump, pushdword="None"):
	db = []
	if pushdword == "None":
		fixmesempai = re.findall('....?', hexdump)
		for x in fixmesempai[::-1]:
			first = str(x[::-1].encode("hex"))
			second = re.findall("..?", first)[::-1]
			db.append("\\x"+"\\x".join(second))
		return "\\x68"+"".join(db)	
				
	else:		
		first = str(hexdump[::-1].encode("hex"))
		second = re.findall("..?", first)[::-1]
		for x in second:
			db.append("\\x"+x)
		return "\\x66\\x68"+"".join(db)

