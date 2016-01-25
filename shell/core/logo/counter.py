#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

import os
from sys import platform
 
class B3mB4mLogo(object):
	def __init__(self):
		self.db = ["database", "OS", "encoders", "inject"]
		self.ret = []
		#self.magic = os.sep.join((os.getcwd()).split(os.sep)[:len((os.getcwd()).split(os.sep))-1])
		self.magic = os.getcwd()+os.sep+"shell"
		if 'win' not in platform.lower():
			self.magic = '/usr/share/shellsploit/'+os.sep

	def calculate(self, select, files=True):
		if files == True:
			self.cout = 0
			for root, dirs, files in os.walk(self.magic+os.sep+select, topdown=True):
				for x in files:
					if ".pyc" not in x and "init" not in x:
						if select == "inject":
							if "inject" in x:
								self.cout += 1
						else:
							self.cout += 1
			return self.cout
		else:
			self.cout = 0
			for root, dirs, files in os.walk(self.magic+os.sep+select, topdown=True):
				for x in dirs:
					self.cout += 1
			return self.cout

	def start(self):
		for x in self.db:
			if x != "OS":
				self.ret.append( self.calculate( x, True))
			else:
				self.ret.append( self.calculate( "database", False))
		return self.ret


