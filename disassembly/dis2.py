from capstone import *

def disasNOTintel(shellcode, choice,  bits=32):
    ARCH = {
        'arm': CS_ARCH_ARM,
        'arm64': CS_ARCH_ARM64,
        'mips': CS_ARCH_MIPS,
        'ppc': CS_ARCH_PPC,
        'x86': CS_ARCH_X86,
        'xcore': CS_ARCH_XCORE
    }

    MODE = {
        '16': CS_MODE_16,
        '32': CS_MODE_32,
        '64': CS_MODE_64,
        'arm': CS_MODE_ARM,
        'be': CS_MODE_BIG_ENDIAN,
        'le': CS_MODE_LITTLE_ENDIAN,
        'micro': CS_MODE_MICRO,
        'thumb': CS_MODE_THUMB
    }

    if choice == "arm":
        if bits == 64:
            md = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
        else:
            md = Cs(CS_ARCH_ARM32, CS_MODE_ARM)
    else:
        #Must be test ..
        if bits == 64:
            md = Cs(CS_ARCH_MIPS, CS_MODE_64)
        else:
            md = Cs(CS_ARCH_MIPS, CS_MODE_32)


    list = []
    for i in md.disasm(shellcode, 0x10000000):
        if len(i.mnemonic) <= 3:
            db = "\t0x%x: %s\t\t%s" % (i.address, i.mnemonic, i.op_str)
            #print("\t0x%x:\t%s\t\t%s" % (i.address, i.mnemonic, i.op_str))
        else:
            db = "\t0x%x: %s\t%s" % (i.address, i.mnemonic, i.op_str)
            #print("\t0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
        list.append(db)
    return "\n".join(list)
