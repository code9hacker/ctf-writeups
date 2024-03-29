#!/usr/bin/env python3

from pwn import *

def get_process():
    if len(sys.argv) == 1:
        return context.binary.process()

    host, port = sys.argv[1].split(':')
    return remote(host, int(port))


def main():
    p = get_process()

    flag = ""                                           # Var to store the flag
    for i in range(250):                                # Try 0-250 indices
        p.recvuntil(b': ')                              # Recieve the line 'Which character (index) of the flag do you want? Enter an index: '
        p.sendline(bytes(str(i), 'utf-8'))              # Send the index in input. sendline() adds \n itself
        res = p.recvline()                              # Receive the line 'Character at Index 8: _'
        flag = flag + chr(res[-2])                      # Last character of response is \n. Second last is the required char.
                                                        # Converting to char since res is a byte array

    print("The flag is " + flag)    


if __name__ == '__main__':
    main()