#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

def encoderlist():
	print ("""
Encoders
========

\tName\t\t\tRank\t\tDescription
\t----\t\t\t----\t\t-----------
\tx86/xor\t\t\tnormal\t\tXOR Encoder
\tx86/xor_b3m [BETA]\texcellent\tPolymorphic XOR Additive Feedback Encoder
		
  """)


#\tx64/xor\t\t\tnormal\t\tXOR Encoder
#\tx86/add_sub\t\tmanual\t\tAdd/Sub Encoder
#\tx86/alpha_mixed\t\tlow\t\tAlpha2 Alphanumeric Mixedcase Encoder
#\tx86/alpha_upper\t\tlow\t\tAlpha2 Alphanumeric Uppercase Encoder
#\tx86/countdown\t\tnormal\t\tSingle-byte XOR Countdown Encoder
#\tx86/nonalpha\t\tlow\t\tNon-Alpha Encoder
#\tx86/nonupper\t\tlow\t\tNon-Upper Encoder

def injectorlist():
	print ("""
\tArchitecture\t\t\tVersion
\t============\t\t\t=======
\t[+] injectors/Linux\t\t(x86/x64)
\t[+] injectors/Windows_x86\t(x86)
	""")

def OSlist():
	print ("""
	Operating System	Architecture
	================	============
	Linux 		   		x86
	Windows 			x86
	FreeBSD 			x86
	OpenBSD 			x86
	Solaris 			x86
	Linux 				PowerPC
	OpenBSD 			PowerPC
	Linux 				Sparc
	FreeBSD 			Sparc
	OpenBSD 			Sparc
	Solaris 			Sparc
	Linux 				ARM
	FreeBSD 			ARM
	OpenBSD 			ARM

""")

def encoders():
  	list = [
  	"x64/xor",
	"x86/xor",
	"x86/add_sub",
	"x86/alpha_mixed",
	"x86/alpha_upper",
	"x86/countdown",
	"x86/nonalpha",
	"x86/nonupper",
	"x86/xor_b3m",
  	]
  	return list