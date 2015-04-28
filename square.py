import math
import decimal
import matplotlib.pyplot as plt

def drange(start, stop, step):
    while start < stop:
        yield start
        start += step

def squarewave(freq, amp):    
    squarev = []
    a = amp
    f = freq
    phase = (2*math.pi*f)/4096
    for i in drange(0, 1, 0.000244140625):
        if phase < math.pi:
            squarev.append(a)
        else:
            squarev.append(-a)
        phase = phase + ((2*math.pi*f)/4096)
        if phase > (2*math.pi):
            phase = phase - (2*math.pi)
    plt.plot(squarev)
    plt.show()
