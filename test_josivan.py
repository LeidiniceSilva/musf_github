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

    start_rundate = '{0}{1:02d}{2:02d}'.format(target_date.year, target_date.month, target_date.day)

    return start_rundate
    
def import_ons_data(basin):
    """ Import obs data.
    """
    
    obs_2w = []
    obs_4w = []

    for year in range(2011, 2015 + 1):
	
	for mon in range(1, 11 + 1):

            c = calendar.TextCalendar(calendar.MONDAY)
            for i in c.itermonthdays(year, mon):
                
		if i != 0:
                    day = date(year, mon, i)
		                        
		    if day.weekday() == calendar.MONDAY:

                        date_final = datetime(year, mon, i)

			date_init = date_final + relativedelta(days=-182)
			
			week1 = date_final 
			week2 = week1 + relativedelta(days=+7)
			week3 = week2 + relativedelta(days=+7)
			week4 = week3 + relativedelta(days=+7)
			week5 = week4 + relativedelta(days=+7)
			week6 = week5 + relativedelta(days=+7)

			date1 = define_dates(date_init)
			date2 = define_dates(date_final)
			date3 = define_dates(week1)
			date4 = define_dates(week2)
			date5 = define_dates(week3)
			date6 = define_dates(week4)
			date7 = define_dates(week5)
			date8 = define_dates(week6)
			
			# 1981-2015 
			file_name1 = '{0}{1}/{2}/ons_daily/1981-present/{3}/' \
				    '{2}_{4}_{5}_{6}_{7}.nc' \
				    .format(HIDROPY_DIR, localdir, var_name, macro, time_freq,
				     data_base, hind_obs1, basin)
			
			# 2016-present 
			file_name2 = lsname('{0}{1}/{2}/ons_daily/2016-present/{3}/' \
				    '{2}_{4}_{5}_{6}_{7}.nc' \
				    .format(HIDROPY_DIR, localdir, var_name, macro, time_freq,
				     data_base, hind_obs2, basin))
			
			ons_data1 = Dataset(file_name1)
			ons_data2 = Dataset(file_name2)
			
			ons1 = ons_data1.variables[var_name][:] 
			ons2 = ons_data2.variables[var_name][:]
			ons = np.concatenate((ons1, ons2), axis=0)
			
						
			date_start = os.path.basename(file_name1).split('_')[4]
			date_end   = os.path.basename(file_name2).split('_')[5]
			
			# indice date1 
			i1, i2 = index_between_dates(date_start, date_end, date1, date2, 'days')
			aux = ons[i1:i2+1]
		
			ons_aux = []
			for i in xrange(0, len(aux[:-1]), 7):
			    ons_aux.append(np.nanmean(aux[i:i+7]))			
    ons_data1.close()
    ons_data2.close()

    ons_new = np.squeeze(ons_aux)

    return ons_new


# Target basin
macros = basinsf(macro=1)
for macro in macros:
    
    basins = basinsf(smap=macro)
    
    for basin in basins:
    
	print 'Processing Basin: {0}'.format(basin)
	
	ons_new = import_ons_data(basin)
	print len(ons_new)
	exit()
	
