#!/usr/bin/env python3

import argparse
from typing import Union


def sign_of_x_plus_one(x: Union[int, float]) -> int:
    """Return the sign of (x + 1): 1 if positive, -1 if negative, 0 if zero."""
    value = x + 1
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute x+1 and return its sign as -1, 0, or 1.")
    parser.add_argument("x", type=float, help="Input value x")
    args = parser.parse_args()

    result = sign_of_x_plus_one(args.x)
    print(result)


if __name__ == "__main__":
    main()