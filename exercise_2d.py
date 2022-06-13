import numpy as np
import matplotlib.pyplot as plt

def Runge(x0, v0):
    # Startwaarden
    x = x0
    v = v0
    t0 = 0

    # Variabelen
    m = 1
    h = 0.01
    phi_max = 5
    xpot = 5

    # 2-vector with dependent variable
    y = np.zeros((2), float)
    y[0] = x
    y[1] = v

    # lists
    x_list = [x]
    t_list = [t0]
    v_list = [v0]

    for time in np.arange(h, 6, h):
        kvector = np.zeros((8), float)
        x_i = y[1]
        y_i = (-y[0] +  xpot) * phi_max * (np.exp(-0.5*(y[0]-xpot)**2))
        kvector[0] = h * x_i # k1 dx/dt
        kvector[1] = h * (x_i + h/2) # k2 dx/dt
        kvector[2] = h * (x_i + h/2)# k3 dx/dt
        kvector[3] = h * (x_i + h)  # k4 dx/dt
        kvector[4] = h * y_i
        kvector[5] = h * (y_i + kvector[0]/2)
        kvector[6] = h * (y_i + kvector[1]/2)
        kvector[7] = h * (y_i + kvector[2])
        y[0] = y[0] + (1/6)*(kvector[0] + 2*kvector[1] + 2*kvector[2] + kvector[3])
        y[1] = y[1] + (1/6)*(kvector[4] + 2*kvector[5] + 2*kvector[6] + kvector[7])
        x_list.append(y[0])
        t_list.append(time)
        v_list.append(y[1])
    
    plt.plot(t_list, x_list, label="position")
    plt.plot(t_list, v_list, label="velocity")
    plt.legend(loc="upper left")
    plt.title('Runge kutta')
    plt.show()
    return x_list, v_list, t_list

RK = Runge(0,1)
x = RK[0]
v = RK[1]
t = RK[2]

def Adams(x0, x1, v0, v1, t0, t1):

    # Lijst met initiele twee waardes
    x_list = [x0, x1]
    t_list = [t0, t1]
    v_list = [v0, v1]

    # vector voor de (i-1)-ste stap
    y_0 = np.zeros((2), float)
    y_0[0] = x0
    y_0[1] = v0

    # vector voor de i-de stap
    y_1 = np.zeros((2), float)
    y_1[0] = x1
    y_1[1] = v1

    # vector voor de (i+1)-ste
    y_2 = np.zeros((2), float)

    # nieuwe vector voor bepalen y_(i+1)
    factor = np.zeros((2), float)

    # Variabelen
    m = 1
    h = 0.01
    phi_max = 5
    xpot = 5

    # for loop die y_(i+1) bepaalt tussen de 3e en laatste stap
    for time in np.arange(t1+h, 6, h):
        factor[0] = h * (1.5 * y_1[1] - 0.5 * y_0[1])
        factor[1] = h * (1.5 * (-y_1[0] + xpot) * phi_max * (np.exp(-0.5*(y_1[0]-xpot)**2)) - 0.5*(-y_0[0] + xpot)*phi_max*(np.exp(-0.5*(y_0[0]-xpot)**2)))
        y_2[0] = y_1[0] + factor[0]
        y_2[1] = y_1[1] + factor[1]

        y_0[0] = y_1[0]
        y_0[1] = y_1[1]

        y_1[0] = y_2[0]
        y_1[1] = y_2[1]
        
        t_list.append(time)
        x_list.append(y_2[0])
        v_list.append(y_2[1])
    plt.plot(t_list, x_list, label="position")
    plt.plot(t_list, v_list, label="velocity")
    plt.legend(loc="upper left")
    plt.title('Adams-bashforth')
    plt.show()
    return

Adams(x[0], x[1], v[0], v[1], t[0], t[1])


