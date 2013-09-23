import numpy as np
import matplotlib.pyplot as plt

def load_data(soil_file):
    soil_data = np.loadtxt(soil_file, skiprows=1, delimiter=',') 
    return soil_data

def plot_data(sdata):
    n = sdata[:,0]
    de = -np.log2(sdata[:,1])
    perm = sdata[:,2]
    plot_specs = {'por': {'axnum': 0,
                          'xlab': 'Fractional percent porosity', 
                          'ylab': 'Permeability',
                          'shape': 'o',
                          'color': 'g',
                          'xdat': n,
                          'ydat': perm,
                          'xlim': [0,0.6]},
                  'perm': {'axnum': 1,
                           'xlab': 'Effective particle diameter', 
                           'ylab': 'Permeability',
                           'shape': 's',
                           'color': 'b',                               
                           'xdat': de,
                           'ydat': perm,
                           'xlim': [5,-1]}}
    
    fig, axes = plt.subplots(1,len(plot_specs))
    
    for v in plot_specs.values():
        ax = axes[v['axnum']]
        xlab, ylab = ax.set_xlabel(v['xlab']), ax.set_ylabel(v['ylab'])
        xtics, ytics = ax.get_xticklabels(), ax.get_yticklabels()
        line = ax.plot(v['xdat'], v['ydat'])
        ax.set_yscale('log')
        ax.set_xlim(v['xlim'])
        plt.setp(line, marker=v['shape'], linestyle='', color=v['color'], markersize=6.0)
        plt.setp([xtics, ytics], fontsize=12, color='k')
        plt.setp([xlab, ylab], fontsize=14)
        ax.grid(True)
        plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        soil_file = sys.argv[1]
    else: 
        soil_file = '../data/soil_data.csv'
    soil_data = load_data(soil_file)
    plot_data(soil_data)