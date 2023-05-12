# Ant Colony Optimization for TSP

## Requirements
This project requires Python 3 and the following Python libraries installed:
- Numpy
- Matplotlib

## Code
`ACO.py`: This is the main file that you would want to run. It initializes the problem parameters, runs the ACO algorithm, and generates the output.

## Run
To run the code, navigate to the project directory and type the following command:
- python ACO.py

## How it Works
The program starts by generating a number of cities with random coordinates. An instance of the AntColony class is created, which contains the main ACO algorithm.

The ants generate paths from a random starting city until all cities are visited. The pheromone levels are updated based on the paths taken by the ants. This process is iterated several times.

Finally, the program prints out the best path found and its distance, and visualizes the cities, the path, and the distances over iterations.

Note: This project includes two versions of the ACO algorithm: a basic one and an improved one that uses ranked-based pheromone update.

## Output
The program prints out the best path found and its distance and saves the array representing the city matrix to a text file named "my_array.txt". It also generates four plots: the cities and the optimal path found by the basic ACO, the average and shortest distances over iterations for the basic ACO, the cities and the optimal path found by the improved ACO, and the average and shortest distances over iterations for the improved ACO.

## Customization
You can customize the problem parameters, such as the number of cities, the number of ants, and the number of iterations, in the main() function in main.py. You can also modify the parameters related to the ACO algorithm, such as the alpha and beta parameters, the evaporation rate, and the minimum and maximum pheromone levels, when creating the AntColony instance.
