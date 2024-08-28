#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: addition.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    except ValueError:
        print("Both arguments must be numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
