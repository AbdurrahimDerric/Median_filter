import numpy as np
import matplotlib.pyplot as pp



def main():
    window_size = int(input('please enter window size for median filtering \n'))
    X = [1,2,3,4,5,88,7,8,9,10]
    Y = filter_by_median(X,window_size)
    print(Y)
    val = 0.5
    pp.plot(Y, np.zeros_like(Y) + val, 'x')
    pp.show()



def get_median(window,window_size):
    median = 0
    if (window_size % 2) == 0:
        median = window[window_size//2]
        median += window[window_size//2 +1]
        median = median/2
    else:
        median = window[window_size//2]

    return median


def filter_by_median(X,window_size):
    Y = []

    for i in range(len(X)):
        window = X[:window_size]
        median = get_median(window,window_size)
        Y.append(median)
        window_size +=1

    return Y


main()
