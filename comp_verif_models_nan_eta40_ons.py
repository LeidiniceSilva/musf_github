# -*- coding: utf-8 -*-

"""
This script to check nan and negative values in the series of models per basin.
"""

import os
import calendar
import numpy as np
import texttable as tt

from netCDF4 import Dataset
from datetime import datetime
from os.path import expanduser
from dateutil.relativedelta import *
from hidropy.utils.hidropy_utils import date2index, basin_dict

typ   = 'hymod'
model = 'eta40'
param = 'flow'
scale = 'daily'
home  = expanduser("~")

__author__ = 'Leidinice Silva'
__email__  = 'leidinicesilva@gmail.com'
__date__   = '01/08/2017'
__description__ = 'This script to check nan and negative values in the series of models per basin'


def define_dates(target_date):

    target_ifcstdate = target_date + relativedelta(days=1)
    target_efcstdate = target_date + relativedelta(days=10)

    start_rundate = '{0}{1:02d}{2:02d}'.format(target_date.year, target_date.month, target_date.day)
    star_fcstdate = '{0}{1:02d}{2:02d}'.format(target_ifcstdate.year, target_ifcstdate.month, target_ifcstdate.day)
    end_fcstdate  = '{0}{1:02d}{2:02d}'.format(target_efcstdate.year, target_efcstdate.month, target_efcstdate.day)

    return start_rundate, star_fcstdate, end_fcstdate


def import_model_data(model_name, target_date, basin):

    start_rundate, star_fcstdate, end_fcstdate = define_dates(target_date)
    basin_fullname = basin_dict(basin)[2]
    basin_name     = basin_dict(basin)[1]

    dir_modelname  = home + "/io/flow/{0}_{1}/{2}/{3}/{4}".format(type, scale, model_name, month, basin_name)
    file_modelname = "{0}/{1}_{2}_{3}_fcst_{4}_{5}_{6}_{7}_{8}_petclim." \
                     "nc".format(dir_modelname, param, scale, model_name, start_rundate, star_fcstdate, end_fcstdate,
                                 type, basin_fullname)
    try:
        input_data = Dataset(os.path.join(dir_modelname, file_modelname))
        var = input_data.variables[param][:]
        input_data.close()
        flag = True
    except:
        var  = []
        flag = False

    return var, flag, file_modelname


def import_obs_data(month, basin):

    basin_fullname = basin_dict(basin)[2]
    basin_name     = basin_dict(basin)[1]
    hind_obs  = '19810101_20151231'
    data_base = 'ons_obs'

    dir_obs   = home + "/io/{0}/ons_{1}/1981-present/{2}".format(param, scale, basin_name)
    file_name = "{0}/{1}_{2}_{3}_{4}_{5}.nc".format(dir_obs, param, scale, data_base, hind_obs, basin_fullname)
    ndays     = calendar.monthrange(1981, month)[1]

    try:
        var = []
        for y in range(1981, 2010 + 1):
            inc = Dataset(file_name)
            time_var = inc.variables['time']
            iidx = date2index(datetime(y, month, 01), time_var)
            fidx = date2index(datetime(y, month, ndays), time_var)
            var.append(inc.variables[param][iidx:fidx + 1])
        flag = True
        obs  = np.squeeze(var)
        obs  = np.reshape(obs, obs.shape[0] * obs.shape[1])
        obs  = np.delete(obs, np.where(obs == -999.))
        return obs, flag
    except:
        flag = False
        obs  = []
        return obs, flag


macros = ['amazonas', 'atlantico_leste', 'atlantico_sudeste', 'atlantico_sul', 'doce', 'grande', 'iguacu', 'jacui',
          'paraguai', 'paraiba_do_sul', 'parana', 'paranaiba', 'paranapanema', 'parnaiba', 'sao_francisco',
          'tiete', 'tocantins', 'uruguai']

for macro in macros:
    basins = sorted(basin_dict(micro=True, basin_name=macro))
    print macro.upper()

    tab = tt.Texttable()
    tab_inform = [[]]

    for basin in basins:
        print basin

        basin_fullname = basin_dict(basin)[2]
        basin_name     = basin_dict(basin)[1]

        for mon in range(8, 12 + 1):
            month = datetime(2017, mon, 01).strftime("%b").lower()
            obs_data, flag_obs = import_obs_data(mon, basin)

            for year in range(2016, 2016 + 1):
                ndays = calendar.monthrange(year, mon)[1]

                for day in range(1, ndays + 1):
                    target_rundate = datetime(year, mon, day)
                    model_data, flag_model, file_modelname = import_model_data(model, target_rundate, basin)

                    if flag_model:

                        idxs_lqzero = np.where(model_data < 0)[0]
                        idxs_nan    = np.where(np.isnan(model_data))[0]

                        if (len(idxs_lqzero) > 0) or len(idxs_nan > 0):
                            print file_modelname
                            print model_data

                        if flag_obs:
                            obs_extreme = 2 * (np.nanmax(obs_data))
                            idxs_max    = np.where(model_data > obs_extreme)[0]

                            if (len(idxs_max) > 0):
                                print np.nanmax(obs_data)
                                print file_modelname
                                print model_data

                                tab_inform.append([year, np.nanmax(obs_data), file_modelname, model_data])

    tab.add_rows(tab_inform)
    tab.set_cols_align(['c', 'c', 'c', 'c'])
    tab.header(['Ano', 'Obs data max', 'Arquivo', 'Valor'])
    table = str(tab.draw())

    dir_file  = "/home/leidinice/documentos/results/eta40/{0}/extremes_values/".format(type)
    file_name = '{0}extremes_values_1616_aug_dec_{1}.asc'.format(dir_file, macro)
    file_save = open(file_name, 'w')
    file_save.write(table)
    file_save.close()
