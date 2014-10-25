from parser import Parser, Scanner
from model import Scope
from printer import PrettyPrinter
from folder import ConstantFolder

if __name__ == "__main__":
    import sys
    for filename in sys.argv[1:]:
        program = Parser().parse(Scanner(filename), False)
        printer = PrettyPrinter()
        folder = ConstantFolder()
        for stmt in program:
            printer.visit(folder.visit(stmt))
