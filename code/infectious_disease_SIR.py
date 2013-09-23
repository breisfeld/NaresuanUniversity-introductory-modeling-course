import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

def SIR_basic(y, t, params):
    beta,gamma = params
    S,I,R = y
    dSdt = -beta*S*I
    dIdt = beta*S*I - gamma*I
    dRdt = gamma*I
    dy = [dSdt,dIdt,dRdt]
    return dy

def odesolve(t, y0, params, odefunc):
    soln = scipy.integrate.odeint(odefunc, y0, t, args=(params,))
    return [t,soln]

def plot_populations(t,y,populations=['S','I','R'], pxlabel='x', pylabel='y', ptitle='Simulation'):
    pdict = {'S':(0,'susceptible'),'I':(1,'infected'),'R':(2,'recovered')}
    plt.figure()
    plegend = []
    for p in populations:
        ind,name = pdict[p]
        plt.plot(t,y[:,ind])
        plegend.append(name)
    plt.title(ptitle)
    plt.xlabel(pxlabel)
    plt.ylabel(pylabel)
    plt.legend(plegend)
    plt.show()

if __name__ == '__main__':
    tspan = np.linspace(0,10*7,2000)
    y0 = S0,I0,R0 = 1.0,0.01,0.0

    params = beta,gamma = 520/365.,1./7
    [t,soln] = odesolve(tspan, y0, params, SIR_basic)
    plot_populations(t,soln,populations=['S','I','R'],
                     pxlabel='Time (days)', pylabel='Fraction of Population in Different Classes', ptitle='Basic SIR Model')

    tspan = np.linspace(0,60*365,100)
    y0 = S0,I0,R0 = 0.1,2.5E-4,0.0
    [t,soln] = odesolve(tspan, y0, params, SIR_basic)
    t_years = t/365.
    plot_populations(t_years,soln,populations=['I'],
                     pxlabel='Time (years)', pylabel='Fraction of Population Infected', ptitle='Basic SIR Model')
