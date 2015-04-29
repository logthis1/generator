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
    print len(squarev)
    plt.plot(squarev)
    plt.show()

def sinewave(freq, amp, phase):
    sinev = []
    for i in drange(0, 1, 0.000244140625):
        a = decimal.Decimal(2*math.pi*freq)
        b = decimal.Decimal(i)*a
        c = decimal.Decimal(math.sin(b))
        d = amp*c
        #e = d*decimal.Decimal(2048)
        #f = round(d)
        sinev.append(d)
    return sinev
    #plt.plot(sinev)
    #plt.show()
        
def triwave(freq, amp, phase):
    a = amp
    f = freq
    phase = 0
    triv = []
    for i in drange(0, 1, 0.000244140625):
        if phase < math.pi:
            b = -a +(2*a/math.pi)*phase
            triv.append(b)
        else:
            b = 3*a-(2*a/math.pi)*phase
            triv.append(b)
        phase = phase + ((2*math.pi*f)/4096)
        if phase > (2*math.pi):
            phase = phase -(2*math.pi)
    return triv
    #plt.plot(triv)
    #plt.show()

def sineplustri(freq, amp, phase):
    si = sinewave(freq, amp, phase)
    tr = triwave(2*freq, amp, 0)
    pl = []
    for i in range(0,4095):
        a = decimal.Decimal(si[i])+decimal.Decimal(tr[i])
        pl.append(a)
    plt.plot(pl)
    plt.show()
    return pl
