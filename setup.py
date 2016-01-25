from optparse import OptionParser
from os import system
from os import path
from os import unlink
from sys import exit



if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option('-s', '--setup', action="store")
	options, args = parser.parse_args()

	if not options.setup:
		exit("\n\tUsage : setup.py -s/--setup install or uninstall ..\n")
	else:
		if options.setup == 'install':
			system('python easyinstall.py install --record shellsploit.ini')
		elif options.setup == 'uninstall': 
			if not path.isfile('shellsploit.ini'):
				exit('\n\tIf you want uninstall you must install it first.\n')
			else:
				files = open('shellsploit.ini', 'r').readlines()
				unlink('shellsploit.ini')
				print ('')
				for x in files:
					if path.isfile(x.strip()):
						print ('Remove : {0}').format(x.strip()) 
						unlink(x.strip())
				else:
					exit('\nUninstall complate ! \n')

		else:
			exit("\n\tUsage : setup.py -s/--setup install or uninstall ..\n")