from utilities import randomize_string, reverse_string, sort_string, fibonacci
from time import time


def main() -> None:
    user_input = input("Please, type a message (or integer): ")

    start = time()

    print(f"Randomized: {randomize_string(user_input)}")
    print(f"Reversed: {reverse_string(user_input)}")
    print(f"Sorted: {sort_string(user_input)}")
    # Run Fibonacci calculation if user input is a small integer.
    if user_input.isnumeric() and int(user_input) <= 50:
        print(f"Fibonacci: {fibonacci(int(user_input))}")

    end = time()
    print(f"Finished in {end-start:.4f}s.")


if __name__ == "__main__":
    main()
