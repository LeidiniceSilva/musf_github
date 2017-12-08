# -*- coding: utf-8 -*-

""" This script creates dictionary with information about the best
monthly remove bias method per basin. """

import os
import netCDF4

from pylab import *
from netCDF4 import Dataset
from dateutil.relativedelta import *
from datetime import datetime, date
from hidropy.utils.hidropy_utils import date2index
from PyFuncemeClimateTools import ClimateStats as cs
from hidropy.utils.hidropy_utils import create_path, lsname
from hidropy.utils.all_basins_dict_monthly import basinsf
from os.path import expanduser

typ   = 'smap'
param = 'flow'
scale = 'monthly'
home  = expanduser("~")

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "26/09/2017"
__description__ = "Create dictionary with information about the best method remove bias of flow monthly per basin"


def define_dates(target_date):

    target_ifcstdate = target_date + relativedelta(months=1)
    target_efcstdate = target_date + relativedelta(months=3)

    ini_rundate   = '{0}{1:02d}{2:02d}'.format(target_date.year,      target_date.month,      target_date.day)
    star_fcstdate = '{0}{1:02d}{2:02d}'.format(target_ifcstdate.year, target_ifcstdate.month, 15)
    end_fcstdate  = '{0}{1:02d}{2:02d}'.format(target_efcstdate.year, target_efcstdate.month, 15)
    
    return ini_rundate, star_fcstdate, end_fcstdate


def import_model_data(model, mon, basin):

    if model == 'echam46':
        dir_model = home + "/io/{0}/{1}_{2}/{3}/{4}/{5}".format(param, typ, scale, model, month, macro)
    else:
        dir_model = home +"/io/{0}/{1}_{2}/nmme/{3}/{4}/{5}".format(param, typ, scale, model, month, macro)

    clim_list = []
    date_list = []
    
    for year in range(1982, 2016+1):
	
        target_rundate = date(year, mon, 01)
        ini_rundate, star_fcstdate, end_fcstdate = define_dates(target_rundate)
	
        if model       == 'echam46':
	    period     = 'hind8110'
            file_model = "{0}/flow_monthly_{1}_{2}_fcst_{3}_{4}_{5}_smap_{6}." \
                         "nc".format(dir_model, model, period, ini_rundate, star_fcstdate, end_fcstdate, basin)
        else:
	    period     = 'hind8210'
            file_model = "{0}/flow_monthly_{1}_{2}_fcst_{3}_{4}_{5}_smap_{6}_petclim." \
                         "nc".format(dir_model, model, period, ini_rundate, star_fcstdate, end_fcstdate, basin)
	try:
	    input_data = Dataset(os.path.join(dir_model, file_model))
	    var        = input_data.variables[param][:]
	    
	    if ma.count_masked(var) == 0:
		var = np.nanmean(var)
	    else:
		var = np.nan
		date_list.append(target_rundate)
	    input_data.close()
	    
	except:
	    print 'Hindcast File: {0} is not available'.format(os.path.join(dir_model, file_model))
            var = np.nan
	    date_list.append(target_rundate)
	clim_list.append(np.nanmean(var))
    
    clim = np.asarray(clim_list)
    clim = clim[~np.isnan(clim)]

    return clim, date_list
		

def import_model_data_cor(model, mon, basin, method):

    if model == 'echam46':
        dir_model = home + "/io/{0}/{1}_{2}{3}/{4}/{5}/{6}".format(param, typ, scale, method, model, month, macro)
    else:
        dir_model = home + "/io/{0}/{1}_{2}{3}/nmme/{4}/{5}/{6}".format(param, typ, scale, method, model, month, macro)

    clim_list = []
    date_list = []
    
    for year in range(1982, 2016+1):
	
        target_rundate = date(year, mon, 01)
        ini_rundate, star_fcstdate, end_fcstdate = define_dates(target_rundate)
	
	if model       == 'echam46':
	    period     = 'hind8110'
	    file_model = "{0}/flow_monthly_{1}_{2}_fcst_{3}_{4}_{5}_smap_{6}{7}."\
		         "nc".format(dir_model, model, period, ini_rundate, star_fcstdate, end_fcstdate, basin, method)
	else:
	    period     = 'hind8210'
            file_model = "{0}/flow_monthly_{1}_{2}_fcst_{3}_{4}_{5}_smap_{6}{7}_petclim." \
                         "nc".format(dir_model, model, period, ini_rundate, star_fcstdate, end_fcstdate, basin, method)	
	try:
	    input_data = Dataset(os.path.join(dir_model, file_model))
	    var        = input_data.variables[param][:]
	    
	    if ma.count_masked(var) == 0:
		var = np.nanmean(var)
	    else:
		var = np.nan
		date_list.append(target_rundate)
	    input_data.close()
	    
	except:
	    print 'Hindcast File: {0} is not available'.format(os.path.join(dir_model, file_model))
            var = np.nan
	    date_list.append(target_rundate)
	clim_list.append(np.nanmean(var))
    
    clim_cor = np.array(clim_list)
    clim_cor = clim_cor[~np.isnan(clim_cor)]
       
    return clim_cor, date_list


def import_obs_data(mon, basin, date_list):

    dir_obs  = home + "/io/{0}/ons_{1}/1981-present/{2}".format(param, scale, macro)
    file_obs = lsname("{0}/{1}_{2}_ons_obs_19810115_*_{3}.nc".format(dir_obs, param, scale, basin))
    var      = netCDF4.Dataset(file_obs)
    time     = var.variables['time']
    
    ons_obs = []

    for year in range(1982, 2016+1):
	
        target_rundate = date(year, mon, 01)
	
	if not target_rundate in date_list:
	    
	    ini_rundate, star_fcstdate, end_fcstdate = define_dates(target_rundate)
	
	    ifcstdate = datetime.strptime(star_fcstdate, "%Y%m%d")
	    ffcstdate = datetime.strptime(end_fcstdate,  "%Y%m%d")

	    iidx = date2index(datetime(ifcstdate.year, ifcstdate.month, ifcstdate.day), time)
	    fidx = date2index(datetime(ffcstdate.year, ffcstdate.month, ffcstdate.day), time)
	    aux  = var.variables[param][iidx:fidx + 1]
	    ons_obs.append(np.nanmean(aux))

	else:
	    print "Model data for {0} does not exist.".format(target_rundate)
	    continue
	        
    var.close()
    obs  = np.array(ons_obs)   
    
    return obs


monthly_dict = {}

dic_month = { 1: 'jan', 2: 'feb', 3: 'mar',  4: 'apr',  5: 'may',  6: 'jun', 
	      7: 'jul', 8: 'aug', 9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec' }
	      
list_model = ['echam46', 'cmc1-cancm3', 'cmc2-cancm4', 'cola-rsmas-ccsm3', 'cola-rsmas-ccsm4', 
	      'gfdl-cm2p5-flor-b01',  'nasa-gmao-062012', 'ncep-cfsv2']

macros = basinsf(macro=1)

for model in list_model:
    print 'Model:', model
    
    for macro in macros:
	print 'Macro:', macro

	basins = basinsf(smap=macro)
	
	for basin in basins:
	    print 'Micro:', basin

	    months = np.arange(1, 12 + 1)
	    month_list = []
	    
	    for mon in months:
		month = dic_month[mon]
		print 'Month:', month

		hind_cru = import_model_data(model, mon, basin)[0]
		
		method = '_cor_flow'
		hind_cor_flow, date_list = import_model_data_cor(model, mon, basin, method)
		
		method = '_cor_pr'
		hind_cor_pr, date_list = import_model_data_cor(model, mon, basin, method)
		
		method = '_cor_pr_flow'
		hind_cor_flow_pr, date_list = import_model_data_cor(model, mon, basin, method)
		
		obs = import_obs_data(mon, basin, date_list)

		rmse_crude       = cs.compute_rmse(hind_cru,         obs)
		rmse_cor_flow    = cs.compute_rmse(hind_cor_flow,    obs)
		rmse_cor_pr      = cs.compute_rmse(hind_cor_pr,      obs)
		rmse_cor_pr_flow = cs.compute_rmse(hind_cor_flow_pr, obs)

		rmse_str    = ['crude', 'cor_flow', 'cor_pr', 'cor_pr_flow']
		rmse_list   = [rmse_crude, rmse_cor_flow, rmse_cor_pr, rmse_cor_pr_flow]
		best_result = rmse_str[np.where(rmse_list == np.min(rmse_list))[-1][-1]]
		month_list.append(best_result)
	    monthly_dict[basin] = month_list

    file_name = 'dict_monthly_hind8216_best_remove_bias_method_{0}.py'.format(model)
    file_save = open(file_name, 'w')
    file_save.write('dict_remove_bias_{0}='.format(model) + str(monthly_dict))
    file_save.close()
    print 'finish'
