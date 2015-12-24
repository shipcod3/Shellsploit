#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from random import randint

def banner( num1,num2,num3,num4):
	logo =[""" 
######                                                                  
#     # #    # ###### #      #       ####  #####  #       ####  # ##### 
#       #    # #      #      #      #      #    # #      #    # #   #   
 #####  ###### #####  #      #       ####  #    # #      #    # #   #   
	  # #    # #      #      #           # #####  #      #    # #   #   
#     # #    # #      #      #      #    # #      #      #    # #   #   
 #####  #    # ###### ###### ######  ####  #      ######  ####  #   # 
""",
"""
	____ __         ____           __      _ __ 
  / ___// /_  ___  / / /________  / /___  (_) /_
  \__ \/ __ \/ _ \/ / / ___/ __ \/ / __ \/ / __/
 ___/ / / / /  __/ / (__  ) /_/ / / /_/ / / /_  
/____/_/ /_/\___/_/_/____/ .___/_/\____/_/\__/  
						/_/  
""",
"""
						 *   
						***
					   ******              
 ____  _          _ _ ********  _       _ _   
/ ___|| |__   ___| | |*********| | ___ (_) |_ 
\___ \| '_ \ / _ \ | / __|****\| |/ _ \| | __|
 ___) | | | |  __/ | \__ \*|_)*| | (_) | | |_ 
|____/|_| |_|\___|_|_|___/**_*/|_|\___/|_|\__|
					*****|_|***
					   *******
						*****
						 ***
						  *   
"""
]

 #num1 Shellcode amount
 #num2 Os type amount
 #num3 Encoder amount
 #num4 injector amount


	dlogo = """
	   =[ Shellsploit v1 - \033[1;31m BETA                               \033[0m]
+ -- --=[ %s shellcode - \033[1;31m%s Different OS                       \033[0m]
+ -- --=[ %s encoders - \033[1;31m (Shellcodes/executable files)          \033[0m]
+ -- --=[ %s injector - \033[1;31m (PE,ELF,DLL,RAR,DEB etc...)            \033[0m]
+ -- --=[ Open Source : \033[1;31mhttps://github.com/b3mb4m/Shellsploit  \033[0m]
	"""	% (num1,num2,num3,num4)
	#

	return '\033[1;31m'+logo[randint(0, len(logo)-1)]+'\033[0m'+dlogo




