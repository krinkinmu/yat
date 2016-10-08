#!/usr/bin/env python3

from parser import Parser, Scanner
from model import Scope

if __name__ == "__main__":
    import sys
    for filename in sys.argv[1:]:
        program = Parser().parse(Scanner(filename))
        program.evaluate(Scope())
