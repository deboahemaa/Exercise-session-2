import numpy as np
import matplotlib.pyplot as plt

def euler(h):
    y = 1
    t = 0
    y_list =[y]
    t_list = [t]
    y_anal_list = [1]
    dev = 0 
    max_dev = 0

    for time in np.arange(h, 2, h):
        y = y + h*(time - 2*y)
        y_anal = 0.25 * (2*time - 1 + 5 * np.exp(-2*time))
        y_list.append(y)
        t_list.append(time)
        y_anal_list.append(np.abs(y - y_anal))
        dev += np.abs(y - y_anal)
    
        if np.abs(y - y_anal) > max_dev:
            max_dev = np.abs(y - y_anal)
    
    global_error = dev / len(t_list)
    return t_list, y_list, y_anal_list, max_dev, global_error

def plotjes():
    f1 = euler(0.2)
    f2 = euler(0.1)
    f3 = euler(0.05)
    f4 = euler(0.025)
    plt.plot([0.2, 0.1, 0.05, 0.025], [f1[3], f2[3], f3[3], f4[3]])
    fig, ax = plt.subplots(4)
    ax[0].plot(f1[0], f1[1])
    ax[1].plot(f2[0], f2[1])
    ax[2].plot(f3[0], f3[1]) 
    ax[3].plot(f4[0], f4[1]) 
    print("The global errors are", f1[4], f2[4], f3[4], f4[4])
    print("The local errors are", f1[3], f2[3], f3[3], f4[3])
    plt.show()
    return

plotjes()