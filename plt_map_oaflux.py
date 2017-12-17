# -*- coding: utf-8 -*-

"""
This script plot mensal anomaly oaflux.
"""

import os
import netCDF4
import numpy as np
import matplotlib as mpl 

import matplotlib as mpl 
mpl.use('Agg')
import matplotlib.pyplot as plt

from datetime import datetime, date
from PyFuncemeClimateTools import PlotMaps as pm
from hidropy.utils.hidropy_utils import create_path
from matplotlib.font_manager import FontProperties

__author__ = "leidinice Silva"
__email__  = "leidinice.silva@funceme.br"
__date__   = "12/07/2017"
__description__ = "This script plot mensal anomaly oaflux"
 
    
def compute_anomaly(model, obs):

    """
    Retorna anomalia e anomalia padronizada
    model = array 1d ou 3d (previsão)
    obs = array 1d ou 3d (climatologia)
    """

    # Climatology average
    y_mean = np.nanmean(obs, axis=0)

    # Standard deviation
    y_std = np.nanstd(obs, axis=0)

    # Anomaly
    anom = model - y_mean

    # Standard anomaly
    anom_pad = (model - y_mean)/y_std

    return anom, anom_pad


# Plot time series per region 
reg_ninos = ['nino1+2', 'nino3', 'nino3.4', 'nino4', 'nino_modokiA','nino_modokiB', 'nino_modokiC']

for reg_nino in reg_ninos:
	print reg_nino
	
	# Open and reading file
	path1 = "/home/leidinice/documentos/oaflux/dados/evapr/"
	file1 = 'evapr_oaflux_2017rt_{0}.nc'.format(reg_nino)
	data1 = netCDF4.Dataset(str(path1) + file1)
	var1  = data1.variables['evapr'][:,:,:]
	lat = data1.variables['lat'][:] 
	lon = data1.variables['lon'][:] 	
	data_ini1 = np.nanmean(var1, axis=1)
	data_end1 = np.nanmean(data_ini1, axis=1)
	
	path2 = "/home/leidinice/documentos/oaflux/dados/lh/"
	file2 = 'lh_oaflux_2017rt_{0}.nc'.format(reg_nino)
	data2 = netCDF4.Dataset(str(path2) + file2)
	var2  = data2.variables['lhtfl'][:,:,:]
	lat = data2.variables['lat'][:] 
	lon = data2.variables['lon'][:] 	
	data_ini2 = np.nanmean(var2, axis=1)
	data_end2 = np.nanmean(data_ini2, axis=1)
	
	path3 = "/home/leidinice/documentos/oaflux/dados/qa/"
	file3 = 'qa_oaflux_2017rt_{0}.nc'.format(reg_nino)
	data3 = netCDF4.Dataset(str(path3) + file3)
	var3  = data3.variables['hum2m'][:,:,:]
	lat = data3.variables['lat'][:] 
	lon = data3.variables['lon'][:] 	
	data_ini3 = np.nanmean(var3, axis=1)
	data_end3 = np.nanmean(data_ini3, axis=1)
	
	path4 = "/home/leidinice/documentos/oaflux/dados/sh/"
	file4 = 'sh_oaflux_2017rt_{0}.nc'.format(reg_nino)
	data4 = netCDF4.Dataset(str(path4) + file4)
	var4  = data4.variables['shtfl'][:,:,:]
	lat = data4.variables['lat'][:] 
	lon = data4.variables['lon'][:] 	
	data_ini4 = np.nanmean(var4, axis=1)
	data_end4 = np.nanmean(data_ini4, axis=1)
	
	path5 = "/home/leidinice/documentos/oaflux/dados/ts/"
	file5 = 'ts_oaflux_2017rt_{0}.nc'.format(reg_nino)
	data5 = netCDF4.Dataset(str(path5) + file5)
	var5  = data5.variables['tmpsf'][:,:,:]
	lat = data5.variables['lat'][:] 
	lon = data5.variables['lon'][:] 	
	data_ini5 = np.nanmean(var5, axis=1)
	data_end5 = np.nanmean(data_ini5, axis=1)
		
	path6 = "/home/leidinice/documentos/oaflux/dados/ws/"
	file6 = 'ws_oaflux_2017rt_{0}.nc'.format(reg_nino)
	data6 = netCDF4.Dataset(str(path6) + file6)
	var6  = data6.variables['wnd10'][:,:,:]
	lat = data6.variables['lat'][:] 
	lon = data6.variables['lon'][:] 	
	data_ini6 = np.nanmean(var6, axis=1)
	data_end6 = np.nanmean(data_ini6, axis=1)

	# Plot figure of time siries per nino region
	fig = plt.figure(figsize=(16,8))
	time = np.arange(1, 6 + 1)
	
	a1 = plt.plot(time, data_end1, time, data_end2, time, data_end3, 
				  time, data_end4 ,time, data_end5, time, data_end6)
	
	l1, l2, l3, l4, l5, l6 = a1
	plt.setp(l1,  linewidth=2, markeredgewidth=1, marker='o', color='black')
	plt.setp(l2,  linewidth=2, markeredgewidth=1, marker='o', color='blue')
	plt.setp(l3,  linewidth=2, markeredgewidth=1, marker='o', color='red')
	plt.setp(l4,  linewidth=2, markeredgewidth=1, marker='o', color='green')
	plt.setp(l5,  linewidth=2, markeredgewidth=1, marker='o', color='orange')
	plt.setp(l6,  linewidth=2, markeredgewidth=1, marker='o', color='gray')
	
	plt.title(u'Air-water interface fluxs - {0}'.format(reg_nino.upper()),
			  fontsize=16, fontweight='bold')
			  	
	plt.xlabel(u'Months', fontsize=16, fontweight='bold')
	plt.ylabel(u'Fluxs', fontsize=16, fontweight='bold')
	
	objects = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
	plt.xticks(time, objects, fontsize=16, fontweight='bold')
	
	font = FontProperties(size=10)
	plt.legend([u'evapr', u'lh',u'qa', u'sh', u'ts', u'ws'],
				loc='best', ncol=2, prop=font)
	
	path_out1 = "/home/leidinice/documentos/oaflux/results/{0}/".format(reg_nino)

	if not os.path.exists(path_out1):
		create_path(path_out1)

	graph_ts = 'plt_time_serie_oaflux_{0}_2017.png'.format(reg_nino)
	plt.savefig(os.path.join(path_out1, graph_ts), bbox_inches='tight')
	plt.close()

	
# Plot map per region
var_names = ['evapr', 'lh', 'qa', 'sh', 'ts', 'ws']

for var_name in var_names:
	print var_name
	
	dic_vars  = {u'evapr': u'evapr',
				 u'lh': u'lhtfl',
				 u'qa': u'hum2m',
				 u'sh': u'shtfl',
				 u'ts': u'tmpsf',
				 u'ws': u'wnd10'}

	dic_title_vars  = {u'evapr': u'Evaporation',
					   u'lh': u'Latent heat flux',
					   u'qa': u'Air humidity 2m',
					   u'sh': u'sensible heat flux',
					   u'ts': u'Sea temperature surface',
					   u'ws': u'Wind speed 10m'}

	for mon in range(0,6):
		month = mon+1
		target_date = datetime(2017, month, 01)
		str_mon = target_date.strftime("%b").lower()
		print str_mon
		
		dic_mon = {u'jan': u'jan',
				   u'feb': u'feb',
				   u'mar': u'mar',
				   u'apr': u'apr',
				   u'may': u'may',
				   u'jun': u'jun',
				   u'jul': u'jul'}

		# Open and reading files
		path_in = "/home/leidinice/documentos/oaflux/dados/{0}/".format(var_name)

		file_hind = '{0}_oaflux_8110.nc'.format(var_name)
		data_hind = netCDF4.Dataset(str(path_in) + file_hind)
		var_hind  = data_hind.variables[dic_vars[var_name]][:,:,:]
		lat = data_hind.variables['lat'][:] 
		lon = data_hind.variables['lon'][:]
		mon_clim = var_hind[mon::12][:,:,:]

		file_fcst = '{0}_oaflux_2017rt.nc'.format(var_name)
		data_fcst = netCDF4.Dataset(str(path_in) + file_fcst)
		var_fcst  = data_fcst.variables[dic_vars[var_name]][:,:,:]
		lat = data_fcst.variables['lat'][:] 
		lon = data_fcst.variables['lon'][:]
		mon_fcst = var_fcst[mon,:,:]
				 
		ano, ano_pad = compute_anomaly(mon_fcst, mon_clim)

		# Plot figure of anomaly
		fig = plt.figure(figsize=(16,8))

		path_out2  = "/home/leidinice/documentos/oaflux/results/anom_maps/{0}".format(var_name)
		
		if not os.path.exists(path_out2):
			create_path(path_out2)
				
		fig_title = u'{0} - Anomaly Flux - {1}/2017'.format(dic_title_vars[var_name], dic_mon[str_mon].upper())
		fig_out = (os.path.join(path_out2, '{0}_anomaly_oaflux_{1}.png'.format(var_name, dic_mon[str_mon])))
		
		ano_map = pm.plotmap(ano, lat, lon, fig_title=fig_title,
							 barinf='both', barloc='right', fig_name=fig_out)
							 				 
		plt.close()


			
		
		




			  





