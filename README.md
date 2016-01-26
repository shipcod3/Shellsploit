#Shellsploit 
-------------

Shellsploit let's you generate customized shellcodes, backdoors, injectors for various operating system.
And let you obfuscation every byte via encoders.
	
#Install/Uninstall	
-------------------

If you want to use Shellsploit, you have to install [Capstone](http://www.capstone-engine.org/) first.

For the Capstone's installation:
    	
    root$ sudo pip install capstone

Also pyreadline for tab completion:
   	
   	root$ sudo pip install readline
    

Now you are ready to install(pip works on both windows/nix machines):

    root$ python setup.py -s/--setup install 
    root$ shellsploit

You dont want it anymore ? Uninstall it:

    root$ python setup.py -s/--setup uninstall 
 

#Usage
-----

    usage: shellsploit  [-l] [-p] [-o] [-n]
    						[--host] [--port]


    optional arguments:
	  	   -l, --list 			Show  list of backdoors,shellcodes,injectors
	  	   -p, --payload 		Set payload for usage
	  	   -n, -nc 				Declare netcat for usage
	  	   --host				The connect/listen address
	  	   --port				The connect/listen port	

  	Inline arguments:

  		Main Menu:
			help           		Help menu
			os					Command directly ur computer
			use 				Select Module For Use
			clear				Clear the menu
			show modules    	Show Modules of Current Database
			show backdoors    	Show Backdoors of Current Database
			show injectors		Show Injectors(Shellcode,dll,so etc..)

		Shellcode Menu:
			back				Exit Current Module
			set 				Set Value Of Options To Modules
			ip					Get IP address(Requires net connection)
			os					Command directly ur computer
			clear				Clear the menu
			disas				Disassembly the shellcode(Support : x86/x64)
			whatisthis      	Learn which kind of shellcode it is
			iteration			Encoder iteration time
			generate 			Generate shellcode 
			output 				Save option to shellcode(txt,py,c,cpp,exe)
			show encoders		List all obfucscation encoders
			show options		Show Current Options Of Selected Module

		Injector Menu:
			set 				Set Value Of Options To Modules
			help 				Help menu
			back				Exit Current Module
			os  				Command directly ur computer
			pids				Get PID list of computer
			getpid				Get specific PID on list(Ex. getpid Python)


#Bugs
------
	Please do not forget report bugs.You can submit issue,pull requests, or directly pm my email address.


#Screenshots
-------------

![alt tag](http://i.hizliresim.com/W18pL2.png)
![alt tag](http://i.hizliresim.com/pBMNO0.png)
