from parser import Parser, Scanner
from model import Scope
from printer import PrettyPrinter

if __name__ == "__main__":
    import sys
    for filename in sys.argv[1:]:
        program = Parser().parse(Scanner(filename), False)
        for stmt in program:
            PrettyPrinter().visit(stmt)