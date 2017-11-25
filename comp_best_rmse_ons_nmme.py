# -*- coding: utf-8 -*-

""" Compute best indices of ons and smap flow. """

import os
import glob
import calendar
import netCDF4
import texttable as tt

from pylab import *
from netCDF4 import Dataset
from dateutil.relativedelta import *
from datetime import datetime, date
from hidropy.utils.hidropy_utils import date2index, basin_dict
from PyFuncemeClimateTools import ClimateStats as cs

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "19/05/2017"
__description__ = "Compute best indices of ons and smap flow"

scale = 'monthly'
param = 'flow'
home  = os.path.expanduser("~")
hidropy_path = "/home/leidinice/documentos/projetos_git_funceme"


def define_dates(target_date_in, target_date_st, target_date_fi):

    target_ifcstdate = target_date_st + relativedelta(months=1)
    target_efcstdate = target_date_fi + relativedelta(months=3)

    start_rundate = '{0}{1:02d}{2:02d}'.format(target_date_in.year, target_date_in.month, target_date_in.day)
    star_fcstdate = '{0}{1:02d}{2:02d}'.format(target_ifcstdate.year, target_ifcstdate.month, target_ifcstdate.day)
    end_fcstdate  = '{0}{1:02d}{2:02d}'.format(target_efcstdate.year, target_efcstdate.month, target_efcstdate.day)

    return start_rundate, star_fcstdate, end_fcstdate


for m in range(1, 12 + 1):
    print datetime(1982, m, 01).strftime("%b").lower()

    models = ['cmc1-cancm3', 'cmc2-cancm4', 'cola-rsmas-ccsm3', 'cola-rsmas-ccsm4', 'gfdl-cm2p5-flor-b01',
              'nasa-gmao-062012']

    for model in models:
        print model

        tab = tt.Texttable()
        tab_inform = [[]]

        macros_total = ['amazonas', 'atlantico_leste', 'atlantico_sudeste', 'atlantico_sul', 'doce', 'grande', 'iguacu',
                        'jacui', 'paraguai', 'paraiba_do_sul', 'parana', 'paranaiba', 'paranapanema', 'parnaiba',
                        'sao_francisco', 'tiete', 'tocantins', 'uruguai']

        for macro in macros_total:
            folders = os.listdir("{0}/hidropy/hidropy/shapes/basins/".format(hidropy_path))
            basins  = sorted(basin_dict(micro=True, basin_name=macro))
            print macro

            bas_new1 = []
            for bas1 in basins:
                if '_henry' not in (bas1):
                    bas_new1.append(bas1)

            bas_new2 = []
            for bas2 in bas_new1:
                if '_richa' not in (bas2):
                    bas_new2.append(bas2)

            bas_new = []
            for bas in bas_new2:
                if '_inc' not in (bas):
                    bas_new.append(bas)

            for basin in bas_new:
                
		basin_fullname = basin_dict(basin)[2]
                basin_name     = basin_dict(basin)[1]

                link1 = home + "/io/flow/ons_monthly/1981-present/{0}".format(basin_name)
                arq1  = "{0}/{1}_{2}_ons_obs_19810115_20170615_{3}.nc".format(link1, param, scale, basin_fullname)
                data1 = netCDF4.Dataset(arq1)
                time1 = data1.variables['time']

                if m in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

                    iidx = date2index(datetime(1982, 01, 01), time1)
                    fidx = date2index(datetime(2010, 12, 31), time1)
                    variable1 = data1.variables[param][iidx:fidx + 1]

                    ons_obs1 = variable1[m + 0::12]
                    ons_obs2 = variable1[m + 1::12]
                    ons_obs3 = variable1[m + 2::12]
                    ons_obs  = np.nanmean((ons_obs1, ons_obs2, ons_obs3), axis=0)

                if m == 10:

                    iidx = date2index(datetime(1982, 01, 01), time1)
                    fidx = date2index(datetime(2010, 12, 31), time1)
                    variable1 = data1.variables[param][iidx:fidx + 1]

                    iidx_next  = date2index(datetime(1983, 01, 01), time1)
                    fidx_next  = date2index(datetime(2011, 12, 31), time1)
                    variable11 = data1.variables[param][iidx_next:fidx_next + 1]

                    ons_obs1 = variable1[m + 0::12]
                    ons_obs2 = variable1[m + 1::12]
                    ons_obs3 = variable11[m - 10::12]
                    ons_obs  = np.nanmean((ons_obs1, ons_obs2, ons_obs3), axis=0)

                if m == 11:

                    iidx = date2index(datetime(1982, 01, 01), time1)
                    fidx = date2index(datetime(2010, 12, 31), time1)
                    variable1 = data1.variables[param][iidx:fidx + 1]

                    iidx_next  = date2index(datetime(1983, 01, 01), time1)
                    fidx_next  = date2index(datetime(2011, 12, 31), time1)
                    variable11 = data1.variables[param][iidx_next:fidx_next + 1]

                    ons_obs1 = variable1[m + 0::12]
                    ons_obs2 = variable11[m - 11::12]
                    ons_obs3 = variable11[m - 10::12]
                    ons_obs  = np.nanmean((ons_obs1, ons_obs2, ons_obs3), axis=0)

                if m == 12:

                    iidx_next  = date2index(datetime(1983, 01, 01), time1)
                    fidx_next  = date2index(datetime(2011, 12, 31), time1)
                    variable11 = data1.variables[param][iidx_next:fidx_next + 1]

                    ons_obs1 = variable11[m - 12::12]
                    ons_obs2 = variable11[m - 11::12]
                    ons_obs3 = variable11[m - 10::12]
                    ons_obs  = np.nanmean((ons_obs1, ons_obs2, ons_obs3), axis=0)

                # print ons_obs1
                # print "break"
                # print ons_obs2
                # print "break"
                # print ons_obs3

                crude       = []
                cor_flow    = []
                cor_pr      = []
                cor_pr_flow = []
		
                for y in range(1982, 2010 + 1):

                    date_aux = datetime(1982, m, 01)
                    month    = date_aux.strftime("%b").lower()

                    target_rundate_in = datetime(y, m, 01)
                    target_rundate_st = datetime(y, m, 15)
                    target_rundate_fi = datetime(y, m, 15)
                    start_rundate, start_fcstdate, end_fcstdate = define_dates(target_rundate_in, target_rundate_st,
                                                                               target_rundate_fi)

                    link2 = home + "/io/flow/smap_monthly/nmme/{0}/{1}/{2}".format(model, month, basin_name)
                    arq2  = "{0}/flow_monthly_{1}_hind8210_fcst_{2}_{3}_{4}_smap_{5}." \
                           "nc".format(link2, model, start_rundate, start_fcstdate, end_fcstdate, basin_fullname)
                    data2     = netCDF4.Dataset(arq2)
                    variable2 = data2.variables[param][:]
                    time2     = data2.variables['time']
                    crude.append(np.nanmean(variable2))

                    cor_flow = []
                    link3 = home + "/io/flow/smap_monthly_cor_flow/nmme/{0}/{1}/{2}".format(model, month, basin_name)
                    arq3  = "{0}/flow_monthly_{1}_hind8210_fcst_{2}_{3}_{4}_smap_{5}" \
                           .format(link3, model, start_rundate, start_fcstdate, end_fcstdate, basin_fullname)
                    arq_new3  = arq3 + "_cor_flow.nc"
                    data3     = netCDF4.Dataset(arq_new3)
                    variable3 = data3.variables[param][:]
                    time3     = data3.variables['time']
                    cor_flow.append(np.nanmean(variable3))

                    cor_pr = []
                    link4 = home + "/io/flow/smap_monthly_cor_pr/nmme/{0}/{1}/{2}".format(model, month, basin_name)
                    arq4  = "{0}/flow_monthly_{1}_hind8210_fcst_{2}_{3}_{4}_smap_{5}" \
                           .format(link4, model, start_rundate, start_fcstdate, end_fcstdate, basin_fullname)
                    arq_new4  = arq4 + "_cor_pr.nc"
                    data4     = netCDF4.Dataset(arq_new4)
                    variable4 = data4.variables[param][:]
                    time4     = data4.variables['time']
                    cor_pr.append(np.nanmean(variable4))

                    cor_pr_flow = []
                    link5 = home + "/io/flow/smap_monthly_cor_pr_flow/nmme/{0}/{1}/{2}".format(model, month, basin_name)
                    arq5  = "{0}/flow_monthly_{1}_hind8210_fcst_{2}_{3}_{4}_smap_{5}" \
                           .format(link5, model, start_rundate, start_fcstdate, end_fcstdate, basin_fullname)
                    arq_new5  = arq5 + "_cor_pr_flow.nc"
                    data5     = netCDF4.Dataset(arq_new5)
                    variable5 = data5.variables[param][:]
                    time5     = data5.variables['time']
                    cor_pr_flow.append(np.nanmean(variable5))

                    # print variable2, "echam_bruto"
                    # print "break"
                    # print variable3, "cor_flow"
                    # print "break"
                    # print variable4, "cor_pr"
                    # print "break"

                rmse_crude       = (cs.compute_rmse(np.array(crude), np.array(ons_obs)))
                rmse_cor_flow    = (cs.compute_rmse(np.array(cor_flow), np.array(ons_obs)))
                rmse_cor_pr      = (cs.compute_rmse(np.array(cor_pr), np.array(ons_obs)))
                rmse_cor_pr_flow = (cs.compute_rmse(np.array(cor_pr_flow), np.array(ons_obs)))
                # print rmse_crude, rmse_cor_flow, rmse_cor_pr, rmse_cor_pr_flow

                rmse_str         = ['CRUDE', 'COR_FLOW', 'COR_PR', 'COR_PR_FLOW', 'OBS_ONS']
                rmse_list        = [rmse_crude, rmse_cor_flow, rmse_cor_pr, rmse_cor_pr_flow]
                best_result_rmse = rmse_str[np.where(rmse_list == np.min(rmse_list))[-1][-1]]
                tab_inform.append([basin_fullname, rmse_crude, rmse_cor_flow, rmse_cor_pr, rmse_cor_pr_flow, best_result_rmse])

        tab.add_rows(tab_inform)
        tab.set_cols_align(['c', 'c', 'c', 'c', 'c', 'c'])
        tab.header(['Nome da Usina', 'RMSE CRUDE', 'RMSE COR_FLOW', 'RMSE COR_PR', 'RMSE COR_PR_FLOW', 'Melhor Indice'])
        table = str(tab.draw())

        dir_file  = "/home/leidinice/documentos/results/nmme/best_rmse/{0}/".format(model)
        file_name = '{1}best_rmse_{0}.asc'.format(datetime(1982, m, 01).strftime("%b").lower(), dir_file)
        file_save = open(file_name, 'w')
        file_save.write(table)
        file_save.close()
    print "next month"
