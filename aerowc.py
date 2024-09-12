import argparse

def main():
    """Entry point"""
    args = parse_args()
    if args.c:
        with open (args.c, 'rb') as f:
            print(len(f.read()))
    if args.l:
        with open (args.l, 'r') as f:
            count = 0
            for line in f.readlines():
                count += 1
            print(count)
    if args.w:
        with open (args.w, 'r') as f:
            count = 0
            for line in f.readlines():
                count += len(line.split())
            print(count)
    if args.m:
        with open (args.m, 'r', encoding='utf-8') as f:
            count = 0
            for line in f:
                count += len(line)
                count += 1
            print(count)

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

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()