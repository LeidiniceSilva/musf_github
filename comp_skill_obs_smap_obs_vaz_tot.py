# -*- coding: utf-8 -*-

""" Compute climatology of fluviometric flow. """

import netCDF4
import os

from pylab import *
from matplotlib import pyplot as plt
from PyFuncemeClimateTools import ClimateStats as cs
from hidropy.utils.hidropy_utils import basin_dict, create_path
from matplotlib.font_manager import FontProperties
from basins_names_code import basins_flow

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "19/05/2017"
__description__ = "Compute climatology of fluviometric flow for kind month of the year"

scale = 'monthly'
month = 'dez'
param = 'flow'
home  = os.path.expanduser("~")
hidropy_path = "/home/leidinice/documentos/projetos_git_funceme"

print month


def all_indices(basin_code, list_idx):
    
    indices = []
    idx = -1
    
    while True:
        try:
            idx = list_idx.index(basin_code, idx+1)
            indices.append(idx)
        except ValueError:
            break
    
    return indices


def load_flow_obs(basin_name, mon):

    path_in  = '{0}/io/flow/smap_monthly/'.format(home)
    flow_obs = 'flow_obs_fluviometric_stations.asc'

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

macros_total = ['amazonas', 'atlantico_leste', 'atlantico_sudeste', 'atlantico_sul', 'doca,' 'grande', 'iguacu',
                'jacui', 'paraguai', 'paraiba_do_sul', 'parana', 'paranaiba', 'paranapanema', 'parnaiba',
                'sao_francisco', 'tiete', 'tocantins', 'uruguai']

for macro in macros_total:

    folders = os.listdir("{0}/hidropy/hidropy/shapes/basins/".format(hidropy_path))
    basins  = sorted(basin_dict(micro=True, basin_name=macro))
    basin_name = macro
    print macro

    bas_new1 = []
    for bas1 in basins:
        if '_henry' not in (bas1):
            bas_new1.append(bas1)

    bas_new2 = []
    for bas2 in bas_new1:
        if '_jauru' not in (bas2):
            bas_new2.append(bas2)

    bas_new3 = []
    for bas3 in bas_new2:
        if '_xingo' not in (bas3):
            bas_new3.append(bas3)

    bas_new = []
    for bas in bas_new3:
        if '_inc' not in (bas):
            bas_new.append(bas)

    len_bas = len(bas_new)

    CORREL = []
    MBE    = []
    RMSE   = []

    for basin in bas_new:
        basin_fullname = basin_dict(basin)[2]
        macro_name     = basin_dict(basin)[1]
        print basin

        vazpaste = load_flow_obs(basin_fullname, 12)

        obs_tot = []
        link1 = home + "/io/flow/smap_monthly/obs/{0}".format(macro_name)
        arq1  = "{0}/{1}_{2}_bases_obs_19810101_20170401_smap_{3}.nc".format(link1, param, scale,
                                                                                       basin_fullname)
        data1 = netCDF4.Dataset(arq1)
        variable1 = data1.variables[param][:].T
        time1   = data1.variables['time']
        st_obs1 = variable1[0:360]

        obs_tot.append(st_obs1[11::12])

        # Calculate correlacao, bias and rmse of pr_thiessen
        corr1 = np.corrcoef(np.squeeze(obs_tot), np.squeeze(vazpaste))
        CORR  = np.array([round(corr1[0][1], 3)])
        CORREL.append(CORR)

        vies1 = np.nanmean(np.squeeze(obs_tot) - np.squeeze(vazpaste))
        BIAS  = np.array([vies1])
        MBE.append(BIAS)

        rmse1 = cs.compute_rmse(np.squeeze(obs_tot), np.squeeze(vazpaste))
        ERRO  = np.array([rmse1])
        RMSE.append(ERRO)

        # print CORREL
        # print MBE
        # print RMSE
        # exit()

    list_basins = []
    fig, ax = plt.subplots(3, figsize=(240, 200))
    cmap = plt.cm.gray
    line_colors = cmap(np.linspace(0, 3))

    x = np.arange(len(CORREL))
    y = np.arange(len(MBE))
    z = np.arange(len(RMSE))

    labels = np.arange(len(bas_new))
    width_n = 0.8

    fig.suptitle(u'Índices: CORRELAÇÃO, MBE e RMSE \n Obs_smap x Vazpast / {0} - 1981_2010 \n Bacia: {1} - Usinas:'
                 u' Totais'.format(month.capitalize(), macro_name.capitalize()), fontsize=250,
                 fontweight='bold')

    a = ax[0].bar(x, CORREL, width_n, color=line_colors, label=bas_new, align='center', linewidth=20.0)
    highest_correl = max([max(CORREL)])
    ax[0].yaxis.set_ticks(np.arange(-1, highest_correl + 0.1, highest_correl/5))
    ax[0].axhline(y=0, linewidth=10, color='k')
    ax[0].set_ylabel(u'Correlação', fontsize=250, fontweight='bold')
    ax[0].tick_params(axis='both', which='major', labelbottom='off', labelsize=150, length=20, width=10, pad=20,
                      labelcolor='k')

    b = ax[1].bar(x, MBE, width_n, color=line_colors, label=bas_new, align='center', linewidth=20.0)
    ax[1].axhline(y=0, linewidth=10, color='k')
    ax[1].set_ylabel(u'MBE', fontsize=250, fontweight='bold')
    ax[1].tick_params(axis='both', which='major', labelbottom='off', labelsize=150, length=20, width=10, pad=20,
                      labelcolor='k')

    c = ax[2].bar(x, RMSE, width_n, color=line_colors, label=bas_new, align='center', linewidth=20.0)
    ax[2].axhline(y=0, linewidth=10, color='k')
    ax[2].set_ylabel(u'RMSE', fontsize=250, fontweight='bold')
    ax[2].tick_params(axis='both', which='major', labelbottom='off', labelsize=150, length=20, width=10, pad=20,
                      labelcolor='k')
    plt.xlabel(u'Usinas', fontsize=250, fontweight='bold')

    for i in range(len(bas_new)):
        list_basins.append(bas_new[i].split('{0}_'.format(basin_name))[1].capitalize())

    font = FontProperties(weight='bold', size=180)
    plt.figlegend(a, list_basins, loc=8, ncol=6, prop=font)

    path_out = ('/home/leidinice/documentos/results/indices_flow/81-10/{0}/{1}/'.format(month, macro_name))
    if not os.path.exists(path_out):
        create_path(path_out)

    plt.savefig(os.path.join(path_out, '{0}_tot_indices_{1}_{2}.png'.format(macro_name, param, month)), dpi=25)
    plt.close('all')
    plt.cla()
