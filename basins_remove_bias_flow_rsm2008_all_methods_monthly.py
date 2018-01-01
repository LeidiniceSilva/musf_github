# -*- coding: utf-8 -*-

# Author = 'Funceme'
# Credits = 'Leidinice Silva'
# Maintainer = 'Funceme'
# Date = 11/12/2017  (dd/mm/aaaa)
# Comment = 'Este script foi desenvolvido dentro do Termo de Cooperação
#            0050.0100467.16.9 entre Funceme e Petrobras sob o contexto do
#            Projeto Projeção de Vazão Natural Afluente com base na escala de
#            tempo e clima'
# Description = 'Dictionary of subbasins estatistical remove bias method for
#                each month.'


"""
Dictionary of subbasins estatistical remove bias method for each month.


Dictionary format:
    dict_remove_bias = {'basin': ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], ...}


Parameters description:

    jan: January
    feb: February
    mar: March
    apr: April
    may: May
    jun: June
    jul: July
    aug: August
    sep: Septembre
    oct: October
    nov: November
    dec: December

Each month must have one of the 4 strings below:

    cor_pr:      Value simulated with the precipitation corrected delivered of RSM2008 model.
    cor_flow:    Value simulated with the flow corrected delivered of RSM2008 model.
    cor_pr_flow: Value simulated with the flow corrected with the precipitation delivered of RSM2008 model.
    crude:       Crude value delivered from RSM2008 model.

Usage:
    Used in the removal of the bias of the flow data from the RSM2008 model.


Last update: 2017-12-11 16:23

"""

dict_remove_bias_rsm2008={

'amazonas_balbina':                                   [   'cor_flow',    'cor_flow',    'cor_flow',       'crude',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr'], 
'amazonas_belo_monte':                                ['cor_pr_flow',    'cor_flow',       'crude',       'crude', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'amazonas_cachoeira_caldeirao':                       [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'amazonas_coaracy_nunes':                             [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'amazonas_colider':                                   ['cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_colider_inc':                               ['cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_curua_una':                                 [      'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_dardanelos':                                [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'amazonas_ferreira_gomes':                            [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'amazonas_ferreira_gomes_inc':                        ['cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',       'crude', 'cor_pr_flow', 'cor_pr_flow',       'crude',       'crude',      'cor_pr', 'cor_pr_flow'], 
'amazonas_guapore':                                   ['cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'amazonas_jirau':                                     ['cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr'], 
'amazonas_jirau_inc':                                 ['cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_rondon_ii':                                 [   'cor_flow',    'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'amazonas_samuel':                                    [      'crude',      'cor_pr',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow'], 
'amazonas_santo_antonio':                             ['cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_santo_antonio_do_jari':                     [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude'], 
'amazonas_sao_manuel':                                [     'cor_pr', 'cor_pr_flow',       'crude',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_sao_manuel_inc':                            [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow'], 
'amazonas_sinop':                                     ['cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_teles_pires':                               ['cor_pr_flow', 'cor_pr_flow',       'crude',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_teles_pires_inc':                           [   'cor_flow',       'crude',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 

'atlantico_leste_irape':                              [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'atlantico_leste_itapebi':                            [   'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow'], 
'atlantico_leste_itapebi_inc':                        [   'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'atlantico_leste_pedra_do_cavalo':                    [   'cor_flow',    'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr'], 
'atlantico_leste_santa_clara':                        [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr'], 

'atlantico_sudeste_lajes_fontes_nova_pereira_passos': [   'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'atlantico_sudeste_pedras':                           [   'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',    'cor_flow'], 
'atlantico_sudeste_rosal':                            [   'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow'], 

'atlantico_sul_capivari_cachoeira':                   [   'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr'], 
'atlantico_sul_salto_pilao':                          [   'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr'], 

'doce_aimores':                                       [   'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr'], 
'doce_aimores_inc':                                   [     'cor_pr',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr'], 
'doce_baguari':                                       [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'doce_baguari_inc':                                   [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'doce_cadonga':                                       [   'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'doce_guilman':                                       [   'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'doce_mascarenhas':                                   [   'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr'], 
'doce_mascarenhas_inc':                               [      'crude',       'crude',       'crude',       'crude',       'crude',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',       'crude'], 
'doce_porto_estrela':                                 [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr'],
'doce_porto_estrela_inc':                             [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr'], 
'doce_sa_carvalho':                                   [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'doce_sa_carvalho_inc':                               [      'crude',       'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow',       'crude',      'cor_pr',      'cor_pr',    'cor_flow', 'cor_pr_flow',       'crude',       'crude'], 
'doce_salto_grande':                                  [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr'], 

'grande_agua_vermelha':                               [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_agua_vermelha_inc':                           [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'grande_as_oliveira':                                 [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_as_oliveira_inc':                             ['cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_caconde':                                     [      'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'grande_camargos':                                    [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'grande_euclides_da_cunha':                           [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_euclides_da_cunha_inc':                       [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_funil_grande':                                [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_funil_grande_inc':                            [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_furnas':                                      [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_furnas_inc':                                  [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_igarapava':                                   [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_igarapava_inc':                               [   'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_itutinga':                                    [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'grande_jaguara':                                     [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_jaguara_inc':                                 [   'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_lc_barreto':                                  [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_lc_barreto_inc':                              [   'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_marimbondo':                                  [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_marimbondo_inc':                              [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'grande_mascarenhas_de_moraes':                       [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_mascarenhas_de_moraes_inc':                   [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'grande_porto_colombia':                              [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_porto_colombia_inc':                          [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_volta_grande':                                [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'grande_volta_grande_inc':                            [   'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 

'iguacu_baixo_iguacu':                                [   'cor_flow',    'cor_flow',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',    'cor_flow'], 
'iguacu_baixo_iguacu_inc':                            [      'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',    'cor_flow'], 
'iguacu_foz_do_areia':                                [   'cor_flow',    'cor_flow',      'cor_pr',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',    'cor_flow'], 
'iguacu_fundao':                                      [      'crude', 'cor_pr_flow',      'cor_pr',      'cor_pr',       'crude', 'cor_pr_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'iguacu_fundao_inc':                                  [      'crude',      'cor_pr',      'cor_pr',      'cor_pr',       'crude', 'cor_pr_flow',       'crude',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow'], 
'iguacu_gov_jose_richa':                              [   'cor_flow',    'cor_flow',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr'], 
'iguacu_gov_jose_richa_inc':                          [      'crude',      'cor_pr',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'iguacu_jordao':                                      [      'crude',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr',    'cor_flow',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow'], 
'iguacu_jordao_inc':                                  [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',       'crude',       'crude',       'crude',      'cor_pr',       'crude',       'crude'], 
'iguacu_salto_osorio':                                [   'cor_flow',    'cor_flow',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',    'cor_flow'], 
'iguacu_salto_osorio_inc':                            [   'cor_flow', 'cor_pr_flow',       'crude',       'crude',      'cor_pr', 'cor_pr_flow',    'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'iguacu_salto_santiago':                              [   'cor_flow',    'cor_flow',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr',    'cor_flow'],
'iguacu_salto_santiago_inc':                          [      'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow'],
'iguacu_santa_clara':                                 [      'crude', 'cor_pr_flow',      'cor_pr',      'cor_pr',       'crude', 'cor_pr_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'iguacu_segredo':                                     [   'cor_flow',    'cor_flow',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr'], 
'iguacu_segredo_inc':                                 [      'crude',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr'], 

'jacui_castro_alves':                                 [   'cor_flow',    'cor_flow',      'cor_pr',       'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr'], 
'jacui_dona_francisca':                               [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'jacui_dona_francisca_inc':                           [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'jacui_ernestina':                                    [   'cor_flow',      'cor_pr',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr'], 
'jacui_itauba':                                       [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'jacui_itauba_inc':                                   [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'jacui_jacui':                                        [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'],
'jacui_jacui_inc':                                    [   'cor_flow', 'cor_pr_flow',       'crude',    'cor_flow',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'jacui_monte_claro':                                  [   'cor_flow',    'cor_flow',      'cor_pr',       'crude',       'crude',       'crude',       'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr'], 
'jacui_monte_claro_inc':                              [   'cor_flow',    'cor_flow',       'crude',      'cor_pr',       'crude',       'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'jacui_passo_real':                                   [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'jacui_passo_real_inc':                               [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'jacui_14_de_julho':                                  [   'cor_flow',    'cor_flow',      'cor_pr',       'crude',       'crude',       'crude',       'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr'], 
'jacui_14_de_julho_inc':                              [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 

'paraguai_itiquira':                                  ['cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraguai_manso':                                     [   'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraguai_ponte_de_pedra':                            [   'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 

'paraiba_do_sul_anta':                                [   'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_anta_inc':                            [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_funil':                               [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_funil_inc':                           [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'paraiba_do_sul_ilha_dos_pombos':                     [   'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_ilha_dos_pombos_inc':                 [     'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow'], 
'paraiba_do_sul_itaocara_i':                          [   'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_itaocara_i_inc':                      ['cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_jaguari':                             [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'paraiba_do_sul_paraibuna':                           ['cor_pr_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_picada':                              [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_santana':                             [   'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_santana_inc':                         [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_santa_branca':                        [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_santa_branca_inc':                    [   'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'paraiba_do_sul_santa_cecilia':                       [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'paraiba_do_sul_santa_cecilia_inc':                   [   'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'paraiba_do_sul_sobragi':                             [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'paraiba_do_sul_sobragi_inc':                         [   'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'paraiba_do_sul_tocos':                               [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow'], 

'parana_ilha_solteira':                               ['cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'parana_ilha_solteira_equivalente':                   [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'parana_ilha_solteira_inc':                           ['cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'parana_itaipu':                                      ['cor_pr_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'parana_itaipu_inc':                                  ['cor_pr_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'parana_jupia':                                       [   'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'parana_jupia_inc':                                   [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'parana_porto_primavera':                             ['cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'parana_porto_primavera_inc':                         ['cor_pr_flow',      'cor_pr',      'cor_pr',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 

'paranaiba_barra_dos_coqueiros':                      ['cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow'], 
'paranaiba_barra_dos_coqueiros_inc':                  [   'cor_flow', 'cor_pr_flow',       'crude',       'crude',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'paranaiba_batalha':                                  [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_cachoeira_dourada':                        [   'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_cachoeira_dourada_inc':                    [     'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_cacu':                                     ['cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_capim_branco_i':                           [   'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_capim_branco_i_inc':                       [     'cor_pr',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'paranaiba_capim_branco_ii':                          [   'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_capim_branco_ii_inc':                      [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow'], 
'paranaiba_corumba_i':                                [   'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_corumba_i_inc':                            [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_corumba_iii':                              [      'crude',       'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_corumba_iii_inc':                          [   'cor_flow',    'cor_flow',       'crude',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',       'crude',       'crude'], 
'paranaiba_corumba_iv':                               [      'crude',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_emborcacao':                               [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_emborcacao_inc':                           [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_espora':                                   [   'cor_flow',    'cor_flow',    'cor_flow',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',       'crude',    'cor_flow'], 
'paranaiba_foz_do_rio_claro':                         ['cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paranaiba_foz_do_rio_claro_inc':                     [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow'], 
'paranaiba_itumbiara':                                [   'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_itumbiara_inc':                            [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow'], 
'paranaiba_miranda':                                  [   'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_miranda_inc':                              [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',       'crude'], 
'paranaiba_nova_ponte':                               [     'cor_pr',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_salto':                                    [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow'], 
'paranaiba_salto_rio_verdinho':                       [   'cor_flow',       'crude',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow'], 
'paranaiba_salto_rio_verdinho_inc':                   ['cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'paranaiba_sao_simao':                                [     'cor_pr', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow'], 
'paranaiba_sao_simao_inc':                            [     'cor_pr',    'cor_flow',       'crude',       'crude',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow'], 
'paranaiba_serra_do_facao':                           [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_serra_do_facao_inc':                       ['cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 

'paranapanema_canoas_i':                              [   'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_canoas_i_inc':                          [   'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paranapanema_canoas_ii':                             [   'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_canoas_ii_inc':                         [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_capivara':                              [   'cor_flow', 'cor_pr_flow',       'crude', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow'], 
'paranapanema_capivara_inc':                          [   'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_chavantes':                             [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_chavantes_inc':                         [   'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr'], 
'paranapanema_jurumirim':                             [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_maua':                                  [   'cor_flow',    'cor_flow',       'crude',       'crude',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_ourinhos':                              [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_ourinhos_inc':                          [   'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_piraju':                                [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_piraju_inc':                            [   'cor_flow',    'cor_flow',       'crude',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_rosana':                                ['cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paranapanema_rosana_inc':                            ['cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_salto_grande_l_n_garcez':               [   'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_salto_grande_l_n_garcez_inc':           [   'cor_flow',      'cor_pr',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow'], 
'paranapanema_taquarucu_escola_politecnica':          [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_taquarucu_escola_politecnica_inc':      [     'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 

'parnaiba_boa_esperanca':                             ['cor_pr_flow', 'cor_pr_flow',      'cor_pr',       'crude',       'crude', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 

'sao_francisco_apolonio_sales':                       [     'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',      'cor_pr'], 
'sao_francisco_complexo_paulo_afonso':                [     'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',      'cor_pr'], 
'sao_francisco_itaparica':                            [     'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',      'cor_pr'], 
'sao_francisco_itaparica_inc':                        [     'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'sao_francisco_paulo_afonso':                         [     'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',      'cor_pr'], 
'sao_francisco_queimado':                             [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'sao_francisco_retiro_baixo':                         [   'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'sao_francisco_sobradinho':                           [     'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr'], 
'sao_francisco_sobradinho_inc':                       [     'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr'], 
'sao_francisco_tres_marias':                          [   'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'sao_francisco_tres_marias_inc':                      [   'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'sao_francisco_xingo':                                [     'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',      'cor_pr'], 

'tiete_bariri':                                       [   'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow'], 
'tiete_bariri_inc':                                   [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'tiete_barra_bonita':                                 [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow'], 
'tiete_barra_bonita_inc':                             [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_billings':                                     [   'cor_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'],
'tiete_billings_mais_pedras':                         [      'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude'],
'tiete_edgard_de_souza':                              [   'cor_flow',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow'], 
'tiete_edgard_de_souza_inc':                          [   'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr'], 
'tiete_guarapiranga':                                 [     'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow'], 
'tiete_ibitinga':                                     [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow'], 
'tiete_ibitinga_inc':                                 [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_nova_avanhandava':                             [   'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow'], 
'tiete_nova_avanhandava_inc':                         [     'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow'], 
'tiete_ponte_nova':                                   [   'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'tiete_promissao':                                    [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow'], 
'tiete_promissao_inc':                                [   'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'tiete_traicao':                                      ['cor_pr_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow'], 
'tiete_tres_irmaos':                                  [   'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'tiete_tres_irmaos_inc':                              ['cor_pr_flow',    'cor_flow',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr'], 

'tocantins_cana_brava':                               [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow'], 
'tocantins_cana_brava_inc':                           [   'cor_flow', 'cor_pr_flow',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'tocantins_estreito_tocantins':                       ['cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'tocantins_estreito_tocantins_inc':                   [   'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'tocantins_lajeado':                                  [   'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow'], 
'tocantins_lajeado_inc':                              [   'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow'], 
'tocantins_peixe_angical':                            [   'cor_flow',       'crude',       'crude',       'crude', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'tocantins_peixe_angical_inc':                        [   'cor_flow', 'cor_pr_flow',       'crude',    'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'tocantins_sao_salvador':                             [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'tocantins_sao_salvador_inc':                         [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'tocantins_serra_da_mesa':                            [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'tocantins_tucurui':                                  ['cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'tocantins_tucurui_inc':                              [   'cor_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 

'uruguai_barra_grande':                               [   'cor_flow',      'cor_pr',      'cor_pr',       'crude',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr'], 
'uruguai_campos_novos':                               [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_campos_novos_inc':                           [   'cor_flow',       'crude',       'crude',      'cor_pr',       'crude',       'crude',       'crude',       'crude',       'crude', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_foz_do_chapeco':                             [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_foz_do_chapeco_inc':                         [   'cor_flow',       'crude',       'crude',      'cor_pr',       'crude',       'crude',       'crude',       'crude',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_garibaldi':                                  [   'cor_flow',    'cor_flow',      'cor_pr',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_garibaldi_inc':                              [   'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_ita':                                        [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_ita_inc':                                    [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',      'cor_pr',       'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_machadinho':                                 [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_machadinho_inc':                             [   'cor_flow',       'crude',       'crude',      'cor_pr',       'crude',       'crude',       'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow'], 
'uruguai_monjolinho':                                 [   'cor_flow',       'crude',       'crude',      'cor_pr',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr'], 
'uruguai_monjolinho_inc':                             [   'cor_flow',      'cor_pr',       'crude',      'cor_pr',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'uruguai_passo_fundo':                                [   'cor_flow',    'cor_flow',       'crude',      'cor_pr',       'crude',       'crude',       'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'uruguai_passo_sao_joao':                             [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'uruguai_passo_sao_joao_inc':                         [   'cor_flow',    'cor_flow',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow'], 
'uruguai_quebra_queixo':                              [   'cor_flow',      'cor_pr',       'crude',      'cor_pr',       'crude',      'cor_pr',      'cor_pr',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'uruguai_sao_jose':                                   [   'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'uruguai_sao_roque':                                  [   'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow']
}


