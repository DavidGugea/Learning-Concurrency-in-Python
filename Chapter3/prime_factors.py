import time
import random
import threading


def calculate_prime_factors(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d

        d += 1

    if n > 1:
        primfac.append(n)

    return primfac


def execute_proc():
    for _ in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))


def main():
    print("Starting number crunching")

    t0 = time.perf_counter()

    threads = []
    for _ in range(10):
        thread = threading.Thread(target=execute_proc)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    t1 = time.perf_counter()
    total_time = t1 - t0
    print(f"Execution time: {total_time}")


if __name__ == '__main__':
    main()
