import matplotlib.pyplot as plt
import numpy as np

def euler():
    b = 100 
    h = 0.01 
    N_0 = 1
    N= N_0
    lam = 0.0431
    N_list = [N]
    t_list = [0]
    error = [0]

    for time in np.arange(1, b, h):
        f_i = - lam * N
        N = N + h * f_i 
        N_anal = N - np.exp(-lam*time)
        error.append(N_anal)
        N_list.append(N)
        t_list.append(time)

    #plt.plot(t_list, N_list)
    #plt.plot(t_list, error)
    #plt.show()
    return t_list, N_list, error

def Runge_kutta():
    N_0 = 1
    h = 0.01
    b = 100
    lam = 0.0431
    N=N_0
    N_list = [N]
    t_list = [0]
    error = [0]

    for time in np.arange(1, b, h):
        k1 = h * lam*N
        k2 = h * (-lam *N + k1 / 2)
        k3 = h * (-lam*N + k2 / 2)
        k4 = h * (-lam*N + k3)
        N = N + (1/6)*(k1 +2*k2 + 2*k3 + k4)
        N_anal = N - np.exp(-lam*time)
        error.append(N_anal)
        N_list.append(N)
        t_list.append(time)

    #plt.plot(t_list, N_list)
    #plt.plot(t_list, error) 
    #plt.show()
    return t_list, N_list, error

def plotjes():
    RK = Runge_kutta()
    EU = euler()

    fig, ax = plt.subplots(2, 2)
    ax[0,0].plot(RK[0], RK[1], label ="Runge-Kutta time vs amount")
    ax[0,1].plot(RK[0], RK[2], label="Runge-kutta time vs error")
    ax[1,0].plot(EU[0], EU[1], label = "Euler time vs amount")
    ax[1,1].plot(EU[0], EU[2], label = "Euler time vs error")
    plt.show()
    return

plotjes()