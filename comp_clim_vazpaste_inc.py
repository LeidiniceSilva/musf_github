# -*- coding: utf-8 -*-

""" Compute climatology of fluviometric flow (inc). """

import os
import netCDF4
from pylab import *
from matplotlib import pyplot as plt
from hidropy.utils.hidropy_utils import basin_dict, create_path
from matplotlib.font_manager import FontProperties
from basins_names_code import basins_flow

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "19/05/2017"
__description__ = "Compute climatology of fluviometric flow for kind month of the year (inc)"

scale = 'monthly'
month = 'jan'
param = 'flow'
home  = os.path.expanduser("~")
hidropy_path = "/home/leidinice/documentos/projetos_git_funceme"

macros_inc = ['amazonas', 'atlantico_leste', 'doce', 'grande', 'iguacu', 'jacui', 'paraiba_do_sul', 'paranaiba',
              'paranapanema', 'sao_francisco', 'tiete', 'tocantins', 'uruguai']

for macro in macros_inc:
    print macro

    folders = os.listdir("{0}/hidropy/hidropy/shapes/basins/".format(hidropy_path))
    basins  = sorted(basin_dict(micro=True, basin_name=macro))
    basin_name = macro

    # total
    bas_new1 = []
    for bas1 in basins:
        if '_coaracy' not in (bas1):
            bas_new1.append(bas1)

    bas_new2 = []
    for bas2 in bas_new1:
        if '_apolonio' not in (bas2):
            bas_new2.append(bas2)

    bas_new = []
    for bas in bas_new2:
        if '_inc' in (bas):
            bas_new.append(bas)

    len_bas = len(bas_new)

    clim = []
    plot_lines = []
    for basin in bas_new:
        basin_fullname = basin_dict(basin)[2]
        macro_name     = basin_dict(basin)[1]
        print basin

        link1 = home + "/io/flow/obs/1981-present/{0}".format(macro)
        arq1  = "{0}/{1}_{2}_ons_obs_19810115_20170615_{3}.nc".format(link1, param, scale, basin_fullname)
        data1 = netCDF4.Dataset(arq1)
        variable1 = data1.variables[param][:].T
        time1 = data1.variables['time']
        obs   = variable1[0:360]
        stc   = obs[0::12]

        climatology = np.nanmean(stc, axis=0)
        clim.append(climatology)

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
              u' Incrementais'.format(month.capitalize(), macro_name.capitalize()),
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

    path_out = ('/home/leidinice/documentos/results/vazpast/clim_flow/inc/81-10/{0}/{1}/'.format(month, macro_name))

    if not os.path.exists(path_out):
        create_path(path_out)

    plt.savefig(os.path.join(path_out, '{0}_inc_clim_{1}_{2}.png'.format(macro_name, param, month)), dpi=25)
    plt.close('all')
    plt.cla()
