# Ant Colony Optimization for TSP

This project uses the Ant Colony Optimization (ACO) algorithm to solve the Travelling Salesman Problem (TSP). The ACO algorithm is a probabilistic technique for solving computational problems which can be reduced to finding good paths through graphs. 

## Code Structure

- **AntColony**: The main class which represents the ant colony. This class includes methods to calculate distances between cities, generate paths for ants, and update pheromone levels.

- **generate_cities(n, size)**: This function generates `n` cities within a specified `size` map. The coordinates of the cities are random.

- **generate_city_matrix(cities, map_size)**: This function generates a matrix that represents the locations of the cities.

- **plot_cities(cities, path)**: This function plots the cities and the best path the algorithm finds.

- **plot_distances(avg_distances, shortest_distances)**: This function plots the average and shortest distances over iterations.

- **main()**: The main function to execute the program. It sets up the parameters, generates the cities, creates the AntColony instance, runs the algorithm, and plots the results.

## Parameters

- **n_cities**: The number of cities.
- **map_size**: The size of the map.
- **n_ants**: The number of ants in the colony.
- **n_iterations**: The number of iterations for the algorithm.
- **alpha**: The relative importance of pheromone.
- **beta**: The relative importance of heuristic information.
- **evaporation_rate**: The rate at which pheromone evaporates.
