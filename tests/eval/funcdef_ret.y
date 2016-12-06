def foo(n) {
    if (n) {
        def bar() {
            print 1;
        }
    } else {
        def baz() {
            print 2;
        }
    }
}
foo(0)();
foo(1)();
