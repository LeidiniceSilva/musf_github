# -*- coding: utf-8 -*-

""" Compute best indices of ons and smap flow. """

import os
import netCDF4
import texttable as tt
from pylab import *
from datetime import datetime
from basins_names_code import basins_flow
from hidropy.utils.hidropy_utils import basin_dict
from PyFuncemeClimateTools import ClimateStats as cs


__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "19/05/2017"
__description__ = "Compute climatology of fluviometric flow for kind month of the year"

scale = 'monthly'
param = 'flow'
home  = os.path.expanduser("~")
hidropy_path = "/home/leidinice/documentos/projetos_git_funceme"


def all_indices(basin_code, list_idx):
    indices = []
    idx     = -1
    while True:
        try:
            idx = list_idx.index(basin_code, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices


def load_flow_obs_ons(basin_name, mon):

    path_in  = '{0}/io/flow/smap_monthly/'.format(home)
    flow_obs = 'vazoes_jun.asc'

    imp_data = np.loadtxt(path_in+flow_obs)
    list_idx = list(imp_data[:, 0])

    basin_code = basins_flow[basin_name]
    idx_list   = all_indices(basin_code, list_idx)
    # print basin_code
    # print basin_name
    # exit()

    data_aux   = imp_data[idx_list[0]:idx_list[-1] + 1, :]
    list_years = list(imp_data[idx_list[0]:idx_list[-1] + 1, 1])
    idx_flow   = []

    for y in range(1981, 2010 + 1):
        idx_flow.append((all_indices(y, list_years))[0])

    var = data_aux[idx_flow[0]:idx_flow[-1]+1, 2:][:, mon-1]

    return var


path_smap  = "/home/leidinice/io/flow/smap_monthly/vazao_simulada/"
q_sim_list = os.listdir(path_smap)

for mon in range(1, 12 + 1):
    print mon

    tab = tt.Texttable()
    tab_inform = [[]]

    path_smap  = "/home/leidinice/io/flow/smap_monthly/vazao_simulada/"
    q_sim_list = os.listdir(path_smap)

    for q_sim in q_sim_list:
        q_s = os.path.join(path_smap, q_sim)
        imp_data_smap = np.loadtxt(q_s)[:]

        basin_fullname = q_sim.split('.asc')[0].split('q_simulada_')[1]
        basin_name     = basin_dict(basin_fullname)[1]
        print basin_fullname

        years = imp_data_smap[:, 0]
        idx_years_in = np.where(1980 < years)[0][0]
        idx_years_fi = np.where(2011 > years)[0][-1]

        link1     = home + "/io/flow/smap_monthly/obs/{0}".format(basin_name)
        arq1      = "{0}/{1}_{2}_bases_obs_19810115_20170615_smap_{3}.nc".format(link1, param, scale, basin_fullname)
        data1     = netCDF4.Dataset(arq1)
        variable1 = data1.variables[param][:].T
        time1     = data1.variables['time']
        obs1      = variable1[0:360]

        obs_smap_old = obs1[mon - 1::12]
        obs_smap_new = imp_data_smap[idx_years_in:idx_years_fi + 1, 2][mon - 1::12]
        obs_ons      = load_flow_obs_ons(basin_fullname, mon)

        rmse_old = cs.compute_rmse(obs_smap_old, obs_ons)
        rmse_new = cs.compute_rmse(obs_smap_new, obs_ons)

        corr_old   = np.corrcoef(obs_smap_old, obs_ons)
        correl_old = np.array([round(corr_old[0][1], 3)])
        corr_new   = np.corrcoef(obs_smap_new, obs_ons)
        correl_new = np.array([round(corr_new[0][1], 3)])

        rmse_str  = ['OBS_OLD', 'OBS_NEW', 'OBS_ONS']
        rmse_list = [rmse_old, rmse_new]
        # best_result_rmse = rmse_str[np.where(rmse_list == np.min(rmse_list))[-1][-1]]
        # tab_inform_rmse.append([basin_fullname, rmse_old, rmse_new, best_result_rmse])

        corr_str  = ['OBS_OLD', 'OBS_NEW', 'OBS_ONS']
        corr_list = [correl_old[0], correl_new[0]]

        best_result_rmse = rmse_str[np.where(rmse_list == np.min(rmse_list))[-1][-1]]
        best_result_corr = corr_str[np.where(corr_list == np.max(corr_list))[-1][-1]]

        tab_inform.append([basin_fullname, rmse_old, rmse_new, best_result_rmse, correl_old, correl_new, best_result_corr])

    # tab.add_rows(tab_inform_rmse)
    # tab.set_cols_align(['c', 'c', 'c', 'c'])
    # tab.header(['Nome da Usina', 'RMSE OBS_OLD', 'RMSE OBS_NEW', 'Melhor Indice'])

    tab.add_rows(tab_inform)
    tab.set_cols_align(['c', 'c', 'c', 'c', 'c', 'c', 'c'])
    tab.header(['Nome da Usina', 'RMSE OBS_OLD', 'RMSE OBS_NEW', 'Melhor Indice', 'CORR OBS_OLD', 'CORR OBS_NEW', 'Melhor Indice'])

    table = str(tab.draw())

    date_aux  = datetime(1981, mon, 15)
    str_mon   = date_aux.strftime("%b").capitalize()
    dir_file  = '/home/leidinice/documentos/results/vazpast/indices_flow/rmse_corr/'
    file_name = '{1}best_rmse_corr_{0}.asc'.format(str_mon, dir_file)
    file_save = open(file_name, 'w')
    file_save.write(table)
    file_save.close()



