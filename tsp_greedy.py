import matplotlib.pyplot as plt
from util import City, read_cities, generate_write_cities, calculate_path_cost
from typing import List

SIZE: int = 25
AUTO_GENERATE: bool = False

class Greedy:
    def __init__(self, cities: List[City]):
        self.unvisited_cities = cities[1:]
        self.route = [cities[0]]

    def run(self) -> float:
        """
        Run the Greedy algorithm to find the shortest route.

        Returns:
            float: The cost of the shortest route.
        """
        step_number: int = 0
        plt.ion()
        plt.show(block=False)
        self.initialize_plot()

        while self.unvisited_cities:
            index, nearest_city = min(
                enumerate(self.unvisited_cities),
                key=lambda item: item[1].distance(self.route[-1])
            )
            step_number += 1
            self.route.append(nearest_city)
            del self.unvisited_cities[index]
            self.plot_interactive(False, step_number)

        self.route.append(self.route[0])
        self.plot_interactive(False, step_number=0)
        return calculate_path_cost(self.route)

    def plot_interactive(self, block: bool, step_number: int) -> None:
        """
        Plot the route interactively.

        Args:
            block (bool): Whether to block the plot.
            number (int): The number to display next to the city on the plot.

        Returns:
            None
        """
        x1, y1, x2, y2 = self.route[-2].x, self.route[-2].y, self.route[-1].x, self.route[-1].y
        x_first, y_first = self.route[0].x, self.route[0].y
        plt.plot([x1, x2], [y1, y2], 'g')
        plt.plot(x_first, y_first, 'bo')
        plt.text(x2, y2 + 20, str(step_number), fontsize=10, ha='center', va='bottom')
        plt.draw()
        plt.pause(0.3)
        plt.show(block=block)

    def initialize_plot(self) -> None:
        """
        Initialize the plot.

        Returns:
            None
        """
        fig = plt.figure(0)
        fig.suptitle('Algorytm najmniejszej krawędzi')
        x_list, y_list = [], []
        for city in [*self.route, *self.unvisited_cities]:
            x_list.append(city.x)
            y_list.append(city.y)
        x_list.append(self.route[0].x)
        y_list.append(self.route[0].y)

        plt.plot(x_list[1:], y_list[1:], 'ro')
        plt.plot(x_list[0], y_list[0], 'bo')
        plt.show(block=False)


if __name__ == "__main__":
    
    if AUTO_GENERATE:
        generate_write_cities(SIZE)
    cities = read_cities(SIZE)
    greedy = Greedy(cities)

    print(f"Znaleziona droga: {greedy.run()}")
    print(f"Kolejność punktów/miast: {greedy.route}")
    plt.show(block=True)
