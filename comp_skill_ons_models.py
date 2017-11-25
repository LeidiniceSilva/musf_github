# -*- coding: utf-8 -*-

"""
This code checks skill of model and observed ability
"""

import os
import calendar
import numpy as np

from netCDF4 import Dataset
from datetime import datetime, date
from os.path import expanduser
from dateutil.relativedelta import *
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from PyFuncemeClimateTools import ClimateStats as cs
from hidropy.utils.hidropy_utils import create_path
from hidropy.utils.hidropy_utils import date2index
from hidropy.utils.all_basins_dict_daily import basinsf

typ   = 'hymod'
model = 'gfs05'
param = 'flow'
scale = 'daily'
home  = expanduser("~")

__author__ = 'Leidinice Silva'
__email__  = 'leidinicesilva@gmail.com'
__date__   = '10/08/2017'
__description__ = 'TThis code checks skill of model and observed ability per basin'


def filter_nan(s, o):
    data = np.array([s.flatten(), o.flatten()])
    data = np.transpose(data)
    data = data[~np.isnan(data).any(1)]
    return data[:, 0], data[:, 1]


def nash(s, o):
    s, o = filter_nan(s, o)
    return 1 - sum((s-o)**2)/sum((o-np.mean(o))**2)


def define_dates(target_date):

    if model == 'gfs05':
        target_ifcstdate = target_date + relativedelta(days=1)
        target_efcstdate = target_date + relativedelta(days=7)
    else:
        target_ifcstdate = target_date + relativedelta(days=1)
        target_efcstdate = target_date + relativedelta(days=10)

    start_rundate = '{0}{1:02d}{2:02d}'.format(target_date.year, target_date.month, target_date.day)
    star_fcstdate = '{0}{1:02d}{2:02d}'.format(target_ifcstdate.year, target_ifcstdate.month, target_ifcstdate.day)
    end_fcstdate  = '{0}{1:02d}{2:02d}'.format(target_efcstdate.year, target_efcstdate.month, target_efcstdate.day)
   
   return start_rundate, star_fcstdate, end_fcstdate


def import_model_data(model, basin):

    sim_list = []
    for year in range(ihind, fhind + 1):

        for mon in range(1, 12 + 1):
            month = datetime(1981, mon, 01).strftime("%b").lower()

            c = calendar.TextCalendar(calendar.SUNDAY)
            for i in c.itermonthdays(year, mon):
                if i != 0:
                    day = date(year, mon, i)
                    if day.weekday() == calendar.FRIDAY:

                        date_friday = datetime(year, mon, i)
                        start_rundate, start_fcstdate, end_fcstdate = define_dates(date_friday)

                        dir_modelname = home + "/io/{0}/{1}_{2}/{3}/{4}/{5}".format(param, type, scale, model, month,
                                                                                    macro)

                        if model == 'gfs05':
                            file_modelname = "{0}/{1}_{2}_{3}_fcst_{4}_{5}_{6}_{7}_{8}." \
                                             "nc".format(dir_modelname, param, scale, model, start_rundate,
                                                         start_fcstdate, end_fcstdate, type, basin)
                        else:
                            file_modelname = "{0}/{1}_{2}_{3}_fcst_{4}_{5}_{6}_{7}_{8}_petclim." \
                                             "nc".format(dir_modelname, param, scale, model, start_rundate,
                                                         start_fcstdate, end_fcstdate, type, basin)
                        try:
                            var = Dataset(os.path.join(dir_modelname, file_modelname))
                            var = var.variables[param][:]
                            var = np.array(var)
                            aux = np.nanmean(var)
                        except:
                            aux = np.nan
                        sim_list.append(aux)

    sim = np.array(sim_list)
    return sim


def import_obs_data(basin):

    hind_obs  = '19810101_20170816'
    data_base = 'bases_obs'
    dir_obs   = home + "/io/{0}/{1}_{2}/obs/{3}".format(param, type, scale, macro)
    file_obs  = "{0}/{1}_{2}_{3}_{4}_{5}_{6}.nc".format(dir_obs, param, scale, data_base, hind_obs, type, basin)
    var       = Dataset(os.path.join(dir_obs, file_obs))
    time      = var.variables['time']

    obs = []
    for year in range(ihind, fhind + 1):

        for mon in range(1, 12 + 1):
            c = calendar.TextCalendar(calendar.SUNDAY)

            for i in c.itermonthdays(year, mon):
                if i != 0:
                    day = date(year, mon, i)
                    if day.weekday() == calendar.FRIDAY:  # if its Tuesday or Thursday

                        date_friday = datetime(year, mon, i)
                        start_rundate, start_fcstdate, end_fcstdate = define_dates(date_friday)
                        ifcstdate = datetime.strptime(start_fcstdate, "%Y%m%d")
                        ffcstdate = datetime.strptime(end_fcstdate, "%Y%m%d")

                        iidx = date2index(datetime(ifcstdate.year, ifcstdate.month, ifcstdate.day), time)
                        fidx = date2index(datetime(ffcstdate.year, ffcstdate.month, ffcstdate.day), time)
                        aux  = var.variables[param][iidx:fidx + 1]
                        obs.append(np.nanmean(aux))

    var.close()
    obs = np.array(obs)
    return obs


if model  == 'gfs05':
    ihind = 2009
    fhind = 2016
else:
    ihind = 2017
    fhind = 2017

macros = basinsf(macro=1)
for macro in macros:
    basins = basinsf(micro=macro)
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
        if 'itutinga_inc' not in (bas3):
            bas_new3.append(bas3)

    NS      = []
    MBE     = []
    RMSE    = []
    len_bas = len(bas_new3)

    for basin in bas_new3:
        print basin

        model_data = import_model_data(model, basin)
        obs_data   = import_obs_data(basin)
        # print model_data, len(model_data)
        # print obs_data, len(obs_data)
        # exit()

        indice = nash(np.squeeze(model_data), np.squeeze(obs_data))
        NASH   = np.array([indice])
        NS.append(NASH)

        vies = np.nanmean((model_data) - np.squeeze(obs_data))
        BIAS = np.array([vies])
        MBE.append(BIAS)

        rmse = cs.compute_rmse(np.squeeze(model_data), np.squeeze(obs_data))
        ERRO = np.array([rmse])
        RMSE.append(ERRO)
        # print NS
        # print MBE
        # print RMSE
        # exit()

    list_basins = []
    fig, ax = plt.subplots(3, figsize=(240, 200))
    cmap    = plt.cm.gray
    line_colors = cmap(np.linspace(0, 3))

    x = np.arange(len(NS))
    y = np.arange(len(MBE))
    z = np.arange(len(RMSE))

    labels = np.arange(len(basin))
    width_n = 0.8

    fig.suptitle(u'Índices: NS, MBE e RMSE \n {0} x ONS - {1} / {2}-{3} \n {4}_avg (Sábado - Sexta) Bacia: {5}'
                 .format(model.upper(), type.upper(), ihind, fhind, param.capitalize(), macro.capitalize()),
                 fontsize=250, fontweight='bold')

    a = ax[0].bar(x, NS, width_n, color=line_colors, label=basin, align='center', linewidth=20.0)
    ax[0].set_ylim([-1, 1])
    ax[0].locator_params(nbins=10, axis='y')
    ax[0].axhline(y=0, linewidth=10, color='k')
    ax[0].set_ylabel(u'NS', fontsize=250, fontweight='bold')
    ax[0].tick_params(axis='both', which='major', labelbottom='off', labelsize=200, length=20, width=10, pad=20,
                      labelcolor='k')

    b = ax[1].bar(x, MBE, width_n, color=line_colors, label=basin, align='center', linewidth=20.0)
    ax[1].axhline(y=0, linewidth=10, color='k')
    ax[1].set_ylabel(u'MBE', fontsize=250, fontweight='bold')
    ax[1].tick_params(axis='both', which='major', labelbottom='off', labelsize=200, length=20, width=10, pad=20,
                      labelcolor='k')

    c = ax[2].bar(x, RMSE, width_n, color=line_colors, label=basin, align='center', linewidth=20.0)
    ax[2].axhline(y=0, linewidth=10, color='k')
    ax[2].set_ylabel(u'RMSE', fontsize=250, fontweight='bold')
    ax[2].tick_params(axis='both', which='major', labelbottom='off', labelsize=200, length=20, width=10, pad=20,
                      labelcolor='k')
    plt.xlabel(u'Usinas', fontsize=250, fontweight='bold')

    for i in range(len(bas_new3)):
        list_basins.append(bas_new3[i].split('{0}_'.format(macro))[1].capitalize())

    font = FontProperties(weight='bold', size=180)
    plt.figlegend(a, list_basins, loc=8, ncol=6, prop=font)

    path_out = ("/home/leidinice/documentos/results/{0}/{1}/skill/{2}/{3}/{4}/"
                .format(model, type, scale, param, macro))

    if not os.path.exists(path_out):
        create_path(path_out)

    plt.savefig(os.path.join(path_out, '{0}_indices_{1}_{2}_{3}.png'.format(macro, param, ihind, fhind)), dpi=25)
    plt.close('all')
    plt.cla()
exit()


