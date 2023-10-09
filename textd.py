#!/usr/bin/python3
# -*- coding: ASCII -*-
# Text decoder v1.2
# Python 3 is recommended for intrepreting this. Python 2 is not supported.
from sys import stdin, stdout, argv

usage = r'''
usage: textd.py [options] [file]

options:
      -h, --help                 Show this help message and exit.

      -f, --file <file>          Specify the file to decode.

      -e, --encoding <encoding>  Specify the encoding of the <file>. Can only be specified when '-f' is used, otherwise a no-op. When a <file> is given while this is not specified, it is default to UTF-8.

      --no-codepoint             Decode and show the content of the <file>, but not the code points. This is a no-op unless '-f' is also used.

Unless '-f' or '--file' is specified, this program reads stdin (standard input).
New line characters will be shown as '\r', '\n', '\r\n', or '\v', depending on the character(s) read.
'''

invisibles = [' ', '\t', '\v', '\r', '\n', '\a', '\b', '\f']
visible = dict(zip(
    invisibles, [" ", "\\t", "\\v", "\\r", "\\n", "\\a", "\\b", "\\f"]
))

def show_text_with_code_points(s):
        n = len(s)
        k = n - 1
        i = 0
        while i < n:
            c = s[i]
            if c in ('\n', '\r'):
                if c == '\r':
                    if i < k:
                        if s[i+1] == '\n':
                            stdout.write('\r\n\033[35m("\\r\\n")\033[0m')
                            break
                        else:
                            pass
                stdout.write(c + '\033[35m("' + visible[c] + '")\033[0m')
            elif c in invisibles:
                stdout.write(c + '\033[36m("' + visible[c] + '")\033[0m')
            else:
                h = (hex(ord(c))[2:]).upper()
                stdout.write('\033[1;33m' + c + '\033[0m\033[36m(U+' + max(0, 4 - len(h)) * '0' + h + ')\033[0m')
            i += 1


def main():
    encoding = 'UTF-8'
    filename = ''
    no_codepoint = False
    argc = len(argv)
    k = argc - 1
    i = 1
    while i < argc:
        a = argv[i]
        if a in ('-h', '--help'):
            stdout.write(usage)
            exit()
        elif a in ('-f', '--file'):
            if i < k:
                filename = argv[i+1]
                i += 2
                continue
            else:
                print("[Error] A file name expected.")
                exit(1)
        elif a in ('-e', '--encoding'):
            if i < k:
                encoding = argv[i+1]
                i += 2
                continue
            else:
                print("[Error] %s used without specifing an encoding." % a)
                exit(1)
        elif a == '--no-codepoint':
            no_codepoint = True
        else:
            print("[Error] Unknown option: '%s'" % a)
            exit(1)
        i += 1
    try:
        if filename != '':
            with open(filename, 'rb') as file:
                if no_codepoint:
                    for line in file:
                        stdout.write(line.decode(encoding = encoding))
                else:
                    for line in file:
                        show_text_with_code_points(line.decode(encoding = encoding))
        else:
            for line in stdin:
                show_text_with_code_points(line)
    except KeyboardInterrupt:
        pass
    except UnicodeDecodeError:
        print("[Error] Failed to decode.")
        exit(2)
    finally:
        print('') #for newline


if __name__ == '__main__':
    main()
