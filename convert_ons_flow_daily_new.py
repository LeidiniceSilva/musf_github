# -*- coding: utf-8 -*-

"""
This script convert daily mean flow from ONS to .asc and .nc.
"""

from datetime import datetime
import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import os
import csv
import pandas
import calendar
import numpy.ma as ma
from hidropy.utils.all_basins_dict_daily import basinsf
from hidropy.utils.hidropy_utils import create_path, read_thiessen_obs, lsname
from hidropy.utils.write_flow import write_flow
import argparse
import pandas as pd
from numpy import genfromtxt

HIDROPY_DIR = os.environ['HIDROPY_DIR']

__author__ = "leidinice Silva"
__email__  = "leidinice.silva@funceme.br"
__date__   = "11/08/2017"
__description__ = "This script convert daily mean flow from ONS"
    
    
def arguments():
    """
    Function to insert parameters from external environment (example: shell)
    In this function is possible to convert observed flows from 
    'historico_vazao_20160101_20171030.xls' in .asc and .nc files for each subbasin.
    New daily flows can be added to old files by using the following parameter:
    Overwrite old files (--overwrite) --> new files will be created with the 
    new daily flow.
    
    Ex: 
        python convert_ons_flow_daily.py --overwrite
    
    :return: observed daily flow from ONS flow for each subbasin.
    """

    global args
    
    # fyear  = datetime.now().year
    # fmonth = datetime.now().month
    # fday   = datetime.now().day
    
    ## datas do último arquivo fornecido pela ONS:
    fyear  = 2018
    fmonth = 02
    fday   = 06
    
    parser = argparse.ArgumentParser(prog='Compute flow')
    parser.add_argument('--iyear'    , help='Initial year (2016)')
    parser.add_argument('--fyear'    , help='Final year ', default=fyear)
    parser.add_argument('--fmonth'   , help='Final month', default=fmonth)
    parser.add_argument('--fday'     , help='Final day'  , default=fday)
    parser.add_argument('--overwrite', help='Overwrite file, if it exists', action='store_true')

    args = parser.parse_args()

    return args
    

# Input arguments
arguments()
iyear     = int(args.iyear)
cur_year  = int(args.fyear)
cur_month = int(args.fmonth)
cur_day   = int(args.fday)
overwrite = args.overwrite

# Actual date
cur_date  = datetime.now().strftime("%Y%m%d")

# Dates for write_flow
idate = datetime(iyear, 01, 01).strftime('%Y%m%d')
fdate = datetime(cur_year, cur_month, cur_day).strftime('%Y%m%d')

# Reading file
print 'Reading ONS daily flow per basin'

my_data = genfromtxt("/home/musf/leidinice/flow_ons/daily/historico_vazao_2016_2018_new.csv", delimiter=',')

for i, cod in enumerate(my_data[:,0]):
   
    sbasin = basinsf(cod=int(cod))[0:]
    if sbasin:
	
	basin = sbasin[0]
	macro  = basinsf(macro=basin)
	values = (my_data[i,1:].squeeze())
	values_mx = ma.masked_values(values, -999.)

	# Write flow
	path_out = "/home/musf/leidinice/flow_ons/daily/ons_daily_2016_2018/{0}/".format(macro)
	
	if not os.path.exists(path_out):
	    os.makedirs(path_out)
	
	out_name = write_flow(values_mx[:], idate, fdate, 'daily', 'flow', 'ons', 'obs', basin, 'smap', output_path=path_out)
	
	cor_name_nc  = 'flow_daily_ons_obs_{0}_{1}_{2}.nc'     .format(idate, fdate, basin)	
	cor_name_asc = 'flow_daily_ons_obs_{0}_{1}_{2}.asc'    .format(idate, fdate, basin)

	os.rename('{0}/flow_daily_ons_obs_{1}_{2}_smap_{3}.nc' .format(path_out, idate, fdate, basin), path_out+cor_name_nc)
	os.rename('{0}/flow_daily_ons_obs_{1}_{2}_smap_{3}.asc'.format(path_out, idate, fdate, basin), path_out+cor_name_asc)
	
	print "basin" , basin
	print 'done'
	
    else:
	continue
		    
		    






	
	




