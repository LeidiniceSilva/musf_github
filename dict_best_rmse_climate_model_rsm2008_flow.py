# -*- coding: utf-8 -*-

""" This script creates dictionary with information about the best
monthly remove bias method per basin. """

import os
import argparse
import calendar
import numpy as np
import numpy.ma as ma

from pylab import *
from netCDF4 import Dataset
from collections import Counter
from dateutil.relativedelta import *
from datetime import datetime, date
from hidropy.utils.hidropy_utils import lsname
from hidropy.utils.all_basins_dict_monthly import basinsf

from PyFuncemeClimateTools.DefineDates import index_between_dates
from PyFuncemeClimateTools import ClimateStats as cs

from os.path import expanduser

var_name   = 'flow'
time_freq  = 'monthly'
model_name = 'rsm2008'
hind_name  = 'hind8110'
obs_base   = 'ons_obs'
obs_period = '19810115_*'

HIDROPY_DIR = os.environ['HIDROPY_DIR']
 
__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "29/11/2017"
__description__ = "Create dictionary with information about the best method remove bias of flow monthly per basin"


def define_dates(target_date):
    
    target_ifcstdate = target_date + relativedelta(months=1)
    target_efcstdate = target_date + relativedelta(months=3)

    start_rundate  = '{0}{1:02d}01'.format(target_date.year, target_date.month)
    start_fcstdate = '{0}{1:02d}15'.format(target_ifcstdate.year, target_ifcstdate.month)
    end_fcstdate   = '{0}{1:02d}15'.format(target_efcstdate.year, target_efcstdate.month)

    return start_rundate, start_fcstdate, end_fcstdate


def import_hind_model_data(model_name, mon, basin):

    hind_cru = []
    for year in range(1981, 2016 + 1):
	
        target_rundate = datetime(year, mon, 01)
        start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)

	dir_modelname  = "{0}/io/{1}/smap_monthly/{2}/{3}/{4}/". \
			 format(HIDROPY_DIR, var_name, model_name, month, macro)
        file_modelname = "{0}_{1}_{2}_{3}_fcst_{4}_{5}_{6}_smap_{7}.nc". \
			 format(var_name, time_freq, model_name, hind_name, start_rundate, start_fcstdate,
			 end_fcstdate, basin)  
        try:        
            input_data = Dataset(os.path.join(dir_modelname, file_modelname))
            hind = input_data.variables[var_name][:]
            hind_cru.append(hind)
        except:
            print 'Hindcast File: {0} is not available'.format(os.path.join(dir_modelname, file_modelname))
            hind_cru = np.nan
    
    input_data.close()
    hind_cru = np.squeeze(hind_cru)
    
    return hind_cru
    

def import_hind_model_data_cor(model_name, mon, basin, method):

    hind_cor = []
    for year in range(1981, 2016 + 1):
	
        target_rundate = datetime(year, mon, 01)
        start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)
	
	dir_modelname  = "{0}/io/{1}/smap_monthly{2}/{3}/{4}/{5}/". \
			 format(HIDROPY_DIR, var_name, method, model_name, month, macro)
        file_modelname = "{0}_{1}_{2}_{3}_fcst_{4}_{5}_{6}_smap_{7}{8}.nc". \
			 format(var_name, time_freq, model_name, hind_name, start_rundate, start_fcstdate,
			 end_fcstdate, basin, method)
        try:
            input_data = Dataset(os.path.join(dir_modelname, file_modelname))
            hind = input_data.variables[var_name][:]
            hind_cor.append(hind)
        except:
            print 'Hindcast File: {0} is not available'.format(os.path.join(dir_modelname, file_modelname))
            hind_cor = np.nan
    
    input_data.close()
    hind_cor = np.squeeze(hind_cor)

    return hind_cor


def import_hind_obs_data(model_name, mon, basin):
   
    obs = []
    for year in range(1981, 2016 + 1):
	
	target_rundate = datetime(year, mon, 01)
        start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)
		
	file_obs  = lsname("{0}/io/{1}/ons_monthly/1981-present/{2}/flow_{3}_{4}_{5}_{6}.nc". \
		    format(HIDROPY_DIR, var_name, macro, time_freq, obs_base, obs_period, basin))

	ons_nc = Dataset(file_obs)
	ons = ons_nc.variables[var_name][:]
	
	date_start = os.path.basename(file_obs).split('_')[4]
	date_end   = os.path.basename(file_obs).split('_')[5]
	i1, i2 = index_between_dates(date_start, date_end, start_fcstdate, end_fcstdate, 'months')
			     
        aux = ons[i1:i2+1]
        obs.append(aux)

    obs = np.squeeze(obs)

    return obs


monthly_dict = {}

dic_month = { 1: 'jan', 2: 'feb', 3: 'mar',  4: 'apr',  5: 'may',  6: 'jun', 
	      7: 'jul', 8: 'aug', 9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec' }
	      
macros = basinsf(macro=1)
    
for macro in macros:
    print 'Processing macro: {0}'.format(macro)
    
    basins = basinsf(smap=macro)
    
    bas_new1 = []
    for bas1 in basins:
        if '_colider_inc' not in (bas1):
            bas_new1.append(bas1)

    bas_new2 = []
    for bas2 in bas_new1:
        if '_billings' not in (bas2):
            bas_new2.append(bas2)
    
    bas_new3 = []
    for bas3 in bas_new2:
        if '_salto_santiago' not in (bas3):
            bas_new3.append(bas3)

    bas_new4 = []
    for bas4 in bas_new3:
        if '_segredo' not in (bas4):
            bas_new4.append(bas4)
	    	
    for basin in bas_new4:
        print 'Processing micro: {0}'.format(basin)
   
        months = np.arange(1, 12 + 1)
        month_list = []
		
        for mon in months:
            month = dic_month[mon]
            print "Run dict for Model and Date: {0} - {1}".format(model_name.upper(), month.upper())
	    
	    list_cru = import_hind_model_data(model_name, mon, basin)
	    conc_cru = np.concatenate(list_cru, axis=0)
	    
	    method = '_cor_flow'
            list_cor_flow = import_hind_model_data_cor(model_name, mon, basin, method)
	    conc_cor_flow = np.concatenate(list_cor_flow, axis=0)
	    
	    method = '_cor_pr'
            list_cor_pr = import_hind_model_data_cor(model_name, mon, basin, method)
	    conc_cor_pr = np.concatenate(list_cor_pr, axis=0)
	    
	    method = '_cor_pr_flow'
            list_cor_pr_flow = import_hind_model_data_cor(model_name, mon, basin, method)
	    conc_cor_pr_flow = np.concatenate(list_cor_pr_flow, axis=0)
	    
            list_obs = import_hind_obs_data(model_name, mon, basin)
	    conc_obs = np.concatenate(list_obs, axis=0)
	    
	    rmse_crude       = cs.compute_rmse(conc_cru,         conc_obs)
	    rmse_cor_flow    = cs.compute_rmse(conc_cor_flow,    conc_obs)
	    rmse_cor_pr      = cs.compute_rmse(conc_cor_pr,      conc_obs)
	    rmse_cor_pr_flow = cs.compute_rmse(conc_cor_pr_flow, conc_obs)

	    rmse_str    = ['crude', 'cor_flow', 'cor_pr', 'cor_pr_flow']
	    rmse_list   = [rmse_crude, rmse_cor_flow, rmse_cor_pr, rmse_cor_pr_flow]
	    best_result = rmse_str[np.where(rmse_list == np.min(rmse_list))[-1][-1]]
	    month_list.append(best_result)
	monthly_dict[basin] = month_list

file_name = 'basins_remove_bias_flow_{0}_all_methods_monthly.py'.format(model_name)
file_save = open(file_name, 'w')
file_save.write('dict_remove_bias_{0}='.format(model_name) + str(monthly_dict))
file_save.close()
print 'finish'
