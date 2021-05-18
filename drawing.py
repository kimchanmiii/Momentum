import matplotlib.pyplot as plt
import numpy as np

def show(function, iter_X, iter_z, iter_count):
    iter_x = np.empty(0)
    iter_y = np.empty(0)
    x = np.linspace(0, 2, 250)
    y = np.linspace(0, 2, 250)
    X_, Y_ = np.meshgrid(x, y)
    Z_ = np.zeros((250,250))
    for i in range(250):
        for j in range(250):
            Z_[i,j] = function.get_value([X_[i,j], Y_[i,j]])
    for X in iter_X:
        iter_x = np.append(iter_x, X[0])
        iter_y = np.append(iter_y, X[1])


    angle_x = iter_x[1:] - iter_x[:-1]
    angle_y = iter_y[1:] - iter_y[:-1]

    fig = plt.figure(figsize=(16, 8))

    ax = fig.add_subplot(1, 2, 2)
    ax.set_title('Momentum Graph')
    ax.scatter(iter_x, iter_y, color='r', marker='.')
    ax.contour(X_, Y_, Z_, 50, cmap='gist_gray')
    ax.quiver(iter_x[:-1], iter_y[:-1], angle_x, angle_y, scale_units='xy', angles='xy', scale=1, color='g', alpha=.3)

    plt.show()



