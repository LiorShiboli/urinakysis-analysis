import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import seaborn as sns

from src.example import add


def main() -> None:
    print("\n" * 5)
    print("Hello World!")

    print(np)
    print(pd)
    print(plt)
    print(sns)
    print(nltk)

    print("\n\n")
    print("5 + 7 = ", add(5, 7))


if __name__ == "__main__":
    main()
