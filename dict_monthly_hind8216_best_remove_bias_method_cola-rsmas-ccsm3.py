# -*- coding: utf-8 -*-
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

    cor_pr:      Value simulated with the precipitation corrected delivered of COLA-RSMAS-CCSM3 model.
    cor_flow:    Value simulated with the flow corrected delivered of COLA-RSMAS-CCSM3 model.
    cor_pr_flow: Value simulated with the flow corrected with the precipitation delivered of COLA-RSMAS-CCSM3 model.
    crude:       Crude value delivered from COLA-RSMAS-CCSM3 model.

Usage:
    Used in the removal of the bias of the flow data from the COLA-RSMAS-CCSM3 model.


Last update: 2017-09-28 12:48

"""

dict_remove_bias_cola-rsmas-ccsm3={

'amazonas_balbina':                                  [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow'], 
'amazonas_belo_monte':                               [   'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'amazonas_cachoeira_caldeirao':                      [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow'], 
'amazonas_coaracy_nunes':                            [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow'], 
'amazonas_colider':                                  ['cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'amazonas_colider_inc':                              [   'cor_flow',    'cor_flow',       'crude',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude', 'cor_pr_flow',    'cor_flow',    'cor_flow'],
'amazonas_curua_una':                                ['cor_pr_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',   ' cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_dardanelos':                               [   'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'amazonas_ferreira_gomes':                           [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow'], 
'amazonas_ferreira_gomes_inc':                       ['cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', '      crude',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',      'cor_pr', 'cor_pr_flow'],
'amazonas_guapore':                                  [   'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'amazonas_jirau':                                    [   'cor_flow',       'crude',    'cor_flow',    'cor_flow',       'crude',       'crude',       'crude', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'amazonas_jirau_inc':                                [   'cor_flow',       'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'amazonas_rondon_ii':                                [   'cor_flow',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',      'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow'],
'amazonas_samuel':                                   [   'cor_flow',       'crude',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow'], 
'amazonas_santo_antonio':                            [   'cor_flow',       'crude',       'crude',      'cor_pr',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'amazonas_santo_antonio_do_jari':                    [     'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'],
'amazonas_santo_antonio_inc':                        [   'cor_flow',       'crude',       'crude',      'cor_pr',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'amazonas_sao_manuel':                               [   'cor_flow',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'],
'amazonas_sao_manuel_inc':                           [   'cor_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow'],
'amazonas_sinop':                                    ['cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'amazonas_teles_pires':                              [   'cor_flow',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'amazonas_teles_pires_inc':                          [   'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'],

'atlantico_leste_irape':                             [      'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow',    'cor_flow',       'crude'], 
'atlantico_leste_itapebi':                           [   'cor_flow',       'crude',      'cor_pr',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',      'cor_pr',    'cor_flow',       'crude',       'crude'], 
'atlantico_leste_itapebi_inc':                       [   'cor_flow',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',       'crude',       'crude',      'cor_pr',      'cor_pr',       'crude',       'crude'], 
'atlantico_leste_pedra_do_cavalo':                   [      'crude',       'crude',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',       'crude'], 
'atlantico_leste_santa_clara':                       [      'crude',       'crude',       'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',       'crude',      'cor_pr',    'cor_flow',      'cor_pr',       'crude'], 

'atlantico_sudeste_lajes_fontes_nova_pereira_passos':['cor_pr_flow',       'crude',      'cor_pr',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'atlantico_sudeste_pedras':                          [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'],
'atlantico_sudeste_rosal':                           [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',       'crude'], 

'atlantico_sul_capivari_cachoeira':                  [   'cor_flow',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'atlantico_sul_salto_pilao':                         [      'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow'], 

'doce_aimores':                                      [      'crude',       'crude',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',       'crude', 'cor_pr_flow',      'cor_pr',      'cor_pr',       'crude',       'crude'], 
'doce_aimores_inc':                                  [      'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'doce_baguari':                                      [      'crude',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',       'crude',       'crude', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',       'crude',       'crude'],
'doce_baguari_inc':                                  [      'crude',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',       'crude'], 
'doce_cadonga':                                      [   'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'doce_guilman':                                      [      'crude',       'crude',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'doce_mascarenhas':                                  [      'crude',       'crude',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',       'crude', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',       'crude'], 
'doce_mascarenhas_inc':                              [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', '   cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow'],
'doce_porto_estrela':                                [   'cor_flow',    'cor_flow',       'crude', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr'], 
'doce_porto_estrela_inc':                            [      'crude',       'crude',       'crude',      'cor_pr',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'doce_sa_carvalho':                                  [      'crude',       'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'doce_sa_carvalho_inc':                              [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr'], 
'doce_salto_grande':                                 [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 

'grande_agua_vermelha':                              [      'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_agua_vermelha_inc':                          [      'crude',       'crude',       'crude',      'cor_pr',       'crude',       'crude',    'cor_flow', 'cor_pr_flow',       'crude', 'cor_pr_flow',    'cor_flow',       'crude'], 
'grande_as_oliveira':                                [   'cor_flow',       'crude',       'crude', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_as_oliveira_inc':                            [      'crude',    'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow', '   cor_flow', 'cor_pr_flow'], 
'grande_caconde':                                    [   'cor_flow',       'crude',       'crude', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_camargos':                                   [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr'], 
'grande_euclides_da_cunha':                          [   'cor_flow',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_euclides_da_cunha_inc':                      [      'crude',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_furnas':                                     [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_furnas_inc':                                 [      'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_funil_grande':                               [      'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_funil_grande_inc':                           [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr'], 
'grande_igarapava':                                  [      'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'],
'grande_igarapava_inc':                              [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_itutinga':                                   [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr'],
'grande_jaguara':                                    [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_jaguara_inc':                                [   'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow'], 
'grande_lc_barreto':                                 [      'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_lc_barreto_inc':                             [   'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'grande_marimbondo':                                 [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_marimbondo_inc':                             [   'cor_flow',    'cor_flow',       'crude', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', '   cor_flow',    'cor_flow'], 
'grande_mascarenhas_de_moraes':                      [      'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_mascarenhas_de_moraes_inc':                  [   'cor_flow',       'crude',       'crude',      'cor_pr',       'crude', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow'], 
'grande_porto_colombia':                             [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_porto_colombia_inc':                         [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'grande_volta_grande':                               [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'grande_volta_grande_inc':                           [      'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 

'iguacu_baixo_iguacu':                               [   'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'iguacu_baixo_iguacu_inc':                           [   'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'iguacu_foz_do_areia':                               [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'iguacu_fundao':                                     [   'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'],
'iguacu_fundao_inc':                                 [     'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'], 
'iguacu_gov_jose_richa':                             [   'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow'], 
'iguacu_gov_jose_richa_inc':                         [     'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'iguacu_jordao':                                     [   'cor_flow',      'cor_pr'       'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr'], 
'iguacu_jordao_inc':                                 [     'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'iguacu_salto_osorio':                               [   'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr'], 
'iguacu_salto_osorio_inc':                           [      'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',       'crude',       'crude'], 
'iguacu_salto_santiago':                             [   'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr'], 
'iguacu_salto_santiago_inc':                         [     'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',       'crude',       'crude'], 
'iguacu_santa_clara':                                [   'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr'], 
'iguacu_segredo':                                    [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'],
'iguacu_segredo_inc':                                [     'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 

'jacui_castro_alves':                                [     'cor_pr',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 	    'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'jacui_dona_francisca':                              [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'jacui_dona_francisca_inc':                          [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',      'cor_pr',       'crude',       'crude'],
'jacui_ernestina':                                   [   'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'],  
'jacui_itauba':                                      [      'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude'], 
'jacui_itauba_inc':                                  [      'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',       'crude',       'crude'],
'jacui_jacui':                                       [      'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude'], 
'jacui_jacui_inc':                                   [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'jacui_monte_claro':                                 [      'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude'], 
'jacui_monte_claro_inc':                             [      'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',       'crude'], 
'jacui_passo_real':                                  [      'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude'],
'jacui_passo_real_inc':                              [      'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude'], 
'jacui_14_de_julho':                                 [      'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude'], 
'jacui_14_de_julho_inc':                             [      'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr'], 

'paraguai_itiquira':                                 [   'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow'], 
'paraguai_manso':                                    [      'crude', 'cor_pr_flow',      'cor_pr',      'cor_pr',       'crude',       'crude',       'crude',       'crude', '     cor_pr',       'crude', 'cor_pr_flow',       'crude'], 
'paraguai_ponte_de_pedra':                           [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 

'paraiba_do_sul_anta':                               [   'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paraiba_do_sul_anta_inc':                           [   'cor_flow',    'cor_flow',       'crude',    'cor_flow',       'crude',       'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'paraiba_do_sul_funil':                              [   'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',	 'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'paraiba_do_sul_funil_inc':                          [   'cor_flow',       'crude',       'crude',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',	 'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'paraiba_do_sul_ilha_dos_pombos':                    [   'cor_flow',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',	 'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'paraiba_do_sul_ilha_dos_pombos_inc':                [   'cor_flow',       'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude',    'cor_flow',	 'cor_flow',	'cor_flow',      'cor_pr',      'cor_pr'], 
'paraiba_do_sul_itaocara_i':                         [   'cor_flow',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',	 'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'paraiba_do_sul_itaocara_i_inc':                     [   'cor_flow',       'crude',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',       'crude',    'cor_flow',	 'cor_flow',	'cor_flow', 'cor_pr_flow',    'cor_flow'],
'paraiba_do_sul_jaguari':                            [   'cor_flow',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'paraiba_do_sul_paraibuna':                          [   'cor_flow',       'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',	 'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'paraiba_do_sul_picada':                             [   'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',	 'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'paraiba_do_sul_santa_branca':                       [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',       'crude',       'crude',      'cor_pr',	 'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'paraiba_do_sul_santa_branca_inc':                   [      'crude',       'crude', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',       'crude',       'crude',      'cor_pr',       'crude',      'cor_pr',       'crude',       'crude'], 
'paraiba_do_sul_santa_cecilia':                      [   'cor_flow',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',	 'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paraiba_do_sul_santa_cecilia_inc':                  [   'cor_flow',       'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',	 'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'],
'paraiba_do_sul_santana':                            [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',	 'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paraiba_do_sul_santana_inc':                        [   'cor_flow',       'crude',       'crude',    'cor_flow', 'cor_pr_flow',       'crude',       'crude',    'cor_flow',	 'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'paraiba_do_sul_sobragi':                            [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',	 'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr'], 
'paraiba_do_sul_sobragi_inc':                        [   'cor_flow',       'crude',       'crude', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude',	 'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'],
'paraiba_do_sul_tocos':                              [   'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',       'crude',      'cor_pr',      'cor_pr', 'cor_pr_flow'],

'parana_ilha_solteira':                              [      'crude',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',       'crude'],
'parana_ilha_solteira_inc':                          [   'cor_flow',    'cor_flow',    'cor_flow',       'crude',       'crude',      'cor_pr',	     'cor_pr',      'cor_pr',       'crude',    'cor_flow',    'cor_flow',       'crude'], 
'parana_ilha_solteira_equivalente':                  [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'],
'parana_itaipu':                                     [   'cor_flow', 'cor_pr_flow',       'crude', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'parana_itaipu_inc':                                 [   'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow'],
'parana_jupia':                                      [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'parana_jupia_inc':                                  [     'cor_pr',      'cor_pr',      'cor_pr',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude',       'crude'], 
'parana_porto_primavera':                            [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'parana_porto_primavera_inc':                        [   'cor_flow',      'cor_pr',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr',       'crude',       'crude',      'cor_pr', '     cor_pr'], 

'paranaiba_barra_dos_coqueiros':                     [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_barra_dos_coqueiros_inc':                 [   'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'paranaiba_batalha':                                 [      'crude',       'crude',    'cor_flow',       'crude',       'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_cachoeira_dourada':                       [      'crude',       'crude',      'cor_pr',    'cor_flow',    'cor_flow',       'crude',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',      'cor_pr',       'crude'],  
'paranaiba_cachoeira_dourada_inc':                   [      'crude',      'cor_pr',      'cor_pr',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_cacu':                                    [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'paranaiba_capim_branco_i':                          [      'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_capim_branco_i_inc':                      [      'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',       'crude',      'cor_pr',       'crude'],
'paranaiba_capim_branco_ii':                         [      'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_capim_branco_ii_inc':                     [      'crude',      'cor_pr',      'cor_pr',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow'], 
'paranaiba_corumba_i':                               [      'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_corumba_i_inc':                           [      'crude',       'crude',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_corumba_iii':                             [      'crude',       'crude',       'crude',       'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_corumba_iii_inc':                         ['cor_pr_flow',    'cor_flow',       'crude',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'],
'paranaiba_corumba_iv':                              [      'crude',       'crude',       'crude',       'crude',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_foz_do_rio_claro':                        [      'crude',       'crude',       'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',       'crude',       'crude',    'cor_flow'], 
'paranaiba_foz_do_rio_claro_inc':                    [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_emborcacao':                              [      'crude',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_emborcacao_inc':                          [      'crude',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'],
'paranaiba_espora':                                  [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paranaiba_itumbiara':                               [      'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_itumbiara_inc':                           [      'crude',       'crude',       'crude',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'],
'paranaiba_miranda':                                 [      'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_miranda_inc':                             [   'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow'],
'paranaiba_nova_ponte':                              [      'crude',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'paranaiba_salto':                                   [      'crude',    'cor_flow',    'cor_flow',       'crude',       'crude', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude',       'crude',       'crude',       'crude'], 
'paranaiba_salto_rio_verdinho':                      [      'crude',       'crude',       'crude',    'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude',       'crude',       'crude',       'crude'], 
'paranaiba_salto_rio_verdinho_inc':                  [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow'],
'paranaiba_sao_simao':                               [      'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',       'crude',       'crude', 'cor_pr_flow',      'cor_pr',    'cor_flow',      'cor_pr',       'crude'], 
'paranaiba_sao_simao_inc':                           [      'crude',       'crude',       'crude',      'cor_pr',       'crude',       'crude',       'crude',      'cor_pr',       'crude',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranaiba_serra_do_facao':                          [      'crude',    'cor_flow',    'cor_flow',       'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',       'crude'], 
'paranaiba_serra_do_facao_inc':                      [      'crude',      'cor_pr',      'cor_pr', 'cor_pr_flow',       'crude',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'],

'paranapanema_canoas_i':                             [      'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_canoas_i_inc':                         [      'crude',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow', '     cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow'], 
'paranapanema_capivara':                             [      'crude', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_capivara_inc':                         [      'crude', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'],
'paranapanema_chavantes':                            [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_chavantes_inc':                        [      'crude',       'crude',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',       'crude'], 
'paranapanema_rosana':                               [      'crude', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_rosana_inc':                           ['cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',       'crude',      'cor_pr',    'cor_flow',    'cor_flow'],
'paranapanema_canoas_ii':                            [      'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_canoas_ii_inc':                        [      'crude',    'cor_flow',       'crude',      'cor_pr',      'cor_pr',       'crude',      'cor_pr', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow'], 
'paranapanema_jurumirim':                            [      'crude',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_maua':                                 [   'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_ourinhos':                             [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'paranapanema_ourinhos_inc':                         [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'paranapanema_piraju':                               [      'crude',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_piraju_inc':                           [      'crude',       'crude',       'crude',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow'],
'paranapanema_salto_grande_l_n_garcez':              [      'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_salto_grande_l_n_garcez_inc':          [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow'],
'paranapanema_taquarucu_escola_politecnica':         [      'crude', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', '   cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'paranapanema_taquarucu_escola_politecnica_inc':     [     'cor_pr',      'cor_pr',     'cor_pr_', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',       'crude',       'crude',      'cor_pr'],

'parnaiba_boa_esperanca':                            ['cor_pr_flow', 'cor_pr_flow',      'cor_pr',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',       'crude',      'cor_pr',      'cor_pr',       'crude', 'cor_pr_flow'], 

'sao_francisco_apolonio_sales':                      [      'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'sao_francisco_complexo_paulo_afonso':               [      'crude',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'sao_francisco_itaparica':                           [      'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'sao_francisco_itaparica_inc':                       [     'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr',       'crude',       'crude',      'cor_pr'], 
'sao_francisco_paulo_afonso':                        [      'crude',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'sao_francisco_queimado':                            [      'crude',       'crude',       'crude',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'sao_francisco_retiro_baixo':                        [      'crude',       'crude',    'cor_flow',      'cor_pr',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'sao_francisco_sobradinho':                          [      'crude',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'sao_francisco_sobradinho_inc':                      [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'sao_francisco_tres_marias':                         [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'],
'sao_francisco_tres_marias_inc':                     [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'],  
'sao_francisco_xingo':                               [      'crude',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'],

'tiete_bariri':                                      [   'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_bariri_inc':                                  [   'cor_flow',    'cor_flow',       'crude', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',       'crude'], 
'tiete_barra_bonita':                                [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_barra_bonita_inc':                            [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_billings':                                    [   'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_billings_mais_pedras':                        [   'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'tiete_edgard_de_souza':                             [   'cor_flow',       'crude',       'crude',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_edgard_de_souza_inc':                         [   'cor_flow',       'crude',       'crude',    'cor_flow',    'cor_flow',       'crude',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_guarapiranga':                                [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow'],
'tiete_ibitinga':                                    [   'cor_flow',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'],  
'tiete_ibitinga_inc':                                [      'crude',       'crude',       'crude', 'cor_pr_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'tiete_nova_avanhandava':                            [      'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'],
'tiete_nova_avanhandava_inc':                        [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',       'crude', 'cor_pr_flow',       'crude',    'cor_flow',       'crude',       'crude'], 
'tiete_ponte_nova':                                  [     'cor_pr',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow'], 
'tiete_promissao':                                   [      'crude',       'crude',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow'], 
'tiete_promissao_inc':                               [   'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow',       'crude',       'crude', 'cor_pr_flow',    'cor_flow',      'cor_pr',       'crude',       'crude'], 
'tiete_traicao':                                     [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_tres_irmaos':                                 [      'crude',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tiete_tres_irmaos_inc':                             [      'crude',       'crude', 'cor_pr_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',       'crude',       'crude',       'crude'], 
  
'tocantins_cana_brava':                              [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'tocantins_cana_brava_inc':                          [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude',       'crude',      'cor_pr',       'crude',       'crude'], 
'tocantins_estreito_tocantins':                      [   'cor_flow', 'cor_pr_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'tocantins_estreito_tocantins_inc':                  ['cor_pr_flow', '     cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',       'crude',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow'], 
'tocantins_lajeado':                                 [   'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'],
'tocantins_lajeado_inc':                             [   'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',       'crude'],
'tocantins_sao_salvador':                            [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'tocantins_sao_salvador_inc':                        ['cor_pr_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',       'crude',       'crude',       'crude',       'crude',    'cor_flow'],
'tocantins_serra_da_mesa':                           [      'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', '   cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'],
'tocantins_peixe_angical':                           [      'crude',       'crude',       'crude',       'crude',    'cor_flow', 'cor_pr_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'tocantins_peixe_angical_inc':                       [   'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',       'crude'], 
'tocantins_tucurui':                                 [   'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 
'tocantins_tucurui_inc':        		     [   'cor_flow',       'crude',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow'], 

'uruguai_barra_grande':                              [      'crude',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'uruguai_campos_novos':                              [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr'],
'uruguai_campos_novos_inc':                          [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr'],
'uruguai_foz_do_chapeco':                            [   'cor_flow',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr'],
'uruguai_foz_do_chapeco_inc':                        [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow', 'cor_pr_flow',       'crude',    'cor_flow'],
'uruguai_garibaldi':                                 [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr'], 
'uruguai_garibaldi_inc':                             [      'crude',       'crude',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow', 'cor_pr_flow',       'crude',       'crude'],
'uruguai_ita':                                       [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'uruguai_ita_inc':                                   [     'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',       'crude'], 
'uruguai_machadinho':                                [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr'], 
'uruguai_machadinho_inc':                            [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude'],
'uruguai_monjolinho':                                [     'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',       'crude',       'crude'], 
'uruguai_monjolinho_inc':                            [     'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',       'crude',       'crude'],
'uruguai_passo_fundo':                               [     'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr', 'cor_pr_flow',      'cor_pr',      'cor_pr',    'cor_flow'], 
'uruguai_passo_sao_joao':                            [     'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude'], 
'uruguai_passo_sao_joao_inc':                        [      'crude', 'cor_pr_flow',    'cor_flow',      'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow', 'cor_pr_flow',    'cor_flow',       'crude'], 
'uruguai_quebra_queixo':                             [     'cor_pr',      'cor_pr',      'cor_pr', 'cor_pr_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',      'cor_pr',      'cor_pr',      'cor_pr'], 
'uruguai_sao_jose':                                  [     'cor_pr',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',    'cor_flow',      'cor_pr',    'cor_flow', 'cor_pr_flow',    'cor_flow',    'cor_flow',       'crude'],
'uruguai_sao_roque':                                 [   'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',    'cor_flow',    'cor_flow',      'cor_pr',      'cor_pr',      'cor_pr',      'cor_pr',       'crude',      'cor_pr']
}			    
 



