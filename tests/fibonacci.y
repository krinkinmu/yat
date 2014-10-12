def fibonacci(index) {
    def fibonacci_impl(current, next, index) {
        if (index == 0) {
            print current;
        } else {
            fibonacci(next, current + next, index - 1);
        }
    }
    fibonacci_impl(0, 1, index);
}
read index;
fibonacci(index);

read index;
fibonacci(index);

read index;
fibonacci(index);
