import math
import time


def main():
    start = time.time()

    functions = (math.sqrt, math.sin, math.cos, math.floor)

    for func in functions:
        for i in range(10000000):
            func(i)

    end = time.time()
    print(f"Finished in {end - start} seconds.")


if __name__ == "__main__":
    main()
