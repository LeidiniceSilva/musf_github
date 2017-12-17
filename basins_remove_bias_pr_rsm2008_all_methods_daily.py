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


Each month must have one of the 3 strings below:

    eqm_des: Empirical Quantile Mapping Desagregated.
    crude: Crude value delivered from RSM2008 model.


Usage:
    Used in the removal of the bias of the preciptation data from the RSM2008 model.


Last update: 2017-12-11 16:23

"""

dict_remove_bias_rsm2008={

'amazonas_balbina':                                   ['cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude'], 
'amazonas_belo_monte':                                [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_cachoeira_caldeirao':                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_coaracy_nunes':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_coaracy_nunes_inc':                         ['cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_colider':                                   [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_colider_inc':                               [     'crude', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_curua_una':                                 ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes'], 
'amazonas_dardanelos':                                [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'amazonas_ferreira_gomes':                            ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_ferreira_gomes_inc':                        ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes'],
'amazonas_guapore':                                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_jirau':                                     ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_jirau_inc':                                 ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_rondon_ii':                                 [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_samuel':                                    [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'amazonas_santo_antonio':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'],
'amazonas_santo_antonio_do_jari':                     ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'amazonas_santo_antonio_inc':                         ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'],
'amazonas_sao_manuel':                                [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_sao_manuel_inc':                            [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude'], 
'amazonas_sinop':                                     [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_teles_pires':                               [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'amazonas_teles_pires_inc':                           [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'atlantico_leste_irape':                              ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'atlantico_leste_itapebi':                            ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'atlantico_leste_itapebi_inc':                        ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'atlantico_leste_pedra_do_cavalo':                    ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'atlantico_leste_santa_clara':                        ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'atlantico_sudeste_lajes_fontes_nova_pereira_passos': [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'atlantico_sudeste_rosal':                            ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'atlantico_sudeste_pedras':                           [     'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 

'atlantico_sul_capivari_cachoeira':                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'atlantico_sul_salto_pilao':                          ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'doce_aimores':                                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'doce_aimores_inc':                                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'doce_baguari':                                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'doce_baguari_inc':                                   ['cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'doce_cadonga':                                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'doce_guilman':                                       [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'doce_mascarenhas':                                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'doce_mascarenhas_inc':                               ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'doce_porto_estrela':                                 ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'doce_porto_estrela_inc':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'doce_salto_grande':                                  ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'doce_sa_carvalho':                                   [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'doce_sa_carvalho_inc':                               [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 

'grande_agua_vermelha':                               ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_agua_vermelha_inc':                           ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'grande_as_oliveira':                                 [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'grande_as_oliveira_inc':                             [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_caconde':                                     [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'grande_camargos':                                    ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'grande_euclides_da_cunha':                           [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'grande_euclides_da_cunha_inc':                       [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'grande_funil_grande':                                ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_funil_grande_inc':                            [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'grande_furnas':                                      [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_furnas_inc':                                  [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_igarapava':                                   [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_igarapava_inc':                               [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'grande_itutinga':                                    ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'grande_itutinga_inc':                                ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'grande_jaguara':                                     [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_jaguara_inc':                                 [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'grande_lc_barreto':                                  [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_lc_barreto_inc':                              [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_marimbondo':                                  [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_marimbondo_inc':                              [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_mascarenhas_de_moraes':                       [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_mascarenhas_de_moraes_inc':                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'grande_porto_colombia':                              [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_porto_colombia_inc':                          [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_volta_grande':                                [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'grande_volta_grande_inc':                            [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 

'iguacu_baixo_iguacu':                                [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'],
'iguacu_baixo_iguacu_inc':                            [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'iguacu_foz_do_areia':                                ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'iguacu_fundao':                                      [     'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'iguacu_fundao_inc':                                  [     'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'iguacu_gov_jose_richa':                              [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'iguacu_gov_jose_richa_inc':                          [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'iguacu_jordao':                                      [     'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'iguacu_jordao_inc':                                  [     'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'iguacu_salto_osorio':                                ['cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'iguacu_salto_osorio_inc':                            [     'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'iguacu_salto_santiago':                              ['cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'iguacu_salto_santiago_inc':                          [     'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'iguacu_santa_clara':                                 [     'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'iguacu_segredo':                                     ['cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'],
'iguacu_segredo_inc':                                 [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'jacui_castro_alves':                                 ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_dona_francisca':                               ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_dona_francisca_inc':                           ['cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_ernestina':                                    ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_itauba':                                       ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_itauba_inc':                                   ['cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_jacui':                                        ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_jacui_inc':                                    ['cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_monte_claro':                                  ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_monte_claro_inc':                              [     'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_passo_real':                                   ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_passo_real_inc':                               ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_14_de_julho':                                  ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'jacui_14_de_julho_inc':                              ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'paraguai_itiquira':                                  [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraguai_jauru':                                     ['cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraguai_manso':                                     ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraguai_ponte_de_pedra':                            [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 

'paraiba_do_sul_anta':                                ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_anta_inc':                            ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_funil':                               ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_funil_inc':                           ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_ilha_dos_pombos':                     ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_ilha_dos_pombos_inc':                 ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_itaocara_i':                          ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_itaocara_i_inc':                      ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_jaguari':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_paraibuna':                           ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_picada':                              ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_santana':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_santana_inc':                         ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_santa_branca':                        ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_santa_branca_inc':                    ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_santa_cecilia':                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_santa_cecilia_inc':                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_sobragi':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_sobragi_inc':                         ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paraiba_do_sul_tocos':                               ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'parana_ilha_solteira':                               ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'parana_ilha_solteira_equivalente':                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'parana_ilha_solteira_equivalente_inc':               ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'parana_ilha_solteira_inc':                           ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'parana_itaipu':                                      ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'parana_itaipu_inc':                                  ['cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'parana_jupia':                                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'parana_jupia_inc':                                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'parana_porto_primavera':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'parana_porto_primavera_inc':                         ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'paranaiba_barra_dos_coqueiros':                      ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_barra_dos_coqueiros_inc':                  [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_batalha':                                  [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_cachoeira_dourada':                        [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranaiba_cachoeira_dourada_inc':                    ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_capim_branco_i':                           ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_capim_branco_i_inc':                       [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranaiba_capim_branco_ii':                          [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_capim_branco_ii_inc':                      [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranaiba_cacu':                                     ['cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_corumba_i':                                [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranaiba_corumba_i_inc':                            [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranaiba_corumba_iii':                              [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'paranaiba_corumba_iii_inc':                          [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'paranaiba_corumba_iv':                               [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude'], 
'paranaiba_emborcacao':                               [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranaiba_emborcacao_inc':                           [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'],
'paranaiba_espora':                                   [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranaiba_foz_do_rio_claro':                         ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_foz_do_rio_claro_inc':                     ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_itumbiara':                                [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranaiba_itumbiara_inc':                            [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranaiba_miranda':                                  ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_miranda_inc':                              [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_nova_ponte':                               ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_salto':                                    [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_salto_rio_verdinho':                       [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_salto_rio_verdinho_inc':                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_sao_simao':                                ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_sao_simao_inc':                            ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_serra_do_facao':                           [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranaiba_serra_do_facao_inc':                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'paranapanema_canoas_i':                              ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_canoas_i_inc':                          ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_canoas_ii':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_canoas_ii_inc':                         ['cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_chavantes':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_chavantes_inc':                         [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'paranapanema_capivara':                              ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_capivara_inc':                          ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_jurumirim':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_maua':                                  [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'paranapanema_ourinhos':                              ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_ourinhos_inc':                          [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'paranapanema_piraju':                                ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_piraju_inc':                            [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'paranapanema_rosana':                                ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_rosana_inc':                            ['cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_salto_grande_l_n_garcez':               ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_salto_grande_l_n_garcez_inc':           ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_taquarucu_escola_politecnica':          ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'paranapanema_taquarucu_escola_politecnica_inc':      ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'parnaiba_boa_esperanca':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'sao_francisco_apolonio_sales':                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_apolonio_sales_inc':                   [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_complexo_paulo_afonso':                ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_complexo_paulo_afonso_inc':            ['cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_itaparica':                            ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_itaparica_inc':                        ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_paulo_afonso':                         ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_paulo_afonso_inc':                     ['cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_queimado':                             [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_retiro_baixo':                         [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'sao_francisco_sobradinho':                           ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_sobradinho_inc':                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_tres_marias':                          [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'sao_francisco_tres_marias_inc':                      [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'sao_francisco_xingo':                                ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'sao_francisco_xingo_inc':                            ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'tiete_bariri':                                       ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_bariri_inc':                                   ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_barra_bonita':                                 ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_barra_bonita_inc':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'tiete_billings':                                     [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'tiete_billings_mais_pedras':                         [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'tiete_edgard_de_souza':                              ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_edgard_de_souza_inc':                          ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_guarapiranga':                                 ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_ibitinga':                                     ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_ibitinga_inc':                                 ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude'], 
'tiete_nova_avanhandava':                             ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_nova_avanhandava_inc':                         ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_promissao':                                    ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_promissao_inc':                                ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_ponte_nova':                                   [     'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude'], 
'tiete_traicao':                                      ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_traicao_inc':                                  ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_tres_irmaos':                                  ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tiete_tres_irmaos_inc':                              ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'tocantins_cana_brava':                               [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude'], 
'tocantins_cana_brava_inc':                           [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude'], 
'tocantins_estreito_tocantins':                       ['cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tocantins_estreito_tocantins_inc':                   ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tocantins_lajeado':                                  [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tocantins_lajeado_inc':                              ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tocantins_peixe_angical':                            [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude'], 
'tocantins_peixe_angical_inc':                        [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude'],
'tocantins_sao_salvador':                             [     'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude'], 
'tocantins_sao_salvador_inc':                         [     'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'tocantins_serra_da_mesa':                            [     'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude'], 
'tocantins_tucurui':                                  ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'tocantins_tucurui_inc':                              ['cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 

'uruguai_barra_grande':                               ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_campos_novos':                               ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_campos_novos_inc':                           [     'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'uruguai_foz_do_chapeco':                             ['cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_foz_do_chapeco_inc':                         [     'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_garibaldi':                                  ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_garibaldi_inc':                              [     'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_ita':                                        ['cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_ita_inc':                                    [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_machadinho':                                 ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_machadinho_inc':                             [     'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude'], 
'uruguai_monjolinho':                                 [     'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_monjolinho_inc':                             [     'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_passo_fundo':                                [     'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'],
'uruguai_passo_sao_joao':                             ['cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_passo_sao_joao_inc':                         [     'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_quebra_queixo':                              [     'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_sao_jose':                                   ['cor_eqmdes',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes'], 
'uruguai_sao_roque':                                  ['cor_eqmdes', 'cor_eqmdes',      'crude',      'crude', 'cor_eqmdes', 'cor_eqmdes',      'crude', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes', 'cor_eqmdes']
} 

