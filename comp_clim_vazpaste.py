# -*- coding: utf-8 -*-

""" Compute climatology of fluviometric flow. """

import os

from pylab import *
from matplotlib import pyplot as plt
from hidropy.utils.hidropy_utils import basin_dict, create_path
from matplotlib.font_manager import FontProperties
from basins_names_code import basins_flow

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "19/05/2017"
__description__ = "Compute climatology of fluviometric flow for kind month of the year"

scale = 'monthly'
month = 'jan'
param = 'flow'
home  = os.path.expanduser("~")
hidropy_path = "/home/leidinice/documentos/projetos_git_funceme"


def all_indices(basin_code, list_idx):
    
    indices = []
    idx     = -1
   
    while True:
        try:
            idx = list_idx.index(basin_code, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices


def load_flow_obs(basin_name, mon):

    path_in  = '{0}/io/flow/smap_monthly/'.format(home)
    flow_obs = 'flow_jun.asc'

    imp_data = np.loadtxt(path_in+flow_obs)
    list_idx = list(imp_data[:, 0])

    basin_code = basins_flow[basin_name]
    idx_list   = all_indices(basin_code, list_idx)

    data_aux   = imp_data[idx_list[0]:idx_list[-1] + 1, :]
    list_years = list(imp_data[idx_list[0]:idx_list[-1] + 1, 1])
    idx_flow   = []

    for y in range(1981, 2010 + 1):
        idx_flow.append((all_indices(y, list_years))[0])

    var = data_aux[idx_flow[0]:idx_flow[-1]+1, 2:][:, mon-1]

    return var

macros_total = ['amazonas', 'atlantico_leste', 'atlantico_sudeste', 'atlantico_sul', 'doce', 'grande', 'iguacu',
                'jacui', 'paraguai', 'paraiba_do_sul', 'parana', 'paranaiba', 'paranapanema', 'parnaiba',
                'sao_francisco', 'tiete', 'tocantins', 'uruguai']

for macro in macros_total:

    folders = os.listdir("{0}/hidropy/hidropy/shapes/basins/".format(hidropy_path))
    basins  = sorted(basin_dict(micro=True, basin_name=macro))
    basin_name = macro
    print macro

    bas_new = []
    for bas in basins:
        if '_inc' not in (bas):
            bas_new.append(bas)

    len_bas = len(bas_new)

    clim = []
    plot_lines = []
    
    for basin in bas_new:
        basin_fullname = basin_dict(basin)[2]
        macro_name     = basin_dict(basin)[1]

        stc = load_flow_obs(basin_fullname, 1)

        climatology = np.nanmean(stc, axis=0)
        clim.append(climatology)
        print basin
        print climatology

    list_basins = []
    clim = np.array(clim).T

    fig, ax = plt.subplots(1, figsize=(160, 120))
    cmap    = plt.cm.gray
    line_colors = cmap(np.linspace(0, 3))

    x = np.arange(len(clim))
    labels  = np.arange(len(bas_new))
    width_n = 1

    a = plt.bar(x, clim, width_n, color=line_colors, label=bas_new, align='center', linewidth=10.0)
    plt.title(u'Climatologia da vazão observada - {0} \n Bacia: {1} - Usinas:'
              u' Totais'.format(month.capitalize(), macro_name.capitalize()),
              fontsize=200, fontweight='bold')

    highest_value = max([max(clim)])
    ax.yaxis.set_ticks(np.arange(0, highest_value + 50, highest_value/10))

    plt.xlabel(u'Usinas', fontsize=180, fontweight='bold')
    plt.ylabel(u'Vazão (m3/s)', fontsize=180, fontweight='bold')

    plt.tick_params(axis='both', which='major', labelbottom='off', labelsize=120, length=40, width=10, pad=40,
                    labelcolor='k')

    for i in range(len(bas_new)):
        list_basins.append(bas_new[i].split('{0}_'.format(basin_name))[1].capitalize())

    font = FontProperties(weight='bold', size=120)
    plt.figlegend(a, list_basins, loc=8, ncol=6, prop=font)

    path_out = ("/home/leidinice/documentos/results/vazpaste_clim/81-10/{0}/{1}/".format(month, macro_name))
    if not os.path.exists(path_out):
        create_path(path_out)

    plt.savefig(os.path.join(path_out, '{0}_tot_clim_{1}_{2}.png'.format(macro_name, param, month)), dpi=25)
    plt.close('all')
    plt.cla()
