import numpy as np
import matplotlib.pyplot as plt
import random

# Set image size and number of fractal points
WIDTH, HEIGHT = 800, 800
NUM_POINTS = 100000

# Define triangle vertices (like the Sierpiński triangle)
vertices = np.array([
    [0.5, 0],
    [0, 1],
    [1, 1]
])

def generate_fractal():
    """
    Generates fractal art using the Chaos Game method.
    Returns an array of points.
    """
    # Start at a random point
    x, y = random.random(), random.random()
    points = []

    for _ in range(NUM_POINTS):
        # Pick a random vertex
        vertex = vertices[np.random.randint(0, 3)]
        # Move halfway toward that vertex
        x = (x + vertex[0]) / 2
        y = (y + vertex[1]) / 2
        points.append((x, y))

    return np.array(points)

def plot_fractal(points, color_map='magma'):
    """
    Plots the fractal using matplotlib.
    """
    plt.figure(figsize=(8, 8), dpi=100)
    plt.axis('off')
    plt.scatter(points[:, 0], points[:, 1], s=0.1, c=np.linspace(0, 1, len(points)), cmap=color_map)
    plt.title("Procedural Fractal Art", fontsize=16)
    plt.tight_layout()
    plt.savefig("fractal_art.png", dpi=300, bbox_inches='tight')
    plt.show()

def main():
    print("Generating fractal art...")
    points = generate_fractal()
    plot_fractal(points)
    print("Done! Image saved as fractal_art.png")

if __name__ == "__main__":
    main()
