import argparse
import sys

def main():
    """Entry point"""

    args = parse_args()

    """TODO: Implement Handling Input Pipe"""
    

    if args.c:
        string = byte_count(args.c)
        filed = args.c

    if args.l:
        string = line_count(args.l)
        filed = args.l

    if args.w:
        string = word_count(args.w)
        filed = args.w

    if args.m:
        string = char_count(args.m)
        filed = args.m

    if args.file:
        string = ""
        length = line_count(args.file)
        word = word_count(args.file)
        byte = byte_count(args.file)
        
        string = f'{length:7}{word:8}{byte:8}'
        filed = args.file
        
    print(f'{string} {filed}')
        

def parse_args():
    parser = argparse.ArgumentParser(
        prog='Aero WC',
        description='Clone of wc Command Line Tool',
        epilog='Have a nice day!'
    )

    c_parser = parser.add_argument('-c', type=str, help='Return Byte Count of File')
    l_parser = parser.add_argument('-l', type=str, help='Return Line Count of File')
    w_parser = parser.add_argument('-w', type=str, help='Return Word Count of File')
    m_parser = parser.add_argument('-m', type=str, help='Return Character Count of File')
    file_parser = parser.add_argument('file', type=str, nargs='?', help='File to process')

    args = parser.parse_args()

    return args

def byte_count(file):
    with open (file, 'rb') as f:
        return len(f.read())

def line_count(file):
    with open (file, 'r') as f:
        count = 0
        for line in f.readlines():
            count += 1
        return count

def word_count(file):
    with open (file, 'r') as f:
        count = 0
        for line in f.readlines():
            count += len(line.split())
        return count

def char_count(file):
    with open (file, 'r', encoding='utf-8') as f:
        count = 0
        for line in f:
            count += len(line)
            count += 1
        return count


if __name__ == "__main__":
    main()