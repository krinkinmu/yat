def main(variable) {
    if (variable) {
        def foo() {
            print variable;
        }
    } else {
        def foo() {
            read variable;
        }
    }
    foo;
}

read arg;
main(arg)();

read other;
main(other)();

read variable;
main(variable)();
