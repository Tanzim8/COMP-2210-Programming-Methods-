import math
def hello(name):
    print("Hello "+name+". Welcome to COMP 2210");

hello("Tanzim");
hello("Falcons");

print(math.sqrt(64))
print(math.pi)

import statistics
print(statistics.mean([70,85,91]))

#selective imports
from math import sqrt, pi as PI
import numpy as np

def main():
    print("Running directly")
if __name__ == "__main__":
    main()