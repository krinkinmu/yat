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

if (1) {
} else {
  print(-1);
}

if (0) {
  print(-1);
}

if (0) {
  print(-1);
} else {
}
