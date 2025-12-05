import time
from contextlib import contextmanager

# Реализация на основе класса
class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"time: {elapsed_time:.1f}")

# Реализация с использованием contextlib
@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"time: {elapsed_time:.1f}")


if __name__ == '__main__':
    from time import sleep
    
    print("Тест cm_timer_1 (реализация на основе класса):")
    with cm_timer_1():
        sleep(2.5)
    
    print("\nТест cm_timer_2 (реализация с contextlib):")
    with cm_timer_2():
        sleep(1.5)
    
    print("\nТест с более длительной операцией:")
    with cm_timer_1():
        sleep(3.2)