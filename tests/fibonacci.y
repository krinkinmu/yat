def fibonacci(current, next, index) {
    if (index == 0) {
        print current;
    } else {
        fibonacci(next, current + next, index - 1);
    }
}
read index;
fibonacci(0, 0, index);
