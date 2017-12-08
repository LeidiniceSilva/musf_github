# -*- coding: utf-8 -*-

""" This script creates dictionary with information about the best
daily remove bias method per basin. """

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

var_name   = 'pr'
time_freq  = 'daily'
model_name = 'rsm2008'
hind_name  = 'hind8110'
data_base_cal   = 'inmet_ana_chirps_merge'
data_base_ope   = 'inmet_ana_merge'
cal_obs_period = '19610101_20141231'
ope_obs_period = '20150101_*'

HIDROPY_DIR = os.environ['HIDROPY_DIR']

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "10/27/2017"
__description__ = "Create dictionary with information about the best method remove bias of pr_thiessen daily per basin"

    
def define_dates(target_date):
    
    target_ifcstdate = target_date + relativedelta(months=1)
    target_efcstdate = target_date + relativedelta(months=3)

    start_rundate  = '{0}{1:02d}01'.format(target_date.year, target_date.month)
    start_fcstdate = '{0}{1:02d}01'.format(target_ifcstdate.year, target_ifcstdate.month)
    end_fcstdate   = '{0}{1:02d}{2:02d}'.format(target_efcstdate.year, target_efcstdate.month, calendar.monthrange(target_efcstdate.year, target_efcstdate.month)[1])

    return start_rundate, start_fcstdate, end_fcstdate


def import_hind_model_data(model_name, mon, basin):

    hind_cru = []
    for year in range(1981, 2016 + 1):
	
        target_rundate = datetime(year, mon, 01)
        start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)

        dir_modelname  =  "{0}/io/{1}/hind8110/{2}/{3}/{4}_thiessen/{5}/". \
			    format(HIDROPY_DIR, model_name, month, time_freq, var_name, macro)
        file_modelname = "{0}_{1}_{2}_hind8110_fcst_{3}_{4}_{5}_thiessen_{6}.nc". \
			    format(var_name, time_freq, model_name, start_rundate, start_fcstdate, 
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
	
        dir_modelname  =  "{0}/io/{1}/hind8110/{2}/{3}/{4}_thiessen_cor/{5}/". \
		            format(HIDROPY_DIR, model_name, month, time_freq, var_name, macro)
			
        file_modelname = "{0}_{1}_{2}_hind8110_fcst_{3}_{4}_{5}_thiessen_{6}{7}.nc". \
			   format(var_name, time_freq, model_name, start_rundate, start_fcstdate,
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
        str_mon, start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)
        firt_mon_sim = calendar.monthrange(year, int(str_mon))[1]
	
	# calibration period 
        file_name_cal = '{0}/io/inmet_ana_chirps_merge/calibration/{1}/' \
			'{2}_thiessen/{3}/{2}_{1}_{4}_obs_{5}_thiessen_{6}.nc' \
			.format(HIDROPY_DIR, time_freq, var_name, macro, data_base_cal,
			cal_obs_period, basin)
			
    	# operation period 
	file_name_ope = lsname('{0}/io/inmet_ana_merge/operation/{1}/' \
			'{2}_thiessen/{3}/{2}_{1}_{4}_obs_{5}_thiessen_{6}.nc' \
			.format(HIDROPY_DIR, time_freq, var_name, macro, data_base_ope,
			ope_obs_period, basin))
					
	ons_nc1 = Dataset(file_name_cal)
	ons_nc2 = Dataset(file_name_ope)

	ons1 = ons_nc1.variables[var_name][:] 
	ons2 = ons_nc2.variables[var_name][:]

	ons = np.concatenate((ons1, ons2), axis=0)

	date_start = os.path.basename(file_name_cal).split('_')[7]
	date_end   = os.path.basename(file_name_ope).split('_')[7]
	i1, i2 = index_between_dates(date_start, date_end, start_fcstdate, end_fcstdate, 'days')
			     
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
	
    for basin in basins:
        print 'Processing micro: {0}'.format(basin)
   
        months = np.arange(1, 12 + 1)
        month_list = []
		
        for mon in months:
            month = dic_month[mon]
            print "Run dict for Model and Date: {0} - {1}".format(model_name.upper(), month.upper())
	    	    
            list_cru = import_hind_model_data(model_name, mon, basin)
	    conc_cru = np.concatenate(list_cru, axis=0)
	    
            method = '_cor'
            list_cor_eqmdes = import_hind_model_data_cor(model_name, mon, basin, method)
	    conc_cor_eqmdes = np.concatenate(list_cor_eqmdes, axis=0)
	    
            list_obs = import_hind_obs_data(model_name, mon, basin)
	    conc_obs = np.concatenate(list_obs, axis=0)
	        
            rmse_crude      = cs.compute_rmse(conc_cru, conc_obs)
            rmse_cor_eqmdes = cs.compute_rmse(conc_cor_eqmdes, conc_obs)
 
	    rmse_str    = ['crude', 'cor_eqmdes']
	    rmse_list   = [rmse_crude, rmse_cor_eqmdes]
	    best_result = rmse_str[np.where(rmse_list == np.min(rmse_list))[-1][-1]]
	    month_list.append(best_result)
	monthly_dict[basin] = month_list
 
file_name = 'basins_remove_bias_pr_{0}_all_methods_daily.py'.format(model_name)
file_save = open(file_name, 'w')
file_save.write('dict_remove_bias_{0}='.format(model_name) + str(monthly_dict))
file_save.close()
print 'finish'
