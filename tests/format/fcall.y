def main() {
    def foo() {
        1;
    }
    foo() + foo();
}

def bar(a, b, c, d, e) {
    bar(b, c, d, e, a);
}

bar(1, 2, 3, 4, 5);
bar(1, 2, 3, 4, 5)(5, 4, 3, 2, 1);
