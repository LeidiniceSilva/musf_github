# -*- coding: utf-8 -*-

""" Compare fluviometric data flow with all models over plot pluma graph. """
import os
import netCDF4
import argparse
from pylab import *
from netCDF4 import Dataset
from scipy.stats import norm
from os.path import expanduser
from dateutil.relativedelta import *
from datetime import date, datetime
from matplotlib import pyplot as plt
from hidropy.utils.hidropy_utils import date2index
from matplotlib.font_manager import FontProperties
from hidropy.utils.hidropy_utils import create_path, lsname
from hidropy.utils.all_basins_dict_monthly import basinsf
import warnings
import subprocess
warnings.filterwarnings("ignore")

typ   = 'smap'
param = 'flow'
scale = 'monthly'
home  = expanduser("~")

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "18/08/2017"
__description__ = "Compare fluviometric data flows of all models by plotting plume graphs"


def arguments():

    """
    Function to insert parameters from external environment (example: shell)

    In this function is possible to insert the following parameters: Initial year 
    of forecasting (--iyear), Initial month of forecasting (--imonth), Final year 
    of forecasting (--fyear) and final month of forecasting (--fmonth).
    
    # Ex: Plume graphs for 201708:
        # python plot_smap_forecast_plume_graphs_all_models_monthly.py --iyear=2017 --imonth=8 --fyear=2017 --fmonth=8
    
    """
 
    global args

    __description__ = "Script to compare fluviometric data flows of all models by plotting plume graphs" 

    iyear  = datetime.now().year
    imonth = datetime.now().month
    fyear  = datetime.now().year
    fmonth = datetime.now().month
 
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('--iyear' , help='Initial  year of forecast. Default is actual year. ', default=iyear)
    parser.add_argument('--imonth', help='Initial month of forecast. Default is actual month.', default=imonth)
    parser.add_argument('--fyear' , help='Final  year of forecast. Default is actual year. '  , default=fyear)
    parser.add_argument('--fmonth', help='Final month of forecast. Default is actual month.'  , default=fmonth)

    args = parser.parse_args()

    return args

arguments()
iyear  = int(args.iyear)
imonth = int(args.imonth)
fyear  = int(args.fyear)
fmonth = int(args.fmonth)


def define_dates(target_date):
    
    target_ifcstdate = target_date + relativedelta(months=1)
    target_efcstdate = target_date + relativedelta(months=3)

    ini_rundate   = '{0}{1:02d}{2:02d}'.format(target_date.year, target_date.month, target_date.day)
    star_fcstdate = '{0}{1:02d}{2:02d}'.format(target_ifcstdate.year, target_ifcstdate.month, 15)
    end_fcstdate  = '{0}{1:02d}{2:02d}'.format(target_efcstdate.year, target_efcstdate.month, 15)
    
    return ini_rundate, star_fcstdate, end_fcstdate


def import_model_data(model, year, mon, basin, method):
    
    if model  == 'echam46':
        period = 'hind8110'
        dir_model = home + "/io/{0}/{1}_{2}{3}/{4}/{5}/{6}".format(param, typ, scale, method, model, month, macro)
    else:
        period = 'hind8210'
        dir_model = home + "/io/{0}/{1}_{2}{3}/nmme/{4}/{5}/{6}".format(param, typ, scale, method, model, month, macro)

    clim_list = []
    
    target_date = date(year, mon, 01)
    ini_rundate, star_fcstdate, end_fcstdate = define_dates(target_date)

    if model == 'ncep-cfsv2':
		file_model = "{0}/{1}_{2}_{3}_{4}_fcst_{5}_{6}_{7}_{8}_{9}{10}_petclim.nc" \
		     .format(dir_model, param, scale, model, period, ini_rundate, 
		             star_fcstdate, end_fcstdate, typ, basin, method)
    else:
		file_model = "{0}/{1}_{2}_{3}_{4}_fcst_{5}_{6}_{7}_{8}_{9}{10}.nc" \
		     .format(dir_model, param, scale, model, period, ini_rundate, 
		             star_fcstdate, end_fcstdate, typ, basin, method)
	
	input_data = Dataset(file_model)
	var  = input_data.variables[param][:]
	clim_list.append(var)
	clim = np.squeeze(clim_list)
	
    return clim


def import_obs_data(fyear, mon, basin):

    dir_obs  = "{0}/io/{1}/ons_{2}/1981-present/{3}"	     .format(home, param, scale, macro)
    file_obs = lsname("{0}/{1}_{2}_ons_obs_19810115_*_{3}.nc".format(dir_obs, param, scale, basin))

	data = netCDF4.Dataset(file_obs)
	time = data.variables['time']

	iidx = date2index(date(1981, 01, 01), time)
	fidx = date2index(date(2010, 12, 15), time)
	variable = data.variables[param][iidx:fidx + 1]

	iidx_y = date2index(date(2016, mon, 01), time)
	fidx_y = date2index(date(fyear, mon, 15), time)

	variable_y = data.variables[param][iidx_y:fidx_y + 1]
	ons_cicle  = np.squeeze([variable_y[1:]])

	dic_clim = {1: [(variable[1::12]), (variable[2::12]), (variable[3::12]), (variable[4::12]), (variable[5::12]),
			(variable[6::12]), (variable[7::12]), (variable[8::12]), (variable[9::12]), (variable[10::12]),
			(variable[11::12]), (variable[0::12]), (variable[1::12]), (variable[2::12]), (variable[3::12])],
		    2: [(variable[2::12]), (variable[3::12]), (variable[4::12]), (variable[5::12]), (variable[6::12]),
			(variable[7::12]), (variable[8::12]), (variable[9::12]), (variable[10::12]), (variable[11::12]),
			(variable[0::12]), (variable[1::12]), (variable[2::12]), (variable[3::12]), (variable[4::12])],
		    3: [(variable[3::12]), (variable[4::12]), (variable[5::12]), (variable[6::12]), (variable[7::12]),
			(variable[8::12]), (variable[9::12]), (variable[10::12]), (variable[11::12]), (variable[0::12]),
			(variable[1::12]), (variable[2::12]), (variable[3::12]), (variable[4::12]), (variable[5::12])],
		    4: [(variable[4::12]), (variable[5::12]), (variable[6::12]), (variable[7::12]), (variable[8::12]),
			(variable[9::12]), (variable[10::12]), (variable[11::12]), (variable[0::12]), (variable[1::12]),
			(variable[2::12]), (variable[3::12]),  (variable[4::12]), (variable[5::12]), (variable[6::12])],
		    5: [(variable[5::12]), (variable[6::12]), (variable[7::12]), (variable[8::12]), (variable[9::12]),
			(variable[10::12]), (variable[11::12]), (variable[0::12]), (variable[1::12]), (variable[2::12]),
			(variable[3::12]), (variable[4::12]), (variable[5::12]), (variable[6::12]), (variable[7::12])],
		    6: [(variable[6::12]), (variable[7::12]), (variable[8::12]), (variable[9::12]), (variable[10::12]),
			(variable[11::12]), (variable[0::12]), (variable[1::12]), (variable[2::12]), (variable[3::12]),
			(variable[4::12]), (variable[5::12]), (variable[6::12]), (variable[7::12]), (variable[8::12])],
		    7: [(variable[7::12]), (variable[8::12]), (variable[9::12]), (variable[10::12]), (variable[11::12]),
			(variable[0::12]), (variable[1::12]), (variable[2::12]), (variable[3::12]), (variable[4::12]),
			(variable[5::12]), (variable[6::12]), (variable[7::12]), (variable[8::12]), (variable[9::12])],
		    8: [(variable[8::12]), (variable[9::12]), (variable[10::12]), (variable[11::12]), (variable[0::12]),
			(variable[1::12]), (variable[2::12]), (variable[3::12]), (variable[4::12]), (variable[5::12]),
			(variable[6::12]), (variable[7::12]), (variable[8::12]), (variable[9::12]), (variable[10::12])],
		    9: [(variable[9::12]), (variable[10::12]), (variable[11::12]), (variable[0::12]), (variable[1::12]),
			(variable[2::12]), (variable[3::12]), (variable[4::12]), (variable[5::12]), (variable[6::12]),
			(variable[7::12]), (variable[8::12]), (variable[9::12]), (variable[10::12]), (variable[11::12])],
		    10: [(variable[10::12]), (variable[11::12]), (variable[0::12]), (variable[1::12]), (variable[2::12]),
			 (variable[3::12]), (variable[4::12]), (variable[5::12]), (variable[6::12]), (variable[7::12]),
			 (variable[8::12]), (variable[9::12]), (variable[10::12]), (variable[11::12]), (variable[0::12])],
		    11: [(variable[11::12]), (variable[0::12]), (variable[1::12]), (variable[2::12]), (variable[3::12]),
			 (variable[4::12]), (variable[5::12]), (variable[6::12]), (variable[7::12]), (variable[8::12]),
			 (variable[9::12]), (variable[10::12]), (variable[11::12]), (variable[0::12]), (variable[1::12])],
		    12: [(variable[0::12]), (variable[1::12]), (variable[2::12]), (variable[3::12]), (variable[4::12]),
			 (variable[5::12]), (variable[6::12]), (variable[7::12]), (variable[8::12]), (variable[9::12]),
			 (variable[10::12]), (variable[11::12]), (variable[0::12]), (variable[1::12]), (variable[2::12])]}

	ons_obs  = np.nanmean(dic_clim[mon], axis=1)
	ons_clim = np.array(ons_obs)

	ons_obs_p33  = norm.ppf(0.33, loc=np.nanmean(dic_clim[mon], axis=1), scale=np.nanstd(dic_clim[mon], axis=1))
	ons_clim_p33 = np.array(ons_obs_p33)

	ons_obs_p66  = norm.ppf(0.66, loc=np.nanmean(dic_clim[mon], axis=1), scale=np.nanstd(dic_clim[mon], axis=1))
	ons_clim_p66 = np.array(ons_obs_p66)
	
	
    else:
		print 'missing --------->', file_obs
	pass
	    
    return ons_cicle, ons_clim, ons_clim_p33, ons_clim_p66


dic_mon = { 1:  ['Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Jan', 'FEV', 'MAR', 'ABR'],
            2:  ['Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Jan', 'Fev', 'MAR', 'ABR', 'MAI'],
            3:  ['Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Jan', 'Fev', 'Abr', 'ABR', 'MAI', 'JUN'],
            4:  ['Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'MAI', 'JUN', 'JUL'],
            5:  ['Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'JUN', 'JUL', 'AGO'],
            6:  ['Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'JUL', 'AGO', 'SET'],
            7:  ['Ago', 'Set', 'Out', 'Nov', 'Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'jul', 'AGO', 'SET', 'OUT'],
            8:  ['Set', 'Out', 'Nov', 'Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'jul', 'Ago', 'SET', 'OUT', 'NOV'],
            9:  ['Out', 'Nov', 'Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'jul', 'Ago', 'Set', 'OUT', 'NOV', 'DEZ'],
            10: ['Nov', 'Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'jul', 'Ago', 'Set', 'Out', 'NOV', 'DEZ', 'JAN'],
            11: ['Dez', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'jul', 'Ago', 'Set', 'Out', 'Nov', 'DEZ', 'JAN', 'FEV'],
            12: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'JAN', 'FEV', 'MAR']}

dic_month = { 1: 'jan', 2: 'feb', 3: 'mar',  4: 'apr',  5: 'may',  6: 'jun', 
	      7: 'jul', 8: 'aug', 9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec' }

cor_method_list = ['', '_cor_pr', '_cor_flow', '_cor_pr_flow']

macros = basinsf(macro=1)

for method in cor_method_list:
    
    for year in range(iyear, fyear+1):
	for mon in range(imonth, fmonth+1):
	    month = dic_month[mon]

	    for macro in macros:
		basins = basinsf(smap=macro)

		for basin in basins:
		    print
		    print 'Plotting:', basin, month, method

		    cicle, clim, p33, p66 = import_obs_data(fyear, mon, basin)
		    
		    model = 'echam46'
		    sim1  = import_model_data(model, year, mon, basin, method)

		    model = 'cmc1-cancm3'
		    sim2  = import_model_data(model, year, mon, basin, method)

		    model = 'cmc2-cancm4'
		    sim3  = import_model_data(model, year, mon, basin, method)

		    model = 'cola-rsmas-ccsm3'
		    sim4  = import_model_data(model, year, mon, basin, method)

		    model = 'cola-rsmas-ccsm4'
		    sim5  = import_model_data(model, year, mon, basin, method)

		    model = 'gfdl-cm2p5-flor-b01'
		    sim6  = import_model_data(model, year, mon, basin, method)

		    model = 'nasa-gmao-062012'
		    sim7  = import_model_data(model, year, mon, basin, method)

		    model = 'ncep-cfsv2'
		    sim8  = import_model_data(model, year, mon, basin, method)

		    data1 = np.full((15), np.nan)
		    data1[0:12]  = np.squeeze(cicle)
		    data1[12:15] = np.squeeze(sim1)

		    data2 = np.full((15), np.nan)
		    data2[0:12]  = np.squeeze(cicle)
		    data2[12:15] = np.squeeze(sim2)

		    data3 = np.full((15), np.nan)
		    data3[0:12]  = np.squeeze(cicle)
		    data3[12:15] = np.squeeze(sim3)

		    data4 = np.full((15), np.nan)
		    data4[0:12]  = np.squeeze(cicle)
		    data4[12:15] = np.squeeze(sim4)

		    data5 = np.full((15), np.nan)
		    data5[0:12]  = np.squeeze(cicle)
		    data5[12:15] = np.squeeze(sim5)

		    data6 = np.full((15), np.nan)
		    data6[0:12]  = np.squeeze(cicle)
		    data6[12:15] = np.squeeze(sim6)

		    data7 = np.full((15), np.nan)
		    data7[0:12]  = np.squeeze(cicle)
		    data7[12:15] = np.squeeze(sim7)

		    data8 = np.full((15), np.nan)
		    data8[0:12]  = np.squeeze(cicle)
		    data8[12:15] = np.squeeze(sim8)

		    data9 = np.full((15), np.nan)
		    data9[0:15] = np.squeeze(clim)

		    data10 = np.full((15), np.nan)
		    data10[0:15] = np.squeeze(p33)

		    data11 = np.full((15), np.nan)
		    data11[0:15] = np.squeeze(p66)

		    data12 = np.full((15), np.nan)
		    data12[0:12] = np.squeeze(cicle)
		    
		    # plot pluma graphs of all models
		    fig   = plt.figure(figsize=(26, 18))
		    time_ = np.arange(1, 15 + 1)

		    a = plt.plot(time_, data1, time_, data2, time_, data3, time_,  data4, time_,  data5, time_, data6,
				 time_, data7, time_, data8, time_, data9, time_, data10, time_, data11, time_, data12)

		    l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12 = a
		    plt.setp(l1,  linewidth=6, markeredgewidth=1, marker='D', color='red')
		    plt.setp(l2,  linewidth=6, markeredgewidth=1, marker='D', color='royalblue')
		    plt.setp(l3,  linewidth=6, markeredgewidth=1, marker='D', color='darkgreen')
		    plt.setp(l4,  linewidth=6, markeredgewidth=1, marker='D', color='limegreen')
		    plt.setp(l5,  linewidth=6, markeredgewidth=1, marker='D', color='magenta')
		    plt.setp(l6,  linewidth=6, markeredgewidth=1, marker='D', color='brown')
		    plt.setp(l7,  linewidth=6, markeredgewidth=1, marker='D', color='navy')
		    plt.setp(l8,  linewidth=6, markeredgewidth=1, marker='D', color='orange')
		    plt.setp(l9,  linewidth=6, markeredgewidth=1, marker='D', linestyle='--', color='black')
		    plt.setp(l10, linewidth=6, markeredgewidth=1, marker='D', linestyle='--', color='silver')
		    plt.setp(l11, linewidth=6, markeredgewidth=1, marker='D', linestyle='--', color='gray')
		    plt.setp(l12, linewidth=6, markeredgewidth=1, marker='D', color='black')

		    plt.fill_between(time_, data10, data11, facecolor='slategray',
				     alpha=0.2, interpolate=True)

		    fig.suptitle(u'Previsão de vazão dos modelos climáticos - {0}_{1}{2} \n {3}/2017 - Usina: {4}'
				 u' (CLIM 1981-2010)'.format(typ.upper(), scale.upper(), method.upper(), month.upper(),
							     basin.upper()), fontsize=32, fontweight='bold', y=0.97)

		    plt.xlabel(u'Meses', fontsize=25, fontweight='bold')
		    plt.ylabel(u'Vazão $\mathregular{(m^3/s)}$', fontsize=25, fontweight='bold')

		    objects = dic_mon[mon]
		    
		    plt.xticks(time_, objects, fontsize=30, fontweight='bold')
		    plt.tick_params(axis='both', which='major', labelsize=25, length=4, width=2, pad=4,
				    labelcolor='k')
		    legend = (u'echam46'.upper(), u'cmc1'.upper(), u'cmc2'.upper(), u'ccsm3'.upper(), u'ccsm4'.upper(),
			      u'gfdl'.upper(), u'nasa'.upper(), u'ncep'.upper(), u'clim_ons'.upper(),
			      u'p33_ons'.upper(), u'p66_ons'.upper(), u'obs_ons'.upper())

		    font = FontProperties(size=20, weight='bold')
		    plt.figlegend(a, legend, loc=8, ncol=12, prop=font)
							
		    target_date = date(year, mon, 01)
		    ini_rundate, star_fcstdate, end_fcstdate = define_dates(target_date)

		    path_out = (home + "/leidinice/results/vazpast/monthly/plume_graphs/{0}_{1}{2}/{3}/{4}/".format(typ, scale, method, month, macro))

		    if not os.path.exists(path_out):
				create_path(path_out)

		    graph = 'plume_flow_all_models_{0}_{1}{2}_{3}_{4}_{5}_{6}.png'.format(typ, scale, method, ini_rundate[0:-2], star_fcstdate[0:-2], end_fcstdate[0:-2], basin)

		    if not os.path.exists(path_out+graph):
				plt.savefig(os.path.join(path_out, graph), bbox_inches='tight')
			print 'done ------------>', path_out+graph
			
		    else:
				print 'file exists -----> {0}'.format(path_out+graph)
			pass




