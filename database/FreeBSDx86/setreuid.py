"\x31\xc0\x50\x50\xb0\x17\xcd\x80\x31\xc0"


31 c0                   xor    %eax,%eax
50                      push   %eax
50                      push   %eax
b0 17                   mov    $0x17,%al
cd 80                   int    $0x80
31 c0                   xor    %eax,%eax