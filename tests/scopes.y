def outer() {
    def inner() {
        print variable;
    }
    inner;
}
read variable;
outer()();
(outer())();
