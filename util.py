import math
import random
import matplotlib.pyplot as plt
from typing import List


class City:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, city: type["City"]) -> float:
        """Calculate the Euclidean distance between two cities."""
        return math.hypot(self.x - city.x, self.y - city.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def read_cities(size: int) -> List[City]:
    """
    Read cities from a file and return a list of City objects.

    Args:
        size (int): The number of cities to read.

    Returns:
        List[City]: A list of City objects.
    """
    cities = []
    with open(f"testing_cities/test_{size}_data.data", "r") as handle:
        lines = handle.readlines()
        for line in lines:
            x, y = map(float, line.split())
            cities.append(City(x, y))
    return cities


def generate_write_cities(size: int) -> List[City]:
    """
    Generate random cities, write them to a file, and return the list of City objects.

    Args:
        size (int): The number of cities to generate and write.

    Returns:
        List[City]: A list of City objects.
    """
    cities = [
        City(x=int(random.random() * 1000), y=int(random.random() * 1000))
        for _ in range(size)
    ]
    with open(f"testing_cities/test_{size}_data.data", "w+") as handle:
        for city in cities:
            handle.write(f"{city.x} {city.y}\n")
    return cities

def calculate_path_cost(route: List[City]) -> float:
    """
    Calculate the total cost of the given route.

    Args:
        route (List[City]): A list of City objects representing a route.

    Returns:
        float: The total cost of the route.
    """
    return round(sum(city.distance(route[index - 1]) for index, city in enumerate(route)),2)
