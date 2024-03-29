#!/usr/bin/env python3

from pwn import *

def get_process():
    if len(sys.argv) == 1:
        return context.binary.process()

    host, port = sys.argv[1].split(':') 
    return remote(host, int(port))


def main():
    p = get_process()

    res = p.recvuntil(b'Are you ready? (y/n) ')
    print(res)
    p.sendline(b'y')
    res = p.recvline()
    print(res)
    res = p.recvline()
    print(res)

    while(True):
        if b'What do you do?' in res:
            res = res[16:]
        res = res.split(b', ')
        print(res)
        req = ""
        cnt = 0
        for r in res:
            if r == b'GORGE' or r == b'GORGE\n':
                req += 'STOP'
            elif r == b'PHREAK' or r == b'PHREAK\n':
                req += 'DROP'
            elif r == b'FIRE' or r == b'FIRE\n':
                req += 'ROLL'
            cnt += 1
            if cnt < len(res):
                req += '-'
        
        print(req)
        p.sendline(bytes(req, "utf-8"))
        res = p.recvline()
        print(res)
        if b'Unfortunate' in res:
            exit(-1)

    


if __name__ == '__main__':
    main()