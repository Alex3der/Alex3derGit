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
- **min_pheromone**: Minimum pheromone level.
- **max_pheromone**: Maximum pheromone level.
- **n_ranked**: number of ranked ants (used in updated pheromone method).
- **flag**: flag to choose pheromone update method (0 for basic ACO, 1 for improved ACO)

## Requirements
This project requires Python 3 and the following Python libraries installed:
- Numpy
- Matplotlib

## Code
**ACO.py**: This is the main file that you would want to run. It initializes the problem parameters, runs the ACO algorithm, and generates the output.

## Run
To run the code, navigate to the project directory and type the following command:
- python main.py

## How it Works
The program starts by generating a number of cities with random coordinates. An instance of the AntColony class is created, which contains the main ACO algorithm.

The ants generate paths from a random starting city until all cities are visited. The pheromone levels are updated based on the paths taken by the ants. This process is iterated several times.

Finally, the program prints out the best path found and its distance, and visualizes the cities, the path, and the distances over iterations.

Note: This project includes two versions of the ACO algorithm: a basic one and an improved one that uses ranked-based pheromone update.

## Output
The program prints out the best path found and its distance and saves the array representing the city matrix to a text file named "my_array.txt". It also generates four plots: the cities and the optimal path found by the basic ACO, the average and shortest distances over iterations for the basic ACO, the cities and the optimal path found by the improved ACO, and the average and shortest distances over iterations for the improved ACO.

## Customization
You can customize the problem parameters, such as the number of cities, the number of ants, and the number of iterations, in the main() function in main.py. You can also modify the parameters related to the ACO algorithm, such as the alpha and beta parameters, the evaporation rate, and the minimum and maximum pheromone levels, when creating the AntColony instance.
