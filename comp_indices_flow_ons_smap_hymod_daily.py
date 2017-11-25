# -*- coding: utf-8 -*-

"""
This script to check correl, bias and rmse indices in the series of ons_obs and obs_bases per basin.
"""
import os
import calendar
import numpy as np

from netCDF4 import Dataset
from datetime import datetime
from os.path import expanduser
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from PyFuncemeClimateTools import ClimateStats as cs
from hidropy.utils.hidropy_utils import create_path
from hidropy.utils.hidropy_utils import date2index
from hidropy.utils.all_basins_dict_daily import basinsf

type  = 'hymod'
param = 'flow'
scale = 'daily'
home  = expanduser("~")

__author__ = 'Leidinice Silva'
__email__  = 'leidinicesilva@gmail.com'
__date__   = '01/08/2017'
__description__ = 'This script to check correl, bias and rmse indices in the series of ons_obs and obs_bases per basin'


def import_hind_obs_ons(mon, basin):

    hind_obs  = '19810101_20151231'
    data_base = 'ons_obs'

    dir_obs_oper = home + "/io/{0}/ons_{1}/1981-present/{2}".format(param, scale, macro)
    file_name    = "{0}/{1}_{2}_{3}_{4}_{5}.nc".format(dir_obs_oper, param, scale, data_base, hind_obs, basin)

    ndays = calendar.monthrange(1981, mon)[1]

    try:
        var = []
        for y in range(1981, 2010 + 1):
            inc = Dataset(file_name)
            time_var = inc.variables['time']
            iidx = date2index(datetime(y, mon, 01), time_var)
            fidx = date2index(datetime(y, mon, ndays), time_var)
            var.append(inc.variables[param][iidx:fidx + 1])
        flag = True
        obs  = np.squeeze(var)
        obs  = np.reshape(obs, obs.shape[0] * obs.shape[1])
        return obs, flag
    except:
        flag = False
        obs  = []
        return obs, flag


def import_hind_obs_bases(mon, basin):

    hind_obs = '19810101_20170811'
    data_base = 'bases_obs'

    dir_obs_oper = home + "/io/{0}/{1}_{2}/obs/{3}".format(param, type, scale, macro)
    file_name = "{0}/{1}_{2}_{3}_{4}_{5}_{6}.nc".format(dir_obs_oper, param, scale, data_base, hind_obs, type,
                                                        basin)
    ndays = calendar.monthrange(1981, mon)[1]

    try:
        var = []
        for y in range(1981, 2010 + 1):
            inc = Dataset(file_name)
            time_var = inc.variables['time']
            iidx = date2index(datetime(y, mon, 01), time_var)
            fidx = date2index(datetime(y, mon, ndays), time_var)
            var.append(inc.variables[param][iidx:fidx + 1])
        flag = True
        obs  = np.squeeze(var)
        obs  = np.reshape(obs, obs.shape[0] * obs.shape[1])
        return obs, flag
    except:
        flag = False
        obs  = []
        return obs, flag


for mon in range(1, 12 + 1):
    month = datetime(1981, mon, 01).strftime("%b").lower()
    print month

    macros = ['amazonas', 'atlantico_leste', 'atlantico_sudeste', 'atlantico_sul', 'doce', 'grande', 'iguacu', 'jacui',
              'paraguai', 'paraiba_do_sul', 'parana', 'paranaiba', 'paranapanema', 'sao_francisco', 'tiete',
              'tocantins', 'uruguai']

    for macro in macros:
        basins = basinsf(hymod=macro)
        print macro

        bas_new1 = []
        for bas1 in basins:
            if 'edgard_de_souza_inc' not in (bas1):
                bas_new1.append(bas1)

        bas_new2 = []
        for bas2 in bas_new1:
            if 'tres_irmaos' not in (bas2):
                bas_new2.append(bas2)

        bas_new3 = []
        for bas3 in bas_new2:
            if 'parnaiba' not in (bas3):
                bas_new3.append(bas3)

        CORREL  = []
        MBE     = []
        RMSE    = []
        len_bas = len(bas_new3)

        for basin in bas_new3:
            print basin

            obs_ons, flag_obs = import_hind_obs_ons(mon, basin)
            obs_bases, flag_bases = import_hind_obs_bases(mon, basin)

            idx_nan = np.where(np.isnan(obs_ons))
            ons     = np.delete(obs_ons, idx_nan)
            bases   = np.delete(obs_bases, idx_nan)

            corr = np.corrcoef(np.squeeze(bases), np.squeeze(ons))
            CORR = np.array([round(corr[0][1], 3)])
            CORREL.append(CORR)

            vies = np.nanmean(np.squeeze(bases) - np.squeeze(ons))
            BIAS = np.array([vies])
            MBE.append(BIAS)

            rmse = cs.compute_rmse(np.squeeze(bases), np.squeeze(ons))
            ERRO = np.array([rmse])
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

        labels  = np.arange(len(basin))
        width_n = 0.8

        fig.suptitle(u'Índices: CORRELAÇÃO, MBE e RMSE \n Obs_ons x Obs_bases - {0} / {1} - 1981_2010 \n Bacia: {2}'
                     .format(type.capitalize(), month.capitalize(), macro.capitalize()), fontsize=250, fontweight='bold')

        a = ax[0].bar(x, CORREL, width_n, color=line_colors, label=basin, align='center', linewidth=20.0)
        highest_correl = max([max(CORREL)])
        ax[0].yaxis.set_ticks(np.arange(-1, highest_correl + 0.1, highest_correl / 5))
        ax[0].axhline(y=0, linewidth=10, color='k')
        ax[0].set_ylabel(u'Correlação', fontsize=250, fontweight='bold')
        ax[0].tick_params(axis='both', which='major', labelbottom='off', labelsize=150, length=20, width=10, pad=20,
                          labelcolor='k')

        b = ax[1].bar(x, MBE, width_n, color=line_colors, label=basin, align='center', linewidth=20.0)
        ax[1].axhline(y=0, linewidth=10, color='k')
        ax[1].set_ylabel(u'MBE', fontsize=250, fontweight='bold')
        ax[1].tick_params(axis='both', which='major', labelbottom='off', labelsize=150, length=20, width=10, pad=20,
                          labelcolor='k')

        c = ax[2].bar(x, RMSE, width_n, color=line_colors, label=basin, align='center', linewidth=20.0)
        ax[2].axhline(y=0, linewidth=10, color='k')
        ax[2].set_ylabel(u'RMSE', fontsize=250, fontweight='bold')
        ax[2].tick_params(axis='both', which='major', labelbottom='off', labelsize=150, length=20, width=10, pad=20,
                          labelcolor='k')
        plt.xlabel(u'Usinas', fontsize=250, fontweight='bold')

        for i in range(len(bas_new3)):
            list_basins.append(bas_new3[i].split('{0}_'.format(macro))[1].capitalize())

        font = FontProperties(weight='bold', size=180)
        plt.figlegend(a, list_basins, loc=8, ncol=6, prop=font)

        path_out = ("/home/leidinice/documentos/results/vazpast/daily/{0}/indices/hind8110/{1}/{2}/".format(type,
                                                                                                            month,
                                                                                                            macro))
        if not os.path.exists(path_out):
            create_path(path_out)

        plt.savefig(os.path.join(path_out, '{0}_indices_{1}_{2}.png'.format(macro, param, month)), dpi=25)
        plt.close('all')
        plt.cla()


