from math import exp,sin
import matplotlib.pyplot as plt
from scipy.fftpack import rfft,fft ##rfft stands for real fast fourier transform


### I expect the fft of a sinus to be a spike at the frequece of the sinus.

    x = np.linspace(0,2*np.pi,1000)
    y = []
    for i in x:
        #y.append(exp(i -9) + exp(-i +2))
        y.append(sin(1*i))

    fft_transf = fft(y)

    plt.figure()
    plt.plot(x,y)

    #f=[]
    #for i in x:
    #    f.append(1./i)
    plt.figure()
    plt.plot(fft_transf)
