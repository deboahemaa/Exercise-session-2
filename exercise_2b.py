# The independent variables are: t
# The dependent variables are y, y' and y''
# 
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta():
    h = 0.1
    y = np.zeros((2), float)
    y[0] = 3
    y[1] = -5
    kvector = np.zeros((2), float)
    x_list = [y[0]]
    v_list = [y[1]]
    t_list = [0]

    for time in np.arange(h, 20, h):
        a_n = -100 * y[0] - 2 * y[1] + np.sin(3*time)
        kvector[0] = h * y[1]
        kvector[1] = h * a_n
        y[0] += (kvector[0] + h/2)
        y[1] += (kvector[1] + np.sqrt(kvector[0]**2 + kvector[1]**2)/2)
        x_list.append(y[0])
        t_list.append(time)

    plt.plot(t_list, x_list)
    plt.show()
    return

runge_kutta()