#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: addition.py num1 num2")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please enter valid numbers.")
        sys.exit(1)

    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
