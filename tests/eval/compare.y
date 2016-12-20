def foo(x) {
    if (x) { print 1; } else { print 0; }
}
def bar(x, y) {
    foo(x <= y);
    foo(x <  y);
    foo(x >= y);
    foo(x >  y);
    foo(x == y);
    foo(x != y);
}
bar(1, 2);
bar(1, 1);
print(1 <= 0);
print(1 <  0);
print(0 >= 1);
print(0 >  1);
print(1 == 0);
print(0 != 0);
