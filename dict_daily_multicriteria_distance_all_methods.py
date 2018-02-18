# -*- coding: utf-8 -*-

# Author = 'Funceme'
# Credits = 'Leidinice Silva, Micael Costa, Duarte Junior'
# Maintainer = 'Funceme'
# Date = 24/01/2018  (dd/mm/aaaa)
# Comment = 'Este script foi desenvolvido dentro do Termo de Cooperação
#            0050.0100467.16.9 entre Funceme e Petrobras sob o contexto do
#            Projeto Projeção de Vazão Natural Afluente com base na escala de
#            tempo e clima'
# Description = 'Dictionary of subbasins estatistical methods classification
#                daily multicriteria distance.'


"""
Dictionary of subbasins estatistical methods classification daily 
multicriteria distance.


Dictionary format:
    dict_best_method = {'basin': ['best_2w', 'best_4w'], ...}


Parameters description:

    best_2w: Best method per period - Two weeks
    best_4w: Best method per period - Four weeks


Each period must have one of the 3 strings below:

    m1: m1 value delivered from GFS05_RSM2008 model.
    m2: m2 value delivered from GFS05_RSM2008 model.
    m3: m3 value delivered from GFS05_RSM2008 model


Usage:
    Used in the choice of best method flow data from the GFS05_RSM2008 model.


Last update: 2018-01-24 14:55

"""

dict_best_method_gfs05_rsm2008={


'amazonas_coaracy_nunes':					 ['m2',	'm1'],
'amazonas_curua_una':						 ['m1',	'm1'],
'amazonas_dardanelos':						 ['m3',	'm1'],
'amazonas_samuel':					         ['m2',	'm3'],
'amazonas_santo_antonio'					 ['m1',	'm1'],
'amazonas_santo_antonio_do_jari':			         ['m2',	'm1'],
'atlantico_leste_irape':					 ['m3', 'm1'],
'atlantico_leste_itapebi':					 ['m3',	'm3'],
'atlantico_leste_pedra_do_cavalo':				 ['m3',	'm3'],
'atlantico_leste_santa_clara':					 ['m3',	'm1'],
'atlantico_sudeste_rosal':					 ['m3',	'm1'],
'atlantico_sul_capivari_cachoeira':				 ['m3',	'm3'],
'atlantico_sul_salto_pilao':					 ['m3',	'm1'],
'doce_aimores':							 ['m3',	'm3'],
'doce_cadonga':							 ['m3',	'm1'],
'doce_mascarenhas':						 ['m3',	'm3'],
'doce_porto_estrela':						 ['m3',	'm1'],
'doce_sa_carvalho':						 ['m2',	'm1'],
'grande_agua_vermelha':						 ['m3',	'm3'],
'grande_as_oliveira':						 ['m3',	'm3'],
'grande_caconde':						 ['m3',	'm3'],
'grande_camargos':						 ['m3',	'm3'],
'grande_euclides_da_cunha':					 ['m3',	'm3'],
'grande_funil_grande':						 ['m3',	'm3'],
'grande_furnas':						 ['m3',	'm3'],
'grande_igarapava':						 ['m3',	'm3'],
'grande_lc_barreto':						 ['m3',	'm3'],
'grande_marimbondo':						 ['m3',	'm3'],
'grande_mascarenhas_de_moraes':				 	 ['m3',	'm3'],
'grande_porto_colombia':					 ['m3',	'm3'],
'grande_volta_grande':						 ['m3',	'm3'],
'iguacu_foz_do_areia':						 ['m3',	'm3'],
'iguacu_fundao':						 ['m3',	'm1'],
'iguacu_gov_jose_richa':					 ['m3',	'm1'],
'iguacu_jordao':						 ['m3',	'm1'],
'iguacu_salto_osorio':						 ['m3',	'm1'],
'iguacu_salto_santiago':					 ['m3',	'm1'],
'iguacu_santa_clara':						 ['m3',	'm1'],
'iguacu_segredo':						 ['m3',	'm1'],
'jacui_castro_alves':						 ['m3',	'm1'],
'jacui_dona_francisca':						 ['m3',	'm1'],
'jacui_ernestina':						 ['m3',	'm1'],
'jacui_itauba':							 ['m3',	'm1'],
'jacui_jacui':							 ['m3',	'm1'],
'jacui_monte_claro':						 ['m3',	'm1'],
'jacui_passo_real':						 ['m3',	'm1'],
'paraiba_do_sul_anta':						 ['m3',	'm1'],
'paraiba_do_sul_ilha_dos_pombos':			         ['m3',	'm1'],
'paraiba_do_sul_jaguari':					 ['m3',	'm1'],
'paraiba_do_sul_paraibuna':					 ['m3',	'm3'],
'paraiba_do_sul_picada':					 ['m3',	'm3'],
'paraiba_do_sul_santa_branca':					 ['m3',	'm3'],
'paraiba_do_sul_santa_cecilia':					 ['m3',	'm1'],
'paraiba_do_sul_santana':					 ['m3',	'm1'],
'paraiba_do_sul_sobragi':					 ['m3',	'm3'],
'paraiba_do_sul_tocos':						 ['m3',	'm1'],
'parana_ilha_solteira':						 ['m3',	'm1'],
'parana_itaipu':						 ['m1',	'm1'],
'parana_jupia':							 ['m3',	'm1'],
'parana_porto_primavera':					 ['m3',	'm1'],
'paranaiba_barra_dos_coqueiros':				 ['m1',	'm1'],
'paranaiba_batalha':						 ['m3',	'm3'],
'paranaiba_cachoeira_dourada':					 ['m3',	'm3'],
'paranaiba_cacu':						 ['m3',	'm1'],
'paranaiba_capim_branco_i':					 ['m3',	'm1'],
'paranaiba_capim_branco_ii':					 ['m3',	'm1'],
'paranaiba_corumba_i':						 ['m3',	'm3'],
'paranaiba_corumba_iii':					 ['m3',	'm3'],
'paranaiba_corumba_iv':						 ['m3',	'm3'],
'paranaiba_emborcacao':						 ['m3',	'm3'],
'paranaiba_foz_do_rio_claro':					 ['m3',	'm1'],
'paranaiba_itumbiara':						 ['m3',	'm3'],
'paranaiba_miranda':						 ['m3',	'm1'],
'paranaiba_nova_ponte':						 ['m3',	'm1'],
'paranaiba_salto':						 ['m2',	'm1'],
'paranaiba_salto_rio_verdinho':					 ['m2',	'm1'],
'paranaiba_sao_simao':						 ['m3',	'm1'],
'paranaiba_serra_do_facao':					 ['m3',	'm3'],
'paranapanema_canoas_i':					 ['m3',	'm3'],
'paranapanema_canoas_ii':					 ['m3',	'm3'],
'paranapanema_capivara':					 ['m3',	'm3'],
'paranapanema_chavantes':					 ['m3',	'm3'],
'paranapanema_jurumirim':					 ['m3',	'm3'],
'paranapanema_maua':						 ['m2',	'm3'],
'paranapanema_ourinhos':					 ['m3',	'm3'],
'paranapanema_piraju':						 ['m3',	'm3'],
'paranapanema_rosana':			     			 ['m3', 'm3'],
'paranapanema_taquarucu_escola_politecnica':			 ['m3', 'm3'],
'sao_francisco_apolonio_sales':             			 ['m3', 'm3'],
'sao_francisco_itaparica':					 ['m3',	'm3'],
'sao_francisco_paulo_afonso':					 ['m3',	'm3'],
'sao_francisco_queimado':					 ['m3',	'm3'],
'sao_francisco_retiro_baixo':					 ['m3',	'm3'],
'sao_francisco_sobradinho':					 ['m3',	'm3'],
'sao_francisco_sobradinho_inc':					 ['m3',	'm3'],
'sao_francisco_tres_marias':					 ['m3',	'm3'],
'sao_francisco_xingo':						 ['m3',	'm3'],
'tiete_bariri':							 ['m3',	'm1'],
'tiete_barra_bonita':						 ['m3',	'm1'],
'tiete_billings':						 ['m3',	'm1'],
'tiete_edgard_de_souza':					 ['m3',	'm1'],
'tiete_guarapiranga':						 ['m3',	'm1'],
'tiete_ibitinga':						 ['m3',	'm1'],
'tiete_nova_avanhandava':					 ['m3',	'm1'],
'tiete_ponte_nova':						 ['m3',	'm3'],
'tiete_promissao':						 ['m3',	'm1'],
'tiete_tres_irmaos':						 ['m3',	'm1'],
'tocantins_cana_brava':						 ['m3',	'm3'],
'tocantins_estreito_tocantins':				         ['m3',	'm3'],
'tocantins_lajeado':						 ['m3',	'm3'],
'tocantins_peixe_angical':					 ['m3', 'm3'],
'tocantins_sao_salvador':					 ['m3',	'm3'],
'tocantins_serra_da_mesa':					 ['m3', 'm3'],
'tocantins_tucurui':						 ['m3',	'm3'],
'uruguai_barra_grande':						 ['m3',	'm1'],
'uruguai_campos_novos':						 ['m3',	'm1'],
'uruguai_foz_do_chapeco':					 ['m3',	'm1'],
'uruguai_garibaldi':						 ['m3',	'm1'],
'uruguai_ita':							 ['m3',	'm1'],
'uruguai_machadinho':						 ['m3',	'm1'],
'uruguai_monjolinho':						 ['m3',	'm1'],
'uruguai_passo_fundo':						 ['m3',	'm1'],
'uruguai_passo_sao_joao':					 ['m3',	'm1'],
'uruguai_quebra_queixo':					 ['m1',	'm1'],
'uruguai_sao_jose':                       			 ['m3', 'm1']}
