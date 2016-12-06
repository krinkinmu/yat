if (!10) {
    def foo() {
      print 1;
    }
} else {
    def bar() {
      print 0;
    }
}
bar();

if (!0) {
    def foo1() {
       print 2;
    }
} else {
    def bar1() {
       print 3;
    }
}
foo1();

print(!1);
print(!2);
print(5 * !1);
