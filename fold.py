#!/usr/bin/env python3

from yat.parser import Parser, Scanner
from yat.model import Scope
from yat.printer import PrettyPrinter
from yat.folder import ConstantFolder

if __name__ == "__main__":
    import sys
    for filename in sys.argv[1:]:
        program = Parser().parse(Scanner(filename), False)
        printer = PrettyPrinter()
        folder = ConstantFolder()
        for stmt in program:
            printer.visit(folder.visit(stmt))
