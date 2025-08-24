
#! usr/bin/env python3
import argparse
def main():
    parser = argparse.ArgumentParser(description="A friendly greeing with script.")
    parser.add_argument('--name', type=str, help='Name of the person to greet'   , required=False, default='World')
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()

