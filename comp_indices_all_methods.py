# -*- coding: utf-8 -*-

# Author = 'Funceme'
# Credits = 'Leidinice Silva'
# Maintainer = 'Funceme'
# Date = 19/12/2017  (dd/mm/aaaa)
# Comment = 'Este script foi desenvolvido dentro do Termo de Cooperação 
#	     0050.0100467.16.9 entre Funceme e Petrobras sob o contexto do
#	     Projeto Projeção de Vazão Natural Afluente com base na escala 
#	     de tempo e clima.'
# Description = 'Compute best indices of m1, m2 and m3.'


""" Compute best indices of m1, m2 and m3. """

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
from hidropy.utils.hidropy_utils import lsname
from hidropy.utils.all_basins_dict_daily import basinsf

from PyFuncemeClimateTools.DefineDates import index_between_dates
from PyFuncemeClimateTools import ClimateStats as cs

from os.path import expanduser

HIDROPY_DIR = os.environ['HIDROPY_DIR']

var_name  = 'flow'
time_freq = 'daily'
data_base = 'ons_obs'
hind_obs1 = '19810101_20151231'
hind_obs2 = '20160101_*'
localdir  = '/io'

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "12/19/2017"
__description__ = "Compute best indices of m1, m2 and m3."


def define_dates(target_date):
    """ Define date start run list.
    """
    str_mon = target_date.strftime("%b").lower()

    start_rundate = '{0}{1:02d}{2:02d}'.format(target_date.year, target_date.month, target_date.day)

    return str_mon, start_rundate


def import_model_data(method, basin):
    """ Import model data.
    """
    
    model_2w = []
    model_4w = []
    
    for year in range(2011, 2014 + 1):
	
	for mon in range(1, 12 + 1):

            c = calendar.TextCalendar(calendar.MONDAY)
	    
            for i in c.itermonthdays(year, mon):

		if i != 0:
                    day = date(year, mon, i)
                    
		    if day.weekday() == calendar.MONDAY:

                        date_monday = datetime(year, mon, i)

			str_mon, start_rundate = define_dates(date_monday)
			
			dir_modelname  = "{0}{1}/{2}/smap_weather_climate/gfs05_rsm2008/{3}/{4}/{5}/{6}". \
					 format(HIDROPY_DIR, localdir, var_name, method, year, str_mon, macro)

			file_modelname = "{0}/{1}_{2}_{3}_gfs05_rsm2008_fcst_{4}_smap_{5}." \
					 "nc".format(dir_modelname, var_name, time_freq, method, start_rundate, basin)		
		
			try:
			    model_data = Dataset(os.path.join(dir_modelname, file_modelname))
			    var_data   = model_data.variables[var_name][:]
			    aux_2w   = np.nanmean(var_data[0:14])
   			    aux_4w   = np.nanmean(var_data[14:])
			except:
			    var_data   = np.nan
			    
			model_2w.append(aux_2w)
			model_4w.append(aux_4w)

    model_data.close()

    model_2w_new = np.array(model_2w)
    model_4w_new = np.array(model_4w)

    return model_2w_new, model_4w_new


def import_ons_data(basin):
    """ Import obs data.
    """
    
    obs_2w = []
    obs_4w = []

    for year in range(2011, 2014 + 1):
	
	for mon in range(1, 12 + 1):

            c = calendar.TextCalendar(calendar.SATURDAY)
            for i in c.itermonthdays(year, mon):
                
		if i != 0:
                    day = date(year, mon, i)
		                        
		    if day.weekday() == calendar.SATURDAY:

                        date_saturday = datetime(year, mon, i)

			date_final = date_saturday + relativedelta(days=+41)
				
			str_mon, start_rundate = define_dates(date_saturday)
			str_mon, end_rundate   = define_dates(date_final)
			
			# 1981-2015 
			file_name1 = '{0}{1}/{2}/ons_daily/1981-present/{3}/' \
				    '{2}_{4}_{5}_{6}_{7}.nc' \
				    .format(HIDROPY_DIR, localdir, var_name, macro, time_freq,
				     data_base, hind_obs1, basin)
			

			ons_data = Dataset(file_name1)
			ons = ons_data.variables[var_name][:] 

			date_start = os.path.basename(file_name1).split('_')[4]
			date_end   = os.path.basename(file_name1).split('_')[5]
			
			i1, i2 = index_between_dates(date_start, date_end, start_rundate, end_rundate, 'days')
			aux = ons[i1:i2+1]
						
			obs_2w.append(np.nanmean(aux[0:14]))
			obs_4w.append(np.nanmean(aux[14:]))
			
    ons_data.close()

    ons_2w_new = np.squeeze(obs_2w)
    ons_4w_new = np.squeeze(obs_2w)

    return ons_2w_new, ons_4w_new


tab = tt.Texttable(max_width=200)
tab_inform = [[]]

# Target basin
macros = basinsf(macro=1)
for macro in macros:
    
    basins = basinsf(smap=macro)
    
    bas_new1 = []
    for bas1 in basins:
	if '_rondon_ii' not in (bas1):
	    bas_new1.append(bas1)

    bas_new2 = []
    for bas2 in bas_new1:
        if '_lajes_fontes_nova_pereira_passos' not in (bas2):
            bas_new2.append(bas2)

    bas_new3 = []
    for bas3 in bas_new2:
        if '_pedras' not in (bas3):
            bas_new3.append(bas3)
    
    bas_new4 = []
    for bas4 in bas_new3:
        if '_guilman' not in (bas4):
            bas_new4.append(bas4)

    bas_new5 = []
    for bas5 in bas_new4:
        if '_porto_estrela_inc' not in (bas5):
            bas_new5.append(bas5)

    bas_new6 = []
    for bas6 in bas_new5:
        if '_sa_carvalho_inc' not in (bas6):
            bas_new6.append(bas6)

    bas_new7 = []
    for bas7 in bas_new6:
        if '_salto_grande' not in (bas7):
            bas_new7.append(bas7)

    bas_new8 = []
    for bas8 in bas_new7:
        if '_itutinga' not in (bas8):
            bas_new8.append(bas8)
	    
    bas_new9 = []
    for bas9 in bas_new8:
        if '_itiquira' not in (bas9):
            bas_new9.append(bas9)

    bas_new10 = []
    for bas10 in bas_new9:
        if '_manso' not in (bas10):
            bas_new10.append(bas10)

    bas_new11 = []
    for bas11 in bas_new10:
        if '_ilha_solteira_equivalente' not in (bas11):
            bas_new11.append(bas11)

    bas_new12 = []
    for bas12 in bas_new11:
        if '_espora' not in (bas12):
            bas_new12.append(bas12)

    bas_new13 = []
    for bas13 in bas_new12:
        if '_boa_esperanca' not in (bas13):
            bas_new13.append(bas13)
	    
    bas_new14 = []
    for bas14 in bas_new13:
        if '_edgard_de_souza_inc' not in (bas14):
            bas_new14.append(bas14)
	    	    	    	    	    	    	    	    
    for basin in bas_new14:
	
	print 'Processing Basin: {0}'.format(basin)

	method = 'm1'
	model_2w_m1, model_4w_m1 = import_model_data(method, basin)
	
	method = 'm2'
	model_2w_m2, model_4w_m2 = import_model_data(method, basin)
	
	method = 'm3'
	model_2w_m3, model_4w_m3 = import_model_data(method, basin)
	
	ons_2w, ons_4w = import_ons_data(basin)
	
	# calculate correlation
	corr_2w_m1 = round((np.corrcoef(np.array(model_2w_m1), np.array(ons_2w)))[0][1], 3)
	corr_2w_m2 = round((np.corrcoef(np.array(model_2w_m2), np.array(ons_2w)))[0][1], 3)
	corr_2w_m3 = round((np.corrcoef(np.array(model_2w_m3), np.array(ons_2w)))[0][1], 3)

	corr_4w_m1 = round((np.corrcoef(np.array(model_4w_m1), np.array(ons_4w)))[0][1], 3)
	corr_4w_m2 = round((np.corrcoef(np.array(model_4w_m2), np.array(ons_4w)))[0][1], 3)
	corr_4w_m3 = round((np.corrcoef(np.array(model_4w_m3), np.array(ons_4w)))[0][1], 3)
	
	# calculate rmse
	rmse_2w_m1  = (cs.compute_rmse(np.array(model_2w_m1),  np.array(ons_2w)))
	rmse_2w_m2  = (cs.compute_rmse(np.array(model_2w_m2),  np.array(ons_2w)))
	rmse_2w_m3  = (cs.compute_rmse(np.array(model_2w_m3),  np.array(ons_2w)))

	rmse_4w_m1  = (cs.compute_rmse(np.array(model_4w_m1),  np.array(ons_4w)))
	rmse_4w_m2  = (cs.compute_rmse(np.array(model_4w_m2),  np.array(ons_4w)))
	rmse_4w_m3  = (cs.compute_rmse(np.array(model_4w_m3),  np.array(ons_4w)))
	
	

	corr_str_2w  = ['m1', 'm2', 'm3']
	corr_list_2w = [corr_2w_m1, corr_2w_m2, corr_2w_m3]
	
	corr_str_4w  = ['m1', 'm2', 'm3']
	corr_list_4w = [corr_4w_m1, corr_4w_m2, corr_4w_m3]

	rmse_str_2w  = ['m1', 'm2', 'm3']
	rmse_list_2w = [rmse_2w_m1, rmse_2w_m2, rmse_2w_m3]
	
	rmse_str_4w  = ['m1', 'm2', 'm3']
	rmse_list_4w = [rmse_4w_m1, rmse_4w_m2, rmse_4w_m3]
	
	best_corr_2w = corr_str_2w[np.where(corr_list_2w == np.max(corr_list_2w))[-1][-1]]
	best_corr_4w = corr_str_4w[np.where(corr_list_4w == np.max(corr_list_4w))[-1][-1]]

	best_rmse_2w = rmse_str_2w[np.where(rmse_list_2w == np.min(rmse_list_2w))[-1][-1]]
	best_rmse_4w = rmse_str_4w[np.where(rmse_list_4w == np.min(rmse_list_4w))[-1][-1]]
	
	# tab_inform.append([basin, corr_2w_m1, corr_2w_m2, corr_2w_m3, corr_4w_m1, corr_4w_m2, corr_4w_m3, best_corr_2w, best_corr_4w])
	tab_inform.append([basin, rmse_2w_m1, rmse_2w_m2, rmse_2w_m3, rmse_4w_m1, rmse_4w_m2, rmse_4w_m3, best_rmse_2w, best_rmse_4w])

tab.add_rows(tab_inform)
tab.set_cols_align(['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'])

# tab.header(['Usina', 'corr_2w_m1', 'corr_2w_m2', 'corr_2w_m3', 'corr_4w_m1', 'corr_4w_m2', 'corr_4w_m3', 'best_2w', 'best_4w'])
tab.header(['Usina', 'rmse_2w_m1', 'rmse_2w_m2', 'rmse_2w_m3', 'rmse_4w_m1', 'rmse_4w_m2', 'rmse_4w_m3', 'best_2w', 'best_4w'])

table = str(tab.draw())

dir_file  = "/home/musf/leidinice/"
file_name = '{0}best_rmse_all_basins.asc'.format(dir_file)
file_save = open(file_name, 'w')
file_save.write(table)
file_save.close()
exit()




