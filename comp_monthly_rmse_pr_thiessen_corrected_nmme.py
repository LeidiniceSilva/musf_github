# -*- coding: utf-8 -*-

""" RMSE of bias correction by many different types for pr_thiessen NMME. """

import os
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
__date__   = "30/03/2017"
__description__ = " RMSE of bias correction by many different types for pr_thiessen echam46 "

scale  = 'monthly'
month  = 'nov'
mon    = 'nov'
param  = 'pr'
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

    if (len(obs_nozero) < 10) or (len(mod) < 10):
        print 'Error in the obs length: {}'.format(len(obs_nozero))

    alpha_mod, loc_mod, beta_mod = ss.gamma.fit(mod, floc=0)
    alpha_obs, loc_obs, beta_obs = ss.gamma.fit(obs_nozero, floc=0)

    corrected_fcst = []
    for ii in fcst:
        if flag:
            if ii >= cutoff_hind:
                prob = q + (1 - q) * (ss.gamma.cdf(ii, alpha_mod, scale=beta_mod))
                corrected_fcst.append(ss.gamma.ppf(prob, alpha_obs, scale=beta_obs))
            else:
                corrected_fcst.append(0.)
        else:
            if ii != 0.0:
                prob = q + (1 - q) * (ss.gamma.cdf(ii, alpha_mod, scale=beta_mod))
                corrected_fcst.append(ss.gamma.ppf(prob, alpha_obs, scale=beta_obs))
            else:
                corrected_fcst.append(obs_nozero[0])
    return corrected_fcst


def gumbel_correction(hind, clim_obs, fcst):
    hind = hind[np.nonzero(hind)]
    hind = hind[~np.isnan(hind)]
    zeros_obs = clim_obs[np.where(clim_obs == 0.)]

    q = len(zeros_obs) / np.float(len(clim_obs))
    obs_nozero = clim_obs[np.nonzero(clim_obs)]

    if (len(obs_nozero) < 10) or (len(hind) < 10):
        print 'Error in the obs length: {}'.format(len(obs_nozero))

    sh_mod = np.nanstd(hind) * np.pi / np.sqrt(6)
    sh_obs = np.nanmean(obs_nozero) - 0.57721 * sh_mod

    corrected_fcst_gumbel = []

    for i in fcst:

        if i == 0.0:
            corrected_fcst_gumbel.append(np.copy(i))
        else:
            prob = q + (1 - q) * (ss.genextreme.cdf(i, 1.5, loc=sh_mod, scale=sh_mod))
            corrected_fcst_gumbel.append(ss.genextreme.ppf(prob, 1.5, loc=sh_obs, scale=sh_obs))
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

    if (len(obs_nozero) < 10) or (len(mod) < 10):
        print 'Error in the obs length: {}'.format(len(obs_nozero))

    alpha_mod, loc_mod, beta_mod = ss.gamma.fit(mod, floc=0)
    alpha_obs, loc_obs, beta_obs = ss.gamma.fit(obs_nozero, floc=0)

    corrected_fcst_gamma_desag = []
    for ii in fcst:
        if flag:
            if ii >= cutoff_hind:
                prob = q + (1 - q) * (ss.gamma.cdf(ii, alpha_mod, scale=beta_mod))
                corrected_fcst_gamma_desag.append(ss.gamma.ppf(prob, alpha_obs, scale=beta_obs))
            else:
                corrected_fcst_gamma_desag.append(0.)
        else:

            if ii != 0.0:
                prob = q + (1 - q) * (ss.gamma.cdf(ii, alpha_mod, scale=beta_mod))
                corrected_fcst_gamma_desag.append(ss.gamma.ppf(prob, alpha_obs, scale=beta_obs))
            else:
                corrected_fcst_gamma_desag.append(obs_nozero[0])

    return corrected_fcst_gamma_desag


print month
print "inc"

macros_total = ['amazonas', 'atlantico_leste', 'atlantico_sudeste', 'atlantico_sul', 'iguacu',
                'jacui', 'paraguai', 'paraiba_do_sul', 'parana', 'paranaiba', 'paranapanema', 'parnaiba',
                'sao_francisco', 'tiete', 'tocantins', 'uruguai']

macros_inc = ['amazonas', 'atlantico_leste', 'doce', 'iguacu', 'jacui', 'paraiba_do_sul', 'parana',
              'paranaiba', 'paranapanema', 'sao_francisco', 'tiete', 'tocantins', 'uruguai']

for macro in macros_inc:
    print macro

    folders = os.listdir("{0}/hidropy/hidropy/shapes/basins/".format(hidropy_path))
    basins  = sorted(basin_dict(micro=True, basin_name=macro))
    basin_name = macro

    # total
    # bas_new = []
    # for bas in basins:
    #     if '_inc' not in(bas):
    #         bas_new.append(bas)

    # inc
    bas_new = []
    for bas in basins:
        if '_inc' in (bas):
            bas_new.append(bas)

    len_bas = len(bas_new)

    models = ['cmc1-cancm3', 'cmc2-cancm4', 'cola-rsmas-ccsm3', 'cola-rsmas-ccsm4', 'gfdl-cm2p5-flor-b01',
              'nasa-gmao-062012', 'ncep-cfsv2']

    for model in models:
        print model

        GAMMA = []
        GUMBEL = []
        GAMMA_DESAG = []
        plot_lines = []

        for basin in bas_new:
            basin_fullname = basin_dict(basin)[2]
            macro_name     = basin_dict(basin)[1]
            print basin

            # open netcdf obs
            stc_obs1 = []
            stc_obs2 = []
            stc_obs3 = []
            stc_obs_acc = []

            link1 = home+"/io/inmet_ana_chirps/calibration/{0}/{1}_thiessen/{2}".format(scale, param, macro_name)
            arq1 = "{0}/{1}_{2}_inmet_ana_chirps_obs_19610101_20141231_thiessen_{3}.nc".format(link1, param, scale,
                                                                                               basin_fullname)

            data1 = netCDF4.Dataset(arq1)
            variable1 = data1.variables[param][:].T
            time1 = data1.variables['time']
            st1 = variable1[252:600] # 1982-2010
            st2 = variable1[264:603] # 1983-2011
            st3 = variable1[600:648] # 2011-2014
            st4 = variable1[612:648] # 2012-2014

            stc_obs1.append(st1[11::12])
            stc_obs2.append(st2[0::12])
            stc_obs3.append(st2[1::12])
            stc_obs_acc.append(st1[11::12] + st2[0::12] + st2[1::12])

            sto1 = []
            sto2 = []
            sto3 = []

            link2 = home + "/io/inmet_ana_chirps/operation/{0}/{1}_thiessen/{2}".format(scale, param, macro_name)
            arq2 = "{0}/{1}_{2}_inmet_ana_chirps_obs_20150101_20170228_thiessen_{3}.nc".format(link2, param, scale,
                                                                                               basin_fullname)
            data2 = netCDF4.Dataset(arq2)
            variable2 = data2.variables[param][:].T
            time2 = data2.variables['time']
            st5 = variable2[0:24] # 2015-2016
            st6 = variable2[0:26] # 2015-2017

            observ1 = np.full(72, np.nan) # 2011-2016
            observ1[0:48] = st3
            observ1[48:72] = st5

            observ2 = np.full(62, np.nan) # 2012-2017
            observ2[0:36] = st4
            observ2[36:62] = st6

            sto1.append(observ1[11::12])
            sto2.append(observ2[0::12])
            sto3.append(observ2[1::12])

            # open netcdf hind and fcst
            ste_hind1 = []
            ste_hind2 = []
            ste_hind3 = []
            ste_hind_acc = []

            link3 = home + "/io/nmme/{0}/{1}/{2}/{3}/{4}_thiessen/{5}".format(model, period, mon, scale, param,
                                                                              macro_name)
            for year1 in range(1982, 2011):

                start_date = date(year1, 12, 31)
                new_year   = start_date + relativedelta(months=2)
                new_year_y = str(new_year)[0:4] + str(new_year)[5:7] + str(new_year)[8:10]

                arq3 = "{0}/{1}_{2}_{3}_{4}_fcst_{5}1101_{5}1201_{6}_thiessen_{7}.nc".format(link3, param, scale,
                                                                                                 model, period, year1,
                                                                                                 new_year_y,
                                                                                                 basin_fullname)
                data3     = netCDF4.Dataset(arq3)
                variable3 = data3.variables[param][:]
                time3     = data3.variables['time']

                ste_hind1.append(variable3[0::3])
                ste_hind2.append(variable3[1::3])
                ste_hind3.append(variable3[2::3])
                ste_hind_acc.append(np.sum(variable3))

            # open netcdf fcst
            ste_fcst1 = []
            ste_fcst2 = []
            ste_fcst3 = []
            ste_fcst_acc = []

            pr_corrected_gamma_desag1 = []
            pr_corrected_gamma_desag2 = []
            pr_corrected_gamma_desag3 = []

            link4 = home + "/io/nmme/{0}/{1}/{2}/{3}/{4}_thiessen/{5}".format(model, period, mon, scale, param,
                                                                              macro_name)
            sto1_new = []
            sto2_new = []
            sto3_new = []

            for ia, year2 in enumerate(range(2011, 2017)):

                start_date_ = date(year2, 12, 31)
                new_year_   = start_date_ + relativedelta(months=2)
                new_year_y_ = str(new_year_)[0:4] + str(new_year_)[5:7] + str(new_year_)[8:10]

                arq4 = "{0}/{1}_{2}_{3}_{4}_fcst_{5}1101_{5}1201_{6}_thiessen_{7}.nc".format(link4, param, scale,
                                                                                             model, period, year2,
                                                                                             new_year_y_,
                                                                                             basin_fullname)
                try:
                    data4     = netCDF4.Dataset(arq4)
                    variable4 = data4.variables[param][:]
                    time4     = data4.variables['time']

                    ste_fcst1.append(variable4[0::3])
                    ste_fcst2.append(variable4[1::3])
                    ste_fcst3.append(variable4[2::3])
                    ste_fcst_acc.append(np.sum(variable4))

                    sto1_new.append(sto1[ia])
                    sto2_new.append(sto2[ia])
                    sto3_new.append(sto3[ia])
                except:
                    print "--->", arq4

            # Calculate vies by gammma, gumbe and desag. gamma
            pr_corrected_gamma1 = gamma_correction(np.squeeze(ste_hind1), stc_obs1[0], np.squeeze(ste_fcst1))
            pr_corrected_gamma2 = gamma_correction(np.squeeze(ste_hind2), stc_obs2[0], np.squeeze(ste_fcst2))
            pr_corrected_gamma3 = gamma_correction(np.squeeze(ste_hind3), stc_obs3[0], np.squeeze(ste_fcst3))

            pr_corrected_gumbel1 = gumbel_correction(np.squeeze(ste_hind1), stc_obs1[0], np.squeeze(ste_fcst1))
            pr_corrected_gumbel2 = gumbel_correction(np.squeeze(ste_hind2), stc_obs2[0], np.squeeze(ste_fcst2))
            pr_corrected_gumbel3 = gumbel_correction(np.squeeze(ste_hind3), stc_obs3[0], np.squeeze(ste_fcst3))

            pr_corrected_gamma_desag = gamma_desag_correction(np.squeeze(ste_hind_acc), np.squeeze(stc_obs_acc[0]), np.squeeze(ste_fcst_acc))
            pr_corrected_gamma_desag1.append((np.squeeze(ste_fcst1) / np.squeeze(ste_fcst_acc)) * pr_corrected_gamma_desag)
            pr_corrected_gamma_desag2.append((np.squeeze(ste_fcst2) / np.squeeze(ste_fcst_acc)) * pr_corrected_gamma_desag)
            pr_corrected_gamma_desag3.append((np.squeeze(ste_fcst3) / np.squeeze(ste_fcst_acc)) * pr_corrected_gamma_desag)

            # Calculate rmse obs x corrected (gamma, gumbel and desag. gamma)
            rmse_gamma1 = cs.compute_rmse(np.squeeze(ste_fcst1), np.squeeze(pr_corrected_gamma1))
            rmse_gamma2 = cs.compute_rmse(np.squeeze(ste_fcst2), np.squeeze(pr_corrected_gamma2))
            rmse_gamma3 = cs.compute_rmse(np.squeeze(ste_fcst3), np.squeeze(pr_corrected_gamma3))
            pr_corrected_gamma = np.array([rmse_gamma1, rmse_gamma2, rmse_gamma3])
            GAMMA.append(pr_corrected_gamma)

            rmse_gumbel1 = cs.compute_rmse(np.squeeze(ste_fcst1), np.squeeze(pr_corrected_gumbel1))
            rmse_gumbel2 = cs.compute_rmse(np.squeeze(ste_fcst2), np.squeeze(pr_corrected_gumbel2))
            rmse_gumbel3 = cs.compute_rmse(np.squeeze(ste_fcst3), np.squeeze(pr_corrected_gumbel3))
            pr_corrected_gumbel = np.array([rmse_gumbel1, rmse_gumbel2, rmse_gumbel3])
            GUMBEL.append(pr_corrected_gumbel)

            rmse_gamma_desag1 = cs.compute_rmse(np.squeeze(ste_fcst1), np.squeeze(pr_corrected_gamma_desag1[0]))
            rmse_gamma_desag2 = cs.compute_rmse(np.squeeze(ste_fcst2), np.squeeze(pr_corrected_gamma_desag2[0]))
            rmse_gamma_desag3 = cs.compute_rmse(np.squeeze(ste_fcst3), np.squeeze(pr_corrected_gamma_desag3[0]))
            pr_corrected_gamma_desagregada = np.array([rmse_gamma_desag1, rmse_gamma_desag2, rmse_gamma_desag3])
            GAMMA_DESAG.append(pr_corrected_gamma_desagregada)

            # print GAMMA
            # print GUMBEL
            # print GAMMA_DESAG
            # exit()

        # Generating comparative bar of pr thiessen
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
        objects = ['DEZ', 'JAN', 'FEV']

        for i in range(len(bas_new)):

            list_basins.append(bas_new[i].split('{0}_'.format(basin_name))[1].capitalize())

            fig.suptitle(u'Correções: GAMMA, GUMBEL e GAMMA DESAG. \n Modelo: {0} / Previsão: {1} - 2011_2016 \n Bacia:'
                         u' {2} - Usinas: Incrementais'.format(model.upper(), month.capitalize(), macro_name.capitalize()),
                         fontsize=250, fontweight='bold')

            count = (1 - len_bas * bar1w) / 2

            a = GAMMA[:, i]
            b = ax[0].bar(x + count + i * bar1w, a, bar1w, color=line_colors[i], label=i)
            ax[0].set_ylim([0, 400])
            ax[0].set_xlim([0, 3])
            ax[0].text(-0.20, 0, u'A)', fontsize=200, fontweight='bold')
            ax[0].set_ylabel(u'RMSE', fontsize=200, fontweight='bold')
            ax[0].set_xticks([0.5, 1.5, 2.5])
            ax[0].set_xticklabels(objects, fontsize=200, fontweight='bold')

            c = GUMBEL[:, i]
            d = ax[1].bar(y + count + i * bar2w, c, bar2w, color=line_colors[i], label=i)
            ax[1].set_ylim([0, 400])
            ax[1].set_xlim([0, 3])
            ax[1].text(-0.20, 0, u'B)', fontsize=200, fontweight='bold')
            ax[1].set_ylabel(u'RMSE', fontsize=200, fontweight='bold')
            ax[1].set_xticks([0.5, 1.5, 2.5])
            ax[1].set_xticklabels(objects, fontsize=200, fontweight='bold')

            e = GAMMA_DESAG[:, i]
            f = ax[2].bar(z + count + i * bar3w, e, bar3w, color=line_colors[i], label=i)
            ax[2].set_ylim([0, 400])
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
            ax[0].axhline(400, color='k')

            ax[1].axvline(0, color='k')
            ax[1].axvline(1, color='#808080')
            ax[1].axvline(2, color='#808080')
            ax[1].axvline(3, color='k')
            ax[1].axhline(0, color='k')
            ax[1].axhline(400, color='k')

            ax[2].axvline(0, color='k')
            ax[2].axvline(1, color='#808080')
            ax[2].axvline(2, color='#808080')
            ax[2].axvline(3, color='k')
            ax[2].axhline(0, color='k')
            ax[2].axhline(400, color='k')

            ax[0].tick_params(axis='both', which='major', labelsize=160, length=50, width=10, pad=50, labelcolor='k')
            ax[0].grid(True, which='major', linestyle='-.', linewidth='5')

            ax[1].tick_params(axis='both', which='major', labelsize=160, length=50, width=10, pad=50, labelcolor='k')
            ax[1].grid(True, which='major', linestyle='-.', linewidth='5')

            ax[2].tick_params(axis='both', which='major', labelsize=160, length=50, width=10, pad=50, labelcolor='k')
            ax[2].grid(True, which='major', linestyle='-.', linewidth='5')

        font = FontProperties(weight='bold', size=155)
        plt.figlegend(aux, list_basins, loc=8, ncol=6, prop=font)

        path_out = ('/home/leidinice/documentos/results/nmme/correc_rmse/{0}/{1}/{2}/{3}_'
                    'thiessen/{4}/incrementais/'.format(model, mon, scale, param, macro_name))

        if not os.path.exists(path_out):
            create_path(path_out)

        plt.savefig(os.path.join(path_out, '{0}_incrementais_indices_RMSE_{1}_thiessen_{2}_{3}_'
                                           '2011_2016.png'.format(macro_name, param, model, month)), dpi=25)

        plt.close('all')
        plt.cla()
