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

def parse_args():
    parser = argparse.ArgumentParser(
        prog='Aero WC',
        description='Clone of wc Command Line Tool',
        epilog='Have a nice day!'
    )

    c_parser = parser.add_argument('-c', type=str, help='Return Byte Count of File')
    l_parser = parser.add_argument('-l', type=str, help='Return Line Count of File')

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()