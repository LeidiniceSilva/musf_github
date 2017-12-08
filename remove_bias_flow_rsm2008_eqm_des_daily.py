# -*- coding: utf-8 -*-

"""
This script remove daily mean flow bias from RSM2008
model. This script focus on operational period and creates files in
the same flow pattern.
"""
    
import os
import glob
import argparse
import bisect
import calendar
import numpy as np
import numpy.ma as ma
import scipy.stats as ss

from netCDF4 import Dataset
from collections import Counter
from dateutil.relativedelta import *
from datetime import datetime, date
from hidropy.utils.hidropy_utils import date2index, basin_dict
from hidropy.utils.write_flow import write_flow

from os.path import expanduser

HIDROPY_DIR = os.environ['HIDROPY_DIR']
    
__author__ = 'Leidinice Silva'
__email__ = 'leidinice.silva@funceme.br'
__date__ = '11/08/2017'
__description__='This script remove daily mean flow bias from RSM2008' \
                ' model. This script focus on operational' \
                ' period and creates files in the same flow pattern.'


def arguments():
    global args

    parser = argparse.ArgumentParser(description=__description__,
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--month_target', default='', 
                        help='Insert initial forecast month.')
    parser.add_argument('--year_target', default='', 
                        help='Insert initial forecast year.')
    parser.add_argument('--local_dir', default='/io',
                        help='Path to data directory.')
    parser.add_argument('--model_name', choices=['rsm2008'],
                        type=str, nargs='?', help='Model option.')
    parser.add_argument('--hydro_model', choices=['hymod', 'smap', 'all'],
                        type=str, nargs='?', help='Hidrologicals models options.')
    parser.add_argument('--basin', help='Name of input basin.', default='')
    parser.add_argument('--macro', action='store_true',
                        help='Compute flow for all macro-basins.')
    parser.add_argument('--micro', action='store_true',
                        help='Compute flow for all micro-basins of '
                             'input basin.')
    parser.add_argument('--all_basins', action='store_true',
                        help='True to compute flow for all macro-basins'
                             ' and micro-basins.')
    args = parser.parse_args()

    return args


def define_initial_parameters(hydromodel):
    """ Define target data and models list.

    :param: modelname: str
    :return: target_date: datatime
    :return: model name list: list
    """

    # List Models
    if hydromodel  == 'all':
        list_model = ['hymod', 'smap']
    else:
        list_model = [hydromodel]

    if not month:
        target_date = datetime(date.today().year, date.today().month, 01) 
    else:
        target_date = datetime(int(year), int(month),  01)

    return target_date, list_model    
   
   
def define_dates(target_date):
    """ Define date start run, and dates that the forecast starts and ends.

    :param: target_date: datatime
    :return: start_rundate: str
    :return: start_fcstdate: str
    :return: end_fcstdate: str
    """    
    
    str_mon = target_date.strftime("%b").lower()

    target_ifcstdate = target_date + relativedelta(months=1)
    target_mfcstdate = target_date + relativedelta(months=2)
    target_efcstdate = target_date + relativedelta(months=3)
    
    fcst_yea1 = target_ifcstdate.strftime("%Y")
    fcst_yea2 = target_mfcstdate.strftime("%Y")
    fcst_yea3 = target_efcstdate.strftime("%Y")

    fcst_mon1 = target_ifcstdate.strftime("%m")
    fcst_mon2 = target_mfcstdate.strftime("%m")
    fcst_mon3 = target_efcstdate.strftime("%m")

    start_rundate  = '{0}{1:02d}01'.format(target_date.year, target_date.month)
    start_fcstdate = '{0}{1:02d}01'.format(target_ifcstdate.year, target_ifcstdate.month)
    end_fcstdate   = '{0}{1:02d}{2:02d}'.format(target_efcstdate.year, target_efcstdate.month,
		      calendar.monthrange(target_efcstdate.year, target_efcstdate.month)[1])
    
    return fcst_yea1, fcst_yea2, fcst_yea3, str_mon, fcst_mon1, fcst_mon2, fcst_mon3, start_rundate, start_fcstdate, end_fcstdate


def import_fcst_model_data(model_name, hydro_model, target_date, basin):
    """ Import fcst model data.

    :param: model_name: str (rsm2008)
    :param: target_date: datetime
    :param: basin: str
    :return: flow time serie
    :return: flag that it refers to data control
    :rtype:list
    """

    fcst_yea1, fcst_yea2, fcst_yea3, str_mon, fcst_mon1, fcst_mon2, fcst_mon3, start_rundate, start_fcstdate, end_fcstdate = define_dates(target_date)

    firt_mon = calendar.monthrange(int(fcst_yea1), int(fcst_mon1))[1]
    seco_mon = calendar.monthrange(int(fcst_yea2), int(fcst_mon2))[1]
    thir_mon = calendar.monthrange(int(fcst_yea3), int(fcst_mon3))[1]
    
    basin_full_name = basin_dict(basin)[2]
    basin_name = basin_dict(basin)[1]
    
    dir_modelname   =  "{0}{1}/{2}/{3}_{4}_bkp/{5}/{6}/{7}/". \
		       format(HIDROPY_DIR, localdir, var_name, hydro_model, time_freq,
		       model_name, str_mon, basin_name)
		       
    file_modelname  = "{0}_{1}_{2}_hind8110_fcst_{3}_{4}_{5}_{6}_{7}.nc". \
		       format(var_name, time_freq, model_name, start_rundate, start_fcstdate,
		       end_fcstdate, hydro_model, basin_full_name)
    try:
	input_data = Dataset(os.path.join(dir_modelname, file_modelname))
	var = input_data.variables[var_name][:]

	var1 = np.copy(var[0:firt_mon])
	var2 = np.copy(var[firt_mon:firt_mon+seco_mon])
	var3 = np.copy(var[firt_mon+seco_mon:firt_mon+seco_mon+thir_mon])
	input_data.close()
	flag = True
	
    except:
	print 'File: {0} is not available'.format(os.path.join(dir_modelname, file_modelname))
	var1 = []
	var2 = []
	var3 = []
	flag = False
    
    fcst1 = np.array(var1)
    fcst2 = np.array(var2)
    fcst3 = np.array(var3)
    print 

    return fcst1, fcst2, fcst3, firt_mon, seco_mon, thir_mon, flag


def import_hind_model_data(model_name, hydro_model, target_date, basin):
    """ Import fcst model data.

        :param: model_name: str ('RSM2008')
        :param: target_date: datetime
        :param: basin: str
        :return: flow time serie
        :rtype: list
        """
    hind_clim1 = []
    hind_clim2 = []
    hind_clim3 = []
    
    ihind = 1981
    year_list = np.arange(ihind, 2010 + 1)
    
    for ii, y in enumerate(year_list):
	
	target_rundate = datetime(y, target_date.month, 01)
	fcst_yea1, fcst_yea2, fcst_yea3, str_mon, fcst_mon1, fcst_mon2, fcst_mon3, start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)
	
	firt_mon = calendar.monthrange(int(fcst_yea1), int(fcst_mon1))[1]
	seco_mon = calendar.monthrange(int(fcst_yea2), int(fcst_mon2))[1]
	thir_mon = calendar.monthrange(int(fcst_yea3), int(fcst_mon3))[1]
	
	basin_full_name = basin_dict(basin)[2]
        basin_name = basin_dict(basin)[1]

	dir_modelname   =  "{0}{1}/{2}/{3}_{4}_bkp/{5}/{6}/{7}/". \
			   format(HIDROPY_DIR, localdir, var_name, hydro_model, time_freq,
			   model_name, str_mon, basin_name)
			
	file_modelname  = "{0}_{1}_{2}_hind8110_fcst_{3}_{4}_{5}_{6}_{7}.nc". \
			   format(var_name, time_freq, model_name, start_rundate, start_fcstdate,
			   end_fcstdate, hydro_model, basin_full_name)
	try:
	    input_data = Dataset(os.path.join(dir_modelname, file_modelname))
	    hind = input_data.variables[var_name][:]
	    
	    hind_clim1.append(np.nansum(hind[0:firt_mon]))
	    hind_clim2.append(np.nansum(hind[firt_mon:firt_mon+seco_mon]))
	    hind_clim3.append(np.nansum(hind[firt_mon+seco_mon:firt_mon+seco_mon+thir_mon]))
	    
	except:
	    print 'Hindcast File: {0} is not available'.format(os.path.join(dir_modelname, file_modelname))
	    hind_clim1 = np.nan
    	    hind_clim2 = np.nan
	    hind_clim3 = np.nan
    
    input_data.close()
    clim_model1 = np.squeeze(hind_clim1)
    clim_model2 = np.squeeze(hind_clim2)
    clim_model3 = np.squeeze(hind_clim3)

    return clim_model1, clim_model2, clim_model3


def import_hind_obs_data(model_name, target_date, basin):
    """ Import obs data.

    :param: model_name: str (rsm2008')
    :param: target_date: datetime
    :param: basin: str
    :return: flow time serie
    """
    
    hind_obs1 = []
    hind_obs2 = []
    hind_obs3 = []
    
    for y in range(1981, 2010 + 1):
	
	target_rundate = datetime(y, target_date.month, 01)
	fcst_yea1, fcst_yea2, fcst_yea3, str_mon, fcst_mon1, fcst_mon2, fcst_mon3, start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)
	
	firt_mon = calendar.monthrange(int(fcst_yea1), int(fcst_mon1))[1]
	seco_mon = calendar.monthrange(int(fcst_yea2), int(fcst_mon2))[1]
	thir_mon = calendar.monthrange(int(fcst_yea3), int(fcst_mon3))[1]
		    
	basin_full_name = basin_dict(basin)[2]
	basin_name = basin_dict(basin)[1]
	
	file_name = '{0}{1}/{2}/ons_daily/1981-present/{3}/' \
		    '{2}_{4}_{5}_{6}_{7}.nc' \
		    .format(HIDROPY_DIR, localdir, var_name, basin_name, time_freq,
		     data_base, hind_obs_period, basin_full_name)
		     
	inc = Dataset(file_name)
	time_var = inc.variables['time']
	ifcstdate = datetime.strptime(start_fcstdate, "%Y%m%d")
	ffcstdate = datetime.strptime(end_fcstdate, "%Y%m%d")

	iidx = date2index(datetime(ifcstdate.year, ifcstdate.month, ifcstdate.day), time_var)
	fidx = date2index(datetime(ffcstdate.year, ffcstdate.month, ffcstdate.day), time_var)
	aux = inc.variables[var_name][iidx:fidx+1]
	
	hind_obs1.append(np.nansum(aux[0:firt_mon]))
	hind_obs2.append(np.nansum(aux[firt_mon:firt_mon+seco_mon]))
	hind_obs3.append(np.nansum(aux[firt_mon+seco_mon:firt_mon+seco_mon+thir_mon]))

    inc.close()
    clim_obs1 = np.squeeze(hind_obs1)
    clim_obs2 = np.squeeze(hind_obs2)
    clim_obs3 = np.squeeze(hind_obs3)

    return clim_obs1, clim_obs2, clim_obs3


def closest(fcst_target, clim_list):
    aux = []    
    for ii in range(0, clim_list.shape[0]):
        aux.append(abs(fcst_target-clim_list[ii]))
    min_value = np.min(aux)    
    idx_min = np.where(aux == min_value)[-1][-1]

    return idx_min


def eqmres_bias_correction(hind, obs, fcst):    
    """ Remove precipitaiton bias via Empirical Quantile Mapping
    (eQM).

    :param: hind: list
    :param: obs: list
    :param: fcst: list
    :return: precipitation
    """

    xs_hind = np.sort(hind)
    #ys_hind = np.arange(1, len(xs_hind)+1)/float(len(xs_hind))
    xs_obs = np.sort(obs)
    #ys_obs = np.arange(1, len(xs_obs)+1)/float(len(xs_obs))
    
    idx_hind = closest(fcst, xs_hind)
    corr = xs_obs[idx_hind]
    
    return np.array(corr)


if __name__ == "__main__":

    arguments()
    global month, year, localdir, var_name, time_freq, data_base,  \
           hind_obs_period
	   
    # Target basin
    bname  = args.basin
    macros = args.macro
    micros = args.micro
    allbasins = args.all_basins

    # Local directory,variable name and Model
    localdir   = args.local_dir
    modelname  = args.model_name
    hydromodel = args.hydro_model
    
    hind_name  = 'hind8110'
    type_corr  = '_cor_flow' 
    var_name   = 'flow'
    time_freq  = 'daily'
    data_base  = 'ons_obs'
    hind_obs_period = '19810101_20151231'

    # Target period
    month = args.month_target
    year = args.year_target

    # Target basin
    if macros or micros or allbasins:
        basin_list = basin_dict(bname, macro=macros, micro=micros,
                                all_basins=allbasins)
    else:
        basin_list = [bname]
    
    bas_new1 = []
    for bas1 in basin_list:
        if 'ilha_solteira_equivalente' not in (bas1):
            bas_new1.append(bas1)

    bas_new2 = []
    for bas2 in bas_new1:
        if 'guapore' not in (bas2):
            bas_new2.append(bas2)

    bas_new3 = []
    for bas3 in bas_new2:
        if 'ponte_de_pedra' not in (bas3):
            bas_new3.append(bas3)
	    
    bas_new4 = []
    for bas4 in bas_new3:
        if 'edgard_de_souza_inc' not in (bas4):
            bas_new4.append(bas4)

    bas_new5 = []
    for bas5 in bas_new4:
        if 'traicao' not in (bas5):
            bas_new5.append(bas5)
    
    bas_new6 = []
    for bas6 in bas_new5:
        if 'xingo' not in (bas6):
            bas_new6.append(bas6)
	
    target_date, list_model = define_initial_parameters(hydromodel)
    
    for hydroname in list_model:

        print " " 
        print "Run Remotion Bias for Model and Date: {0} - {1}/{2:02d}".format(modelname.upper(),
                                        target_date.year, target_date.month)
        print " " 
         
        for basin in bas_new6:
            
            print 'Processing Basin: {0}'.format(basin)

            basin_full_name = basin_dict(basin)[2]
            basin_name = basin_dict(basin)[1]
            
	    fcst_yea1, fcst_yea2, fcst_yea3, str_mon, fcst_mon1, fcst_mon2, fcst_mon3, start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate)
            
	    fcst1, fcst2, fcst3, firt_mon, seco_mon, thir_mon, flag = import_fcst_model_data(modelname, hydroname, target_date, basin)
	    
	    fcst_acc1 = np.array(np.nansum(fcst1))
	    fcst_acc2 = np.array(np.nansum(fcst2))
	    fcst_acc3 = np.array(np.nansum(fcst3))
	    
	    if flag:
		
                model1, model2, model3 = import_hind_model_data(modelname, hydroname, target_date, basin)
                obs1, obs2, obs3 = import_hind_obs_data(modelname, target_date, basin)
		
                if  len(model1) != len(obs1):
                    print 'Error hind and obs climatology period1'

                if  len(model2) != len(obs2):
                    print 'Error hind and obs climatology period2'
		    
                if  len(model3) != len(obs3):
                    print 'Error hind and obs climatology period3'
		
		# Removing Bias - Empirical Quantil Mapping Method
		fcst_eqmres1 = eqmres_bias_correction(model1, obs1, fcst_acc1)
                fcst_eqmres2 = eqmres_bias_correction(model2, obs2, fcst_acc2)
                fcst_eqmres3 = eqmres_bias_correction(model3, obs3, fcst_acc3)
		
		corr1 = np.full((firt_mon), np.nan)
		corr_des1 = ((fcst1 / fcst_acc1) * fcst_eqmres1)
		
		corr2 = np.full((seco_mon), np.nan)
		corr_des2 = ((fcst2 / fcst_acc2) * fcst_eqmres2)

		corr3 = np.full((thir_mon), np.nan)
		corr_des3 = ((fcst3 / fcst_acc3) * fcst_eqmres3)
		
		fcst_eqmres_array  = np.array([corr_des1, corr_des2, corr_des3])
		fcst_eqmres  =  np.concatenate((fcst_eqmres_array), axis=0)
					
		path_out =  "{0}{1}/{2}/{3}_{4}{5}/{6}/{7}/{8}/". \
			   format(HIDROPY_DIR, localdir, var_name, hydroname, time_freq,
				type_corr, modelname, str_mon, basin_name)

		if not os.path.exists(path_out):
		    os.makedirs(path_out)
			
		write_flow(fcst_eqmres, start_fcstdate, end_fcstdate, time_freq, 
			var_name,'{0}_{1}'.format(modelname, hind_name), 'fcst',
			'{0}{1}'.format(basin_full_name, type_corr), hydroname,
			init_date=start_rundate, output_path=path_out)
	    else:
		continue


