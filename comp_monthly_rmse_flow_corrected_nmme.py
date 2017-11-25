# -*- coding: utf-8 -*-

""" RMSE of bias correction by many different types for flow. """

import os
import argparse
import numpy as np
import scipy.stats as ss
import netCDF4
from datetime import date
from dateutil.relativedelta import relativedelta

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from PyFuncemeClimateTools import ClimateStats as cs
from hidropy.utils.hidropy_utils import basin_dict, create_path

__author__ = "Leidinice Silva"
__email__  = "leidinice.silvae@funceme.br"
__date__   = "17/04/2017"
__description__ = " RMSE of bias correction by many different types for flow "

scale  = 'monthly'
month  = 'dec'
mon    = 'dez'
param  = 'flow'
period = 'hind8210'
home   = os.path.expanduser("~")
hidropy_path = "/home/leidinice/documentos/projetos_git_funceme"


def gamma_correction(hind, clim_obs, fcst):
    hind = np.sort(hind)
    obs  = np.sort(clim_obs)

    n_obszeros = len(obs[np.where(obs == 0.0)])
    q = n_obszeros / np.float(len(obs))

    flag = False
    if n_obszeros > 0:
        q_obshind = len(hind) / np.float(len(obs))
        idx_hindzeros = int(n_obszeros * q_obshind)
        cutoff_hind = hind[idx_hindzeros - 1]
        mod = hind[idx_hindzeros:]
        mod = mod[np.nonzero(mod)]
        obs_nozero = obs[np.nonzero(obs)]
        flag = True
    else:
        mod = np.copy(hind)
        mod = mod[np.nonzero(mod)]
        obs_nozero = np.copy(obs)

    if (len(obs_nozero) > 15) or (len(mod) > 15):

        alpha_mod, loc_mod, beta_mod = ss.gamma.fit(mod, floc=0)
        alpha_obs, loc_obs, beta_obs = ss.gamma.fit(obs_nozero, floc=0)

        corrected_fcst_gamma = []
        for ii in fcst:
            if flag:
                if ii >= cutoff_hind:
                    prob = q + (1 - q) * (ss.gamma.cdf(ii, alpha_mod, scale=beta_mod))
                    if prob == 1.:
                        prob = 0.99
                    aux_corr = ss.gamma.ppf(prob, alpha_obs, scale=beta_obs)
                    if not np.isinf(aux_corr):
                        corrected_fcst_gamma.append(aux_corr)
                    else:
                        corrected_fcst_gamma.append(ii)
                else:
                    corrected_fcst_gamma.append(0.)
            else:
                if ii != 0.0:
                    prob = q + (1 - q) * (ss.gamma.cdf(ii, alpha_mod, scale=beta_mod))
                    if prob == 1.:
                        prob = 0.99
                    aux_corr = ss.gamma.ppf(prob, alpha_obs, scale=beta_obs)
                    if not np.isinf(aux_corr):
                        corrected_fcst_gamma.append(aux_corr)
                    else:
                        corrected_fcst_gamma.append(ii)
                else:
                    corrected_fcst_gamma.append(obs_nozero[0])
    else:
        print 'Error in the obs length: {}'.format(len(obs_nozero))
        corrected_fcst_gamma = np.copy(fcst)
    return corrected_fcst_gamma


def gumbel_correction(hind, clim_obs, fcst):
    hind = np.sort(hind)
    obs = np.sort(clim_obs)

    n_obszeros = len(obs[np.where(obs == 0.0)])
    q = n_obszeros / np.float(len(obs))

    flag = False
    if n_obszeros > 0:
        q_obshind = len(hind) / np.float(len(obs))
        idx_hindzeros = int(n_obszeros * q_obshind)
        cutoff_hind = hind[idx_hindzeros - 1]
        mod = hind[idx_hindzeros:]
        mod = mod[np.nonzero(mod)]
        obs_nozero = obs[np.nonzero(obs)]
        flag = True
    else:
        mod = np.copy(hind)
        mod = mod[np.nonzero(mod)]
        obs_nozero = np.copy(obs)

    if (len(obs_nozero) > 15) or (len(mod) > 15):

        sh_mod = np.nanstd(hind) * np.pi / np.sqrt(6)
        sh_obs = np.nanmean(obs_nozero) - 0.57721 * sh_mod

        corrected_fcst_gumbel = []
        for ii in fcst:
            if flag:
                if ii >= cutoff_hind:
                    prob = q + (1 - q) * (ss.genextreme.cdf(ii, 1.5, loc=sh_mod, scale=sh_mod))
                    if prob == 1.:
                        prob = 0.99
                    aux_corr = ss.genextreme.ppf(prob, 1.5, loc=sh_obs, scale=sh_obs)
                    if not np.isinf(aux_corr):
                        corrected_fcst_gumbel.append(aux_corr)
                    else:
                        corrected_fcst_gumbel.append(ii)
                else:
                    corrected_fcst_gumbel.append(0.)
            else:
                if ii != 0.0:
                    prob = q + (1 - q) * (ss.genextreme.cdf(ii, 1.5, loc=sh_mod, scale=sh_mod))
                    if prob == 1.:
                        prob = 0.99
                    aux_corr = ss.genextreme.ppf(prob, 1.5, loc=sh_obs, scale=sh_obs)
                    if not np.isinf(aux_corr):
                        corrected_fcst_gumbel.append(aux_corr)
                    else:
                        corrected_fcst_gumbel.append(ii)
                else:
                    corrected_fcst_gumbel.append(obs_nozero[0])
    else:
        print 'Error in the obs length: {}'.format(len(obs_nozero))
        corrected_fcst_gumbel = np.copy(fcst[0])
    return corrected_fcst_gumbel


def gamma_desag_correction(hind, clim_obs, fcst):
    hind = np.sort(hind)
    obs  = np.sort(clim_obs)

    n_obszeros = len(obs[np.where(obs == 0.0)])
    q = n_obszeros / np.float(len(obs))

    flag = False
    if n_obszeros > 0:
        q_obshind = len(hind) / np.float(len(obs))
        idx_hindzeros = int(n_obszeros * q_obshind)
        cutoff_hind = hind[idx_hindzeros - 1]
        mod = hind[idx_hindzeros:]
        mod = mod[np.nonzero(mod)]
        obs_nozero = obs[np.nonzero(obs)]
        flag = True
    else:
        mod = np.copy(hind)
        mod = mod[np.nonzero(mod)]
        obs_nozero = np.copy(obs)

    if (len(obs_nozero) > 15) or (len(mod) > 15):

        alpha_mod, loc_mod, beta_mod = ss.gamma.fit(mod, floc=0)
        alpha_obs, loc_obs, beta_obs = ss.gamma.fit(obs_nozero, floc=0)

        corrected_fcst_gamma_desag = []
        for ii in fcst:
            if flag:
                if ii >= cutoff_hind:
                    prob = q + (1 - q) * (ss.gamma.cdf(ii, alpha_mod, scale=beta_mod))
                    if prob == 1.:
                        prob = 0.99
                    aux_corr = ss.gamma.ppf(prob, alpha_obs, scale=beta_obs)
                    if not np.isinf(aux_corr):
                        corrected_fcst_gamma_desag.append(aux_corr)
                    else:
                        corrected_fcst_gamma_desag.append(ii)
                else:
                    corrected_fcst_gamma_desag.append(0.)
            else:
                if ii != 0.0:
                    prob = q + (1 - q) * (ss.gamma.cdf(ii, alpha_mod, scale=beta_mod))
                    if prob == 1.:
                        prob = 0.99
                    aux_corr = ss.gamma.ppf(prob, alpha_obs, scale=beta_obs)
                    if not np.isinf(aux_corr):
                        corrected_fcst_gamma_desag.append(aux_corr)
                    else:
                        corrected_fcst_gamma_desag.append(ii)
                else:
                    corrected_fcst_gamma_desag.append(obs_nozero[0])
    else:
        print 'Error in the obs length: {}'.format(len(obs_nozero))
        corrected_fcst_gamma_desag = np.copy(fcst)
    return corrected_fcst_gamma_desag


def arguments():
    global args

    parser = argparse.ArgumentParser(description=__description__)
    args = parser.parse_args()

if __name__ == '__main__':
    arguments()

    print month
    print "macros_total"

    macros_total = ['amazonas', 'atlantico_leste', 'atlantico_sudeste', 'atlantico_sul', 'doce', 'grande', 'iguacu',
                    'jacui', 'paraguai', 'paraiba_do_sul', 'parana', 'paranaiba', 'paranapanema', 'parnaiba',
                    'sao_francisco', 'tiete', 'tocantins', 'uruguai']

    macros_inc   = ['amazonas', 'atlantico_leste', 'doce', 'grande', 'iguacu', 'jacui', 'paraiba_do_sul', 'parana',
                    'paranaiba', 'paranapanema', 'sao_francisco', 'tiete', 'tocantins', 'uruguai']

    for macro in macros_total:
        print macro

        folders = os.listdir("{0}/hidropy/hidropy/shapes/basins/".format(hidropy_path))
        basins  = sorted(basin_dict(micro=True, basin_name=macro))
        basin_name = macro

        bas_new1 = []
        for bas1 in basins:
            if '_henry' not in (bas1):
                bas_new1.append(bas1)

        bas_new2 = []
        for bas2 in bas_new1:
            if '_jauru' not in (bas2):
                bas_new2.append(bas2)

        bas_new3 = []
        for bas3 in bas_new2:
            if '_xingo' not in (bas3):
                bas_new3.append(bas3)

        # total
        bas_new = []
        for bas in bas_new3:
            if '_inc' not in (bas):
                bas_new.append(bas)

        len_bas = len(bas_new)

        models = ['cmc1-cancm3', 'cmc2-cancm4', 'cola-rsmas-ccsm3', 'cola-rsmas-ccsm4', 'gfdl-cm2p5-flor-b01',
                  'nasa-gmao-062012']

        for model in models:
            print model

            GAMMA       = []
            GUMBEL      = []
            GAMMA_DESAG = []
            plot_lines  = []

            for basin in bas_new:
                basin_fullname = basin_dict(basin)[2]
                macro_name     = basin_dict(basin)[1]
                print basin

                # open netcdf obs
                stc_obs1    = []
                stc_obs2    = []
                stc_obs3    = []
                stc_obs_acc = []

                link1 = home + "/io/flow/smap_monthly/obs/{0}".format(macro_name)
                arq1 = "{0}/{1}_{2}_bases_obs_19810101_20170401_smap_{3}.nc".format(link1, param, scale,
                                                                                    basin_fullname)
                data1     = netCDF4.Dataset(arq1)
                variable1 = data1.variables[param][:].T
                time1     = data1.variables['time']
                st_obs1   = variable1[0:360]
                st_obs2   = variable1[12:372]

                stc_obs1.append(st_obs2[0::12])
                stc_obs2.append(st_obs2[1::12])
                stc_obs3.append(st_obs2[2::12])
                stc_obs_acc.append(st_obs2[0::12] + st_obs2[1::12] + st_obs2[2::12])

                # open netcdf hind and fcst
                ste_hind1 = []
                ste_hind2 = []
                ste_hind3 = []
                ste_hind_acc = []

                link2 = home + "/io/{0}/smap_{1}/nmme/{2}/{3}/{4}".format(param, scale, model, month, macro_name)

                for year1 in range(1982, 2011):

                    start_date  = date(year1, 12, 15)
                    new_year    = start_date + relativedelta(months=1)
                    new_year_   = start_date + relativedelta(months=3)
                    new_year_y  = str(new_year)[0:4] + str(new_year)[5:7] + str(new_year)[8:10]
                    new_year_y_ = str(new_year_)[0:4] + str(new_year_)[5:7] + str(new_year_)[8:10]

                    arq2 = "{0}/{1}_{2}_{3}_{4}_fcst_{5}1201_{6}_{7}_smap_{8}.nc".format(link2, param,  scale,
                                                                                         model, period, year1,
                                                                                         new_year_y, new_year_y_,
                                                                                         basin_fullname)
                    try:
                        arq_new2 = arq2 + "_petclim.nc"
                        data2 = netCDF4.Dataset(arq2)
                        variable2 = data2.variables[param][:]
                        time2 = data2.variables['time']

                        ste_hind1.append(variable2[0::3])
                        ste_hind2.append(variable2[1::3])
                        ste_hind3.append(variable2[2::3])
                        ste_hind_acc.append(np.sum(variable2))
                    except:
                        print "--->", arq2

                # open netcdf fcst
                ste_fcst1 = []
                ste_fcst2 = []
                ste_fcst3 = []
                ste_fcst_acc = []

                link3 = home + "/io/{0}/smap_{1}/nmme/{2}/{3}/{4}".format(param, scale, model, month, macro_name)
                for year2 in range(2011, 2017):

                    start_date  = date(year2, 12, 15)
                    new_year    = start_date + relativedelta(months=1)
                    new_year_   = start_date + relativedelta(months=3)
                    new_year_y  = str(new_year)[0:4] + str(new_year)[5:7] + str(new_year)[8:10]
                    new_year_y_ = str(new_year_)[0:4] + str(new_year_)[5:7] + str(new_year_)[8:10]

                    arq3 = "{0}/{1}_{2}_{3}_{4}_fcst_{5}1201_{6}_{7}_smap_{8}.nc".format(link3, param,  scale,
                                                                                                 model, period, year2,
                                                                                             new_year_y, new_year_y_,
                                                                                                 basin_fullname)
                    try:
                        arq_new3 = arq3+"_petclim.nc"
                        data3 = netCDF4.Dataset(arq3)
                        variable3 = data3.variables[param][:]
                        time3 = data3.variables['time']

                        ste_fcst1.append(variable3[0::3])
                        ste_fcst2.append(variable3[1::3])
                        ste_fcst3.append(variable3[2::3])
                        ste_fcst_acc.append(np.sum(variable3))
                    except:
                        print "--->", arq3

                flow_corrected_gamma_desag1 = []
                flow_corrected_gamma_desag2 = []
                flow_corrected_gamma_desag3 = []

                # Calculate vies by gammma, gumbe and desag. gamma
                flow_corrected_gamma1 = gamma_correction(np.squeeze(ste_hind1), np.squeeze(stc_obs1), np.squeeze(ste_fcst1))
                flow_corrected_gamma2 = gamma_correction(np.squeeze(ste_hind2), np.squeeze(stc_obs2), np.squeeze(ste_fcst2))
                flow_corrected_gamma3 = gamma_correction(np.squeeze(ste_hind3), np.squeeze(stc_obs3), np.squeeze(ste_fcst3))

                flow_corrected_gumbel1 = gumbel_correction(np.squeeze(ste_hind1), np.squeeze(stc_obs1), np.squeeze(ste_fcst1))
                flow_corrected_gumbel2 = gumbel_correction(np.squeeze(ste_hind2), np.squeeze(stc_obs2), np.squeeze(ste_fcst2))
                flow_corrected_gumbel3 = gumbel_correction(np.squeeze(ste_hind3), np.squeeze(stc_obs3), np.squeeze(ste_fcst3))

                flow_corrected_gamma_desag = gamma_desag_correction(np.squeeze(ste_hind_acc), np.squeeze(stc_obs_acc), np.squeeze(ste_fcst_acc))
                flow_corrected_gamma_desag1.append((np.squeeze(ste_fcst1) / np.squeeze(ste_fcst_acc)) * flow_corrected_gamma_desag)
                flow_corrected_gamma_desag2.append((np.squeeze(ste_fcst2) / np.squeeze(ste_fcst_acc)) * flow_corrected_gamma_desag)
                flow_corrected_gamma_desag3.append((np.squeeze(ste_fcst3) / np.squeeze(ste_fcst_acc)) * flow_corrected_gamma_desag)

                # Calculate rmse obs x corrected (gamma, gumbel and desag. gamma)
                rmse_gamma1 = cs.compute_rmse(np.squeeze(ste_fcst1), np.squeeze(flow_corrected_gamma1))
                rmse_gamma2 = cs.compute_rmse(np.squeeze(ste_fcst2), np.squeeze(flow_corrected_gamma2))
                rmse_gamma3 = cs.compute_rmse(np.squeeze(ste_fcst3), np.squeeze(flow_corrected_gamma3))
                rmse_corrected_gamma = np.array([rmse_gamma1, rmse_gamma2, rmse_gamma3])
                GAMMA.append(rmse_corrected_gamma)

                rmse_gumbel1 = cs.compute_rmse(np.squeeze(ste_fcst1), np.squeeze(flow_corrected_gumbel1))
                rmse_gumbel2 = cs.compute_rmse(np.squeeze(ste_fcst2), np.squeeze(flow_corrected_gumbel2))
                rmse_gumbel3 = cs.compute_rmse(np.squeeze(ste_fcst3), np.squeeze(flow_corrected_gumbel3))
                rmse_corrected_gumbel = np.array([rmse_gumbel1, rmse_gumbel2, rmse_gumbel3])
                GUMBEL.append(rmse_corrected_gumbel)

                rmse_gamma_desag1 = cs.compute_rmse(np.squeeze(ste_fcst1), np.squeeze(flow_corrected_gamma_desag1))
                rmse_gamma_desag2 = cs.compute_rmse(np.squeeze(ste_fcst2), np.squeeze(flow_corrected_gamma_desag2))
                rmse_gamma_desag3 = cs.compute_rmse(np.squeeze(ste_fcst3), np.squeeze(flow_corrected_gamma_desag3))
                rmse_corrected_gamma_desag = np.array([rmse_gamma_desag1, rmse_gamma_desag2, rmse_gamma_desag3])
                GAMMA_DESAG.append(rmse_corrected_gamma_desag)

            # Generating comparative bar of flow
            cmap = plt.cm.gray
            fig, ax = plt.subplots(3, figsize=(210, 180))
            w = 0.14

            GAMMA = np.array(GAMMA).T
            GUMBEL = np.array(GUMBEL).T
            GAMMA_DESAG = np.array(GAMMA_DESAG).T

            bar1 = len(GAMMA[:, 0])
            bar1w = w / bar1

            bar2 = len(GUMBEL[:, 0])
            bar2w = w / bar2

            bar3 = len(GAMMA_DESAG[:, 0])
            bar3w = w / bar3

            x = np.arange(len(GAMMA))
            y = np.arange(len(GUMBEL))
            z = np.arange(len(GAMMA_DESAG))

            line_colors = cmap(np.linspace(0, 3))
            labels = np.arange(len(bas_new))

            aux = []
            list_basins = []
            objects = ['JAN', 'FEV', 'MAR']

            for i in range(len(bas_new)):

                list_basins.append(bas_new[i].split('{0}_'.format(basin_name))[1].capitalize())

                fig.suptitle(u'Correções: GAMMA, GUMBEL e GAMMA DESAG. \n Modelo: {0} / Previsão: {1} - 2011_2016 '
                             u'\n Bacia: {2} - Usinas: Totais'.format(model.upper(), mon.capitalize(),
                                                                      macro_name.capitalize()),
                             fontsize=250, fontweight='bold')

                count = (1 - len_bas * bar1w) / 2

                a = GAMMA[:, i]
                b = ax[0].bar(x + count + i * bar1w, a, bar1w, color=line_colors[i], label=i)
                ax[0].set_ylim([0, 1500])
                ax[0].set_xlim([0, 3])
                ax[0].text(-0.20, 0, u'A)', fontsize=200, fontweight='bold')
                ax[0].set_ylabel(u'RMSE', fontsize=200, fontweight='bold')
                ax[0].set_xticks([0.5, 1.5, 2.5])
                ax[0].set_xticklabels(objects, fontsize=200, fontweight='bold')

                c = GUMBEL[:, i]
                d = ax[1].bar(y + count + i * bar2w, c, bar2w, color=line_colors[i], label=i)
                ax[1].set_ylim([0, 1500])
                ax[1].set_xlim([0, 3])
                ax[1].text(-0.20, 0, u'B)', fontsize=200, fontweight='bold')
                ax[1].set_ylabel(u'RMSE', fontsize=200, fontweight='bold')
                ax[1].set_xticks([0.5, 1.5, 2.5])
                ax[1].set_xticklabels(objects, fontsize=200, fontweight='bold')

                e = GAMMA_DESAG[:, i]
                f = ax[2].bar(z + count + i * bar3w, e, bar3w, color=line_colors[i], label=i)
                ax[2].set_ylim([0, 1500])
                ax[2].set_xlim([0, 3])
                ax[2].text(-0.20, 0, u'C)', fontsize=200, fontweight='bold')
                ax[2].set_ylabel(u'RMSE', fontsize=200, fontweight='bold')
                ax[2].set_xticks([0.5, 1.5, 2.5])
                ax[2].set_xticklabels(objects, fontsize=200, fontweight='bold')
                aux.append(f)

                ax[0].axvline(0, color='k')
                ax[0].axvline(1, color='#808080')
                ax[0].axvline(2, color='#808080')
                ax[0].axvline(3, color='k')
                ax[0].axhline(0, color='k')
                ax[0].axhline(1500, color='k')

                ax[1].axvline(0, color='k')
                ax[1].axvline(1, color='#808080')
                ax[1].axvline(2, color='#808080')
                ax[1].axvline(3, color='k')
                ax[1].axhline(0, color='k')
                ax[1].axhline(1500, color='k')

                ax[2].axvline(0, color='k')
                ax[2].axvline(1, color='#808080')
                ax[2].axvline(2, color='#808080')
                ax[2].axvline(3, color='k')
                ax[2].axhline(0, color='k')
                ax[2].axhline(1500, color='k')

                ax[0].tick_params(axis='both', which='major', labelsize=160, length=50, width=10, pad=50, labelcolor='k')
                ax[0].grid(True, which='major', linestyle='-.', linewidth='5')

                ax[1].tick_params(axis='both', which='major', labelsize=160, length=50, width=10, pad=50, labelcolor='k')
                ax[1].grid(True, which='major', linestyle='-.', linewidth='5')

                ax[2].tick_params(axis='both', which='major', labelsize=160, length=50, width=10, pad=50, labelcolor='k')
                ax[2].grid(True, which='major', linestyle='-.', linewidth='5')

            font = FontProperties(weight='bold', size=155)
            plt.figlegend(aux, list_basins, loc=8, ncol=6, prop=font)

            path_out = ("/home/leidinice/documentos/results/nmme/correc_rmse/{0}/{1}/{2}/{3}_smap/{4}/"
                        "totais/".format(model, month, scale, param, macro_name))

            if not os.path.exists(path_out):
                create_path(path_out)

            plt.savefig(os.path.join(path_out, '{0}_totais_indices_RMSE_{1}_smap_{2}_{3}_2011_2016'
                                               '.png'.format(macro_name, param, model, mon)), dpi=25)

            plt.close('all')
            plt.cla()
