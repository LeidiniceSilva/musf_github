# -*- coding: utf-8 -*-

""" Compute climatology of fluviometric flow. """


# import matplotlib as mpl; mpl.use('Agg')
import os
import netCDF4
from pylab import *
from matplotlib import pyplot as plt
from hidropy.utils.hidropy_utils import basin_dict, create_path


__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "19/05/2017"
__description__ = "Compute climatology of fluviometric flow for kind month of the year"

scale  = 'monthly'
month  = 'jan'
param  = 'flow'
period = 'hind8110'
home   = os.path.expanduser("~")
hidropy_path = "/home/leidinice/documentos/projetos_git_funceme"


macros_inc = ['amazonas', 'atlantico_leste', 'doce', 'grande', 'iguacu', 'jacui', 'paraiba_do_sul', 'paranaiba',
              'paranapanema', 'sao_francisco', 'tiete', 'tocantins', 'uruguai']

macros_total = ['amazonas', 'atlantico_leste', 'atlantico_sudeste', 'atlantico_sul', 'doce', 'grande', 'iguacu',
                'jacui', 'paraguai', 'paraiba_do_sul', 'parana', 'paranaiba', 'paranapanema', 'parnaiba',
                'sao_francisco', 'tiete', 'tocantins', 'uruguai']

for macro in macros_total:
    print macro

    folders = os.listdir("{0}/hidropy/hidropy/shapes/basins/".format(hidropy_path))
    basins  = sorted(basin_dict(micro=True, basin_name=macro))
    basin_name = macro

    # total
    bas_new1 = []
    for bas1 in basins:
        if '_henry' not in (bas1):
            bas_new1.append(bas1)

    bas_new2 = []
    for bas2 in bas_new1:
        if '_richa' not in (bas2):
            bas_new2.append(bas2)

    bas_new3 = []
    for bas3 in bas_new2:
        if '_coaracy' not in (bas3):
            bas_new3.append(bas3)

    bas_new4 = []
    for bas4 in bas_new3:
        if '_itutinga' not in (bas4):
            bas_new4.append(bas4)

    bas_new5 = []
    for bas5 in bas_new4:
        if '_apolonio' not in (bas5):
            bas_new5.append(bas5)

    bas_new = []
    for bas in bas_new5:
        if '_inc' in (bas):
            bas_new.append(bas)

    len_bas = len(bas_new)

    for basin in bas_new:
        basin_fullname = basin_dict(basin)[2]
        macro_name = basin_dict(basin)[1]
        print basin

        link1 = home + "/io/flow/ons_monthly/1981-present/{0}".format(macro)
        arq1 = "{0}/{1}_{2}_ons_obs_19810115_20170615_{3}.nc".format(link1, param, scale, basin_fullname)
        data1 = netCDF4.Dataset(arq1)
        variable1 = data1.variables[param][:].T
        time1 = data1.variables['time']
        obs = variable1[0:360]

        stc1  = obs[0::12]
        stc2  = obs[1::12]
        stc3  = obs[2::12]
        stc4  = obs[3::12]
        stc5  = obs[4::12]
        stc6  = obs[5::12]
        stc7  = obs[6::12]
        stc8  = obs[7::12]
        stc9  = obs[8::12]
        stc10 = obs[9::12]
        stc11 = obs[10::12]
        stc12 = obs[11::12]

        climatology1  = np.nanmean(stc1, axis=0)
        climatology2  = np.nanmean(stc2, axis=0)
        climatology3  = np.nanmean(stc3, axis=0)
        climatology4  = np.nanmean(stc4, axis=0)
        climatology5  = np.nanmean(stc5, axis=0)
        climatology6  = np.nanmean(stc6, axis=0)
        climatology7  = np.nanmean(stc7, axis=0)
        climatology8  = np.nanmean(stc8, axis=0)
        climatology9  = np.nanmean(stc9, axis=0)
        climatology10 = np.nanmean(stc10, axis=0)
        climatology11 = np.nanmean(stc11, axis=0)
        climatology12 = np.nanmean(stc12, axis=0)

        clim_anual = np.array([climatology1, climatology2, climatology3, climatology4, climatology5, climatology6,
                           climatology7, climatology8, climatology9, climatology10, climatology11, climatology12])

        fig = plt.figure(figsize=(40, 20))
        dates = np.arange(1, 12 + 1)
        plt.plot(dates, clim_anual)
        plt.title(u'Clico anual da vazão observada - {0} \n Usina:'
                  u' {1}'.format(period.capitalize(), basin_fullname.capitalize()), fontsize=40, fontweight='bold')
        plt.xlabel(u'Meses', fontsize=40, fontweight='bold')
        plt.ylabel(u'Vazão (m3/s)', fontsize=40, fontweight='bold')

        highest_value = max([max(clim_anual)])
        plt.yticks(np.arange(0, highest_value + 50, highest_value / 10))

        objects = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        plt.xticks(dates, objects, fontsize=40)

        plt.tick_params(axis='both', which='major', labelsize=40, length=5, width=1, pad=5,
                        labelcolor='k')

        path_out = ('/home/leidinice/documentos/results/vazpast/clim_flow/tot/ciclo/{0}/'.format(macro_name))
        if not os.path.exists(path_out):
            create_path(path_out)

        plt.savefig(os.path.join(path_out, 'ciclo_anual_{0}_{1}.png'.format(param, basin_fullname)), dpi=50)
        plt.close('all')
        plt.cla()

