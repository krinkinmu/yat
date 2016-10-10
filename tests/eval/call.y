def call_f(f, arg) {
    f(arg);
}

def print_x(x) {
    print x;
}

call_f(print_x, 10);
call_f(print_x, 20);
