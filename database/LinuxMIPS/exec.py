"\x66\x06\x06\x24\xff\xff\xd0\x04\xff\xff\x06\x28\xe0\xff\xbd\x27\x01\x10\xe4\x27\x1f\xf0\x84\x24\xe8\xff\xa4\xaf\xec\xff\xa0\xaf\xe8\xff\xa5\x27\xab\x0f\x02\x24\x0c\x01\x01\x01\x68\x65\x6c\x6c\x00\x00\x00\x00"


#hell



"""
00000000  6606              o16 push es
00000002  06                push es
00000003  24FF              and al,0xff
00000005  FFD0              call eax
00000007  04FF              add al,0xff
00000009  FF06              inc dword [esi]
0000000B  28E0              sub al,ah
0000000D  FF                db 0xff
0000000E  BD270110E4        mov ebp,0xe4100127
00000013  27                daa
00000014  1F                pop ds
00000015  F08424E8          lock test [eax+ebp*8],ah
00000019  FFA4AFECFFA0AF    jmp dword [edi+ebp*4-0x505f0014]
00000020  E8FFA527AB        call dword 0xab27a624
00000025  0F02240C          lar esp,[esp+ecx]
00000029  0101              add [ecx],eax
0000002B  016865            add [eax+0x65],ebp
0000002E  6C                insb
0000002F  6C                insb
00000030  0000              add [eax],al
00000032  0000              add [eax],al
"""

print "hell".encode("hex")[::-1]