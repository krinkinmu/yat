#!/usr/bin/env python3

from yat.parser import Parser, Scanner
from yat.model import Scope

if __name__ == "__main__":
    import sys
    for filename in sys.argv[1:]:
        program = Parser().parse(Scanner(filename))
        program.evaluate(Scope())
