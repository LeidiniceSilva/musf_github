# -*- coding: utf-8 -*-

""" Compute best indices of smap/hymod obs and model flow. """

import os
import glob
import calendar
import netCDF4
import texttable as tt

from pylab import *
from netCDF4 import Dataset
from os.path import expanduser
from dateutil.relativedelta import *
from datetime import datetime, date
from hidropy.utils.hidropy_utils import date2index
from PyFuncemeClimateTools import ClimateStats as cs
from hidropy.utils.all_basins_dict_daily import basinsf

param = 'flow'
scale = 'daily'
model = 'gfs05'
home  = expanduser("~")

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "10/08/2017"
__description__ = "Compute best indices of smap/hymod obs and model flow"


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


def import_model_data(typ, model, mon, basin):

    sim_list = []
    
    for y in range(ihind, fhind + 1):
        ndays = calendar.monthrange(y, mon)[1]

        for d in range(1, ndays + 1):
            target_rundate = date(y, mon, d)
            start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)

            dir_modelname = home + "/io/{0}/{1}_{2}/{3}/{4}/{5}".format(param, type, scale, model, month, macro)

            if model == 'gfs05':
                file_modelname = "{0}/{1}_{2}_{3}_fcst_{4}_{5}_{6}_{7}_{8}." \
                                 "nc".format(dir_modelname, param, scale, model, start_rundate, start_fcstdate,
                                             end_fcstdate, type, basin)
            else:
                file_modelname = "{0}/{1}_{2}_{3}_fcst_{4}_{5}_{6}_{7}_{8}_petclim." \
                                 "nc".format(dir_modelname, param, scale, model, start_rundate, start_fcstdate,
                                             end_fcstdate, type, basin)
            try:
                model = Dataset(os.path.join(dir_modelname, file_modelname))
                var   = model.variables[param][:]
                var   = np.array(var)
                aux   = np.nanmean(var)
            except:
                var   = np.nan

            sim_list.append(aux)
	    
    sim = np.array(sim_list)
    
    return sim


def import_obs_data(typ, period, mon, basin):

    data_base = 'bases_obs'
    dir_obs   = home + "/io/{0}/{1}_{2}/obs/{3}".format(param, type, scale, macro)
    file_obs  = "{0}/{1}_{2}_{3}_{4}_{5}_{6}.nc".format(dir_obs, param, scale, data_base, period, type, basin)

    var = Dataset(os.path.join(dir_obs, file_obs))
    time_var = var.variables['time']

    obs = []
    
    for y in range(ihind, fhind + 1):
        ndays = calendar.monthrange(y, mon)[1]

        for d in range(1, ndays + 1):
            target_rundate = date(y, mon, d)
            start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)

            ifcstdate = datetime.strptime(start_fcstdate, "%Y%m%d")
            ffcstdate = datetime.strptime(end_fcstdate, "%Y%m%d")

            iidx = date2index(date(ifcstdate.year, ifcstdate.month, ifcstdate.day), time_var)
            fidx = date2index(date(ffcstdate.year, ffcstdate.month, ffcstdate.day), time_var)
            aux  = var.variables[param][iidx:fidx + 1]
            obs.append(np.nanmean(aux))

    var.close()
    obs = np.array(obs)
    
    return obs


for mon in range(1, 12 + 1):
    month = datetime(1981, mon, 01).strftime("%b").lower()
    print month

    if model  == 'gfs05':
        ihind = 2009
        fhind = 2016
    else:
        ihind = 2017
        fhind = 2017

    tab = tt.Texttable()
    tab_inform = [[]]

    macros = basinsf(macro=1)
    for macro in macros:

        basins = basinsf(smap=macro)
        print macro

        bas_new1 = []
        for bas1 in basins:
            if 'edgard_de_souza_inc' not in (bas1):
                bas_new1.append(bas1)

        bas_new2 = []
        for bas2 in bas_new1:
            if 'tres_irmaos' not in (bas2):
                bas_new2.append(bas2)

        CORREL  = []
        MBE     = []
        RMSE    = []
        len_bas = len(bas_new2)

        for basin in bas_new2:
            print basin

            typ    = 'smap'
            period = '19810101_20170808'
            model_smap = import_model_data(type, model, mon, basin)
            obs_smap   = import_obs_data(type, period, mon, basin)

            typ    = 'hymod'
            period = '19810101_20170808'
            model_hymod = import_model_data(type, model, mon, basin)
            obs_hymod   = import_obs_data(type, period, mon, basin)

            # print len(model_smap), "smap"
            # print len(obs_smap), "smap"
            # print len(model_hymod), "hymod"
            # print len(obs_hymod), "hymod"

            rmse_smap  = (cs.compute_rmse(np.array(model_smap),  np.array(obs_smap)))
            rmse_hymod = (cs.compute_rmse(np.array(model_hymod), np.array(obs_hymod)))

            corr_smap  = round((np.corrcoef(np.array(model_smap),  np.array(obs_smap)))[0][1], 3)
            corr_hymod = round((np.corrcoef(np.array(model_hymod), np.array(obs_hymod)))[0][1], 3)

            # print rmse_smap
            # print rmse_hymod
            # print
            # print corr_smap
            # print corr_hymod
            # exit()

            rmse_str  = ['MODEL SMAP', 'MODEL HYMOD', 'OBS SMAP', 'OBS HYMOD']
            rmse_list = [rmse_smap, rmse_hymod]

            corr_str  = ['MODEL SMAP', 'MODEL HYMOD', 'OBS SMAP', 'OBS HYMOD']
            corr_list = [corr_smap, corr_hymod]

            best_result_rmse = rmse_str[np.where(rmse_list == np.min(rmse_list))[-1][-1]]
            best_result_corr = corr_str[np.where(corr_list == np.max(corr_list))[-1][-1]]

            tab_inform.append([basin, rmse_smap, rmse_hymod, best_result_rmse, corr_smap, corr_hymod, best_result_corr])

    tab.add_rows(tab_inform)
    tab.set_cols_align(['c', 'c', 'c', 'c', 'c', 'c', 'c'])
    tab.header(['Nome da Usina', 'RMSE SMAP', 'RMSE HYMOD', 'Melhor Indice', 'CORR SMAP', 'CORR HYMOD', 'Melhor Indice'])
    table = str(tab.draw())

    dir_file  = "/home/leidinice/documentos/results/{0}/best_indices/".format(model)
    file_name = '{1}best_rmse_corr_{0}_0916.asc'.format(datetime(1981, month, 01).strftime("%b").lower(), dir_file)
    file_save = open(file_name, 'w')
    file_save.write(table)
    file_save.close()
    print 'next month'
    exit()
