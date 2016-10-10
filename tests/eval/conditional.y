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

if (main(10)()) {
} else {
}

if (main(20)()) {
  print(30);
} else {
}

if (main(40)()) {
} else {
  print(50);
}

if (main(60)()) {
  print(70);
} else {
  print(80);
}
