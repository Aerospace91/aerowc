import argparse
import sys

def main():
    """Entry point"""

    args = parse_args()

    #Check if input is being piped
    if not sys.stdin.isatty():
        #If input is piped, read from stdin
        content = sys.stdin.read()
        binary_content = content.encode('utf-8') #Convert to bytes
        filename = "(stdin)"

    elif args.file:
        #If a file is provided, read from file.
        content = read_file(args.file)
        binary_content = read_binary_file(args.file)
        filename = args.file

    else:
        print("No File or piped input provided.")
        return


    result = {
        'length': line_count(content),
        'words': word_count(content),
        'bytes': byte_count(binary_content),
        'chars': char_count(content)
    }

    if args.c:
        print(f'{byte_count(content):7 {args.file}}')
    elif args.l:
        print(f'{result["length"]:7} {args.file}')
    elif args.w:
        print(f'{result["words"]:7} {args.file}')
    elif args.m:
        print(f'{result["chars"]:7} {args.file}')
    else:
        print(f'{result["length"]:7}{result["words"]:8}{result["bytes"]:8} {args.file}')

        

def parse_args():
    parser = argparse.ArgumentParser(
        prog='Aero WC',
        description='Clone of wc Command Line Tool',
        epilog='Have a nice day!'
    )

    parser.add_argument('-c', action='store_true', help='Return Byte Count of File')
    parser.add_argument('-l', action='store_true', help='Return Line Count of File')
    parser.add_argument('-w', action='store_true', help='Return Word Count of File')
    parser.add_argument('-m', action='store_true', help='Return Character Count of File')
    parser.add_argument('file', type=str, nargs='?', help='File to process')

    return parser.parse_args()


def read_file(file):
    """Read the entire content of the file"""
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def read_binary_file(file):
    with open(file, 'rb') as f:
        return f.read()

def byte_count(binary_content):
    return len(binary_content)

def line_count(content):
    return content.count('\n')

def word_count(content):
    return len(content.split())

def char_count(content):
    return len(content)


if __name__ == "__main__":
    main()