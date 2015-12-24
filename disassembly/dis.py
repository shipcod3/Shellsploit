#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

def disas(shellcode, bits=32):
    store = "\n"    
    if bits == 32:
        control = ["AL", "AX", "EAX"]
        from Syscalls import linux_32
        from distorm3 import Decode,Decode32Bits
        disasm = Decode(0x0, shellcode, Decode32Bits)
        for x in disasm:
            if "PUSH" in x[2]:
                if "0x" in x[2]:
                    try:
                        store += "\t0x%08x:\t %-20s %s ;%s\n" % (x[0],  x[3], x[2].lower(), x[2].split("0x")[1].decode("hex")[::-1])
                    except TypeError:
                        store += "\t0x%08x:\t %-20s %s ;%s\n" % (x[0],  x[3], x[2].lower(), x[2].split("0x")[1])
                    continue
           
            elif "MOV" in x[2]:
                if "0x" in x[2]:
                    if control in x:
                        continue
                    else:
                        try:
                            i386 =  linux_32.call( str(int(x[2].split("0x")[1].decode("hex")[::-1],16)))   
                            store += "\t0x%08x:\t %-20s %s ;%s\n" % (x[0],  x[3], x[2].lower(), i386)
                        except:
                            store += "\t0x%08x:\t %-20s %s\n" % (x[0],  x[3], x[2].lower())
                            continue
                        #continue        


            if x == disasm[-1]:
                store += "\t0x%08x:\t %-20s %s" % (x[0], x[3], x[2].lower())
            else:
                store += "\t0x%08x:\t %-20s %s\n" % (x[0], x[3], x[2].lower())

        

    elif bits == 64:
        control = ["AL", "AX", "EAX", "RAX"]
        from Syscalls import linux_64
        from distorm3 import Decode,Decode64Bits
        disasm = Decode(0x0, shellcode, Decode64Bits)
        for x in disasm:    
            store += "\t0x%08x:\t %-20s\t %s\n" % (x[0], x[3], x[2].lower())
       
    return store+"\n" 
    
