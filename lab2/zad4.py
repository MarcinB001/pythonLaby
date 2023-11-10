class FibonacciIterator:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0
        self.x = 0
        self.y = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_step < self.steps:
            temp_x = self.x
            temp_y = self.y
            self.x = temp_y
            self.y = temp_x + temp_y
            self.current_step += 1
            return temp_x
        else:
            raise StopIteration


if __name__ == '__main__':

    fibonacci_iter = FibonacciIterator(10)

    for i in fibonacci_iter:
        print(i)
