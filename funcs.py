import math
import numpy as np


def clamp(x:float):
    return min(max(x,-1),1)
# Activation functions
def sigmoid(x: float) -> float:
    """Standard sigmoid activation function"""
    try:
        return 2.0 / (1.0 + math.exp(-4*x))-1
    except OverflowError:
        return 0.0 if x < 0 else 1.0



def cube(x:float):
    return x**3


def tanh_activation(x: float) -> float:
    """Hyperbolic tangent activation function"""
    return math.tanh(x)


def relu(x: float) -> float:
    """ReLU activation function"""
    return max(0.0, x)


def leaky_relu(x: float, alpha: float = 0.01) -> float:
    """Leaky ReLU activation function"""
    return x if x > 0 else alpha * x
def sin(x:float):
    return math.sin(4*x)


def inv(x:float):
    return sigmoid(1/(10*x)) if x!=0 else 0

def sign(x:float):
    return -x

funcs = [clamp,sigmoid, leaky_relu, cube,sin,inv, abs,sign]




def main():
    import matplotlib.pyplot as plt
    # Create x values
    x = np.linspace(-1, 1, 100)  # 1000 points from -5 to 5

    # Calculate y values for each activation function
    y_sigmoid = [sigmoid(val) for val in x]
    y_tanh = [tanh_activation(val) for val in x]
    y_relu = [relu(val) for val in x]
    y_leaky_relu = [leaky_relu(val) for val in x]
    y_sin=[sin(val) for val in x]
    y_inv = [inv(val) for val in x]

    # Create the plot
    plt.figure(figsize=(9,6),facecolor="gray")

    # Plot each function
    plt.subplot(2, 3, 1)
    plt.plot(x, y_sigmoid, 'b-', linewidth=2, label='Sigmoid')
    plt.title('Sigmoid Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 2)
    plt.plot(x, y_tanh, 'r-', linewidth=2, label='Tanh')
    plt.title('Tanh Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 3)
    plt.plot(x, y_relu, 'g-', linewidth=2, label='ReLU')
    plt.title('ReLU Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 4)
    plt.plot(x, y_leaky_relu, 'm-', linewidth=2, label='Leaky ReLU')
    plt.title('Leaky ReLU Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 5)
    plt.plot(x, y_sin, 'm-', linewidth=2, label='Sin')
    plt.title('Sin')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 6)
    plt.plot(x, y_inv, 'm-', linewidth=2, label='Inv')
    plt.title('Inv')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__=="__main__":
    main()