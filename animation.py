import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update(f):
    ax.cla()  # ax をクリア
    ax.grid()
    ax.plot(np.cos(theta), np.sin(theta), c="gray")
    ax.plot(np.cos(f), np.sin(f), "o", c="red")


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect=1)

    theta = np.linspace(0, 2 * np.pi, 128)

    anim = FuncAnimation(fig, update, frames=np.pi * np.arange(0, 2, 0.25), interval=200)
    plt.show()

    anim.save("c03.gif", writer="imagemagick")
    plt.close()
