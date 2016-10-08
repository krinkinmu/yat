from yat.parser import Parser, Scanner
from yat.model import Scope
from yat.printer import PrettyPrinter

if __name__ == "__main__":
    import sys
    for filename in sys.argv[1:]:
        program = Parser().parse(Scanner(filename), False)
        printer = PrettyPrinter()
        for stmt in program:
            printer.visit(stmt)
