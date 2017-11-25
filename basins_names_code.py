# -*- coding: utf-8 -*-

"""
Dictionaries of the basins and the subbasins

> {basins}

    Itens format and locations:

        N:['macro basin name',
           'macro or micro basin name',
           'type macro or micro']

    where:

        N - number for ordenation, macro basin in 1:18, micro in 19:262.
        macro basin name - name of the macro basin, for macro and micro type.
        macro of micro basin name - name of the macro of micro basin in situ.
        smap parameter 1 - smap parameter 1
        smap parameter 2 - smap parameter 2
        smap parameter 3 - smap parameter 3
        smap parameter 4 - smap parameter 4
        type macro or micro - self explained

    Examples:

         1:['amazonas', 'amazonas', 'macro']
        19:['amazonas', 'balbina',  'micro'],

> {basin_n}

    Itens format and locations:

        'basin name':N

    where:

        basin name - if macro: 'macro name', if micro: 'macro_micro name'.

    Examples:

        'amazonas':1
        'amazonas_balbina':19

> {n_basin}

    Itens format and locations:

        N:'basin name'

    Exampĺes:

         1:'amazonas'
        19:'amazonas_balbina'


"""


basins_flow = {'amazonas_balbina': 269,
    'amazonas_belo_monte': 292,
    'amazonas_cachoeira_caldeirao': 204,
    'amazonas_coaracy_nunes': 280,
    'amazonas_coaracy_nunes_nc': 2800,
    'amazonas_colider': 228,
    'amazonas_colider_inc': 2280,
    'amazonas_curua_una': 277,
    'amazonas_dardanelos': 291,
    'amazonas_ferreira_gomes': 297,
    'amazonas_ferreira_gomes_inc': 2970,
    'amazonas_guapore': 296,
    'amazonas_jirau': 285,
    'amazonas_jirau_inc': 2850,
    'amazonas_rondon_ii': 145,
    'amazonas_samuel': 279,
    'amazonas_santo_antonio': 287,
    'amazonas_santo_antonio_inc': 2870,
    'amazonas_santo_antonio_do_jari': 290,
    'amazonas_sao_manuel': 230,
    'amazonas_sao_manuel_inc': 2300,
    'amazonas_sinop': 227,
    'amazonas_teles_pires': 229,
    'amazonas_teles_pires_inc': 2290,

    'atlantico_leste_irape': 255,
    'atlantico_leste_itapebi': 188,
    'atlantico_leste_itapebi_inc': 1880,
    'atlantico_leste_pedra_do_cavalo': 25,
    'atlantico_leste_santa_clara': 283,

    'atlantico_sudeste_henry_borden': 318,
    'atlantico_sudeste_lajes_fontes_nova_pereira_passos': 202,
    'atlantico_sudeste_pedras': 116,
    'atlantico_sudeste_rosal': 196,

    'atlantico_sul_capivari_cachoeira': 115,
    'atlantico_sul_salto_pilao': 101,

    'doce_aimores': 148,
    'doce_aimores_inc': 1480,
    'doce_baguari': 141,
    'doce_baguari_inc': 1410,
    'doce_cadonga': 149,
    'doce_guilman': 262,
    'doce_mascarenhas': 144,
    'doce_mascarenhas_inc': 1440,
    'doce_porto_estrela': 263,
    'doce_porto_estrela_inc': 2630,
    'doce_sa_carvalho': 183,
    'doce_sa_carvalho_inc': 1830,
    'doce_salto_grande': 134,

    'grande_agua_vermelha': 18,
    'grande_agua_vermelha_inc': 1800,
    'grande_as_oliveira': 16,
    'grande_as_oliveira_inc': 1600,
    'grande_caconde': 14,
    'grande_camargos': 1,
    'grande_euclides_da_cunha': 15,
    'grande_euclides_da_cunha_inc': 1500,
    'grande_funil_grande': 211,
    'grande_funil_grande_inc': 2110,
    'grande_furnas': 6,
    'grande_furnas_inc': 6000,
    'grande_igarapava': 10,
    'grande_igarapava_inc': 1000,
    'grande_itutinga': 2,
    'grande_itutinga_inc': 2000,
    'grande_jaguara': 9,
    'grande_jaguara_inc': 9000,
    'grande_lc_barreto': 8,
    'grande_lc_barreto_inc': 8000,
    'grande_marimbondo': 17,
    'grande_marimbondo_inc': 1700,
    'grande_mascarenhas_de_moraes': 7,
    'grande_mascarenhas_de_moraes_inc': 7000,
    'grande_porto_colombia': 12,
    'grande_porto_colombia_inc': 1200,
    'grande_volta_grande': 11,
    'grande_volta_grande_inc': 1100,

    'iguacu_baixo_iguacu': 81,
    'iguacu_baixo_iguacu_inc': 8100,
    'iguacu_foz_do_areia': 74,
    'iguacu_fundao': 72,
    'iguacu_fundao_inc': 7200,
    'iguacu_gov_jose_richa': 222,
    'iguacu_gov_jose_richa_inc': 2220,
    'iguacu_jordao': 73,
    'iguacu_jordao_inc': 7300,
    'iguacu_salto_osorio': 78,
    'iguacu_salto_osorio_inc': 7800,
    'iguacu_salto_santiago': 77,
    'iguacu_salto_santiago_inc': 7700,
    'iguacu_santa_clara': 71,
    'iguacu_segredo': 76,
    'iguacu_segredo_inc': 7600,

    'jacui_14_de_julho': 284,
    'jacui_14_de_julho_inc': 2840,
    'jacui_castro_alves': 98,
    'jacui_dona_francisca': 114,
    'jacui_dona_francisca_inc': 1140,
    'jacui_ernestina': 110,
    'jacui_itauba': 113,
    'jacui_itauba_inc': 1130,
    'jacui_jacui': 112,
    'jacui_jacui_inc': 1120,
    'jacui_monte_claro': 97,
    'jacui_monte_claro_inc': 9700,
    'jacui_passo_real': 111,
    'jacui_passo_real_inc': 1110,

    'paraguai_itiquira': 259,
    'paraguai_jauru': 295,
    'paraguai_manso': 278,
    'paraguai_ponte_de_pedra': 281,

    'paraiba_do_sul_anta': 129,
    'paraiba_do_sul_anta_inc': 1290,
    'paraiba_do_sul_funil': 123,
    'paraiba_do_sul_funil_inc': 1230,
    'paraiba_do_sul_ilha_dos_pombos': 130,
    'paraiba_do_sul_ilha_dos_pombos_inc': 1300,
    'paraiba_do_sul_jaguari': 120,
    'paraiba_do_sul_itaocara_i': 199,
    'paraiba_do_sul_itaocara_i_inc': 1990,
    'paraiba_do_sul_paraibuna': 121,
    'paraiba_do_sul_picada': 197,
    'paraiba_do_sul_santa_branca': 54,
    'paraiba_do_sul_santa_branca_inc': 5400,
    'paraiba_do_sul_santa_cecilia': 125,
    'paraiba_do_sul_santa_cecilia_inc': 1250,
    'paraiba_do_sul_santana': 203,
    'paraiba_do_sul_santana_inc': 2030,
    'paraiba_do_sul_sobragi': 198,
    'paraiba_do_sul_sobragi_inc': 1980,
    'paraiba_do_sul_tocos': 201,

    'parana_ilha_solteira': 34,
    'parana_ilha_solteira_inc': 3400,
    'parana_ilha_solteira_equivalente': 244,
    'parana_ilha_solteira_equivalente_inc': 2440,
    'parana_itaipu': 266,
    'parana_itaipu_inc': 2660,
    'parana_jupia': 245,
    'parana_jupia_inc': 2450,
    'parana_porto_primavera': 246,
    'parana_porto_primavera_inc': 2460,

    'paranaiba_barra_dos_coqueiros': 248,
    'paranaiba_barra_dos_coqueiros_inc': 2480,
    'paranaiba_batalha': 22,
    'paranaiba_cachoeira_dourada': 32,
    'paranaiba_cachoeira_dourada_inc': 3200,
    'paranaiba_cacu': 247,
    'paranaiba_capim_branco_i': 207,
    'paranaiba_capim_branco_i_inc': 2070,
    'paranaiba_capim_branco_ii': 28,
    'paranaiba_capim_branco_ii_inc': 2800,
    'paranaiba_corumba_i': 209,
    'paranaiba_corumba_i_inc': 2090,
    'paranaiba_corumba_iii': 23,
    'paranaiba_corumba_iii_inc': 23000,
    'paranaiba_corumba_iv': 205,
    'paranaiba_emborcacao': 24,
    'paranaiba_emborcacao_inc': 2400,
    'paranaiba_espora': 99,
    'paranaiba_foz_do_rio_claro': 261,
    'paranaiba_foz_do_rio_claro_inc': 2610,
    'paranaiba_itumbiara': 31,
    'paranaiba_itumbiara_inc': 3100,
    'paranaiba_miranda': 206,
    'paranaiba_miranda_inc': 2060,
    'paranaiba_nova_ponte': 25,
    'paranaiba_salto': 294,
    'paranaiba_salto_rio_verdinho': 241,
    'paranaiba_salto_rio_verdinho_inc': 2410,
    'paranaiba_sao_simao': 33,
    'paranaiba_sao_simao_inc': 3300,
    'paranaiba_serra_do_facao': 251,
    'paranaiba_serra_do_facao_inc': 2510,

    'paranapanema_canoas_i': 52,
    'paranapanema_canoas_i_inc': 5200,
    'paranapanema_canoas_ii': 51,
    'paranapanema_canoas_ii_inc': 5100,
    'paranapanema_capivara': 61,
    'paranapanema_capivara_inc': 6100,
    'paranapanema_chavantes': 49,
    'paranapanema_chavantes_inc': 4900,
    'paranapanema_jurumirim': 47,
    'paranapanema_maua': 57,
    'paranapanema_ourinhos': 249,
    'paranapanema_ourinhos_inc': 2490,
    'paranapanema_piraju': 48,
    'paranapanema_piraju_inc': 4800,
    'paranapanema_rosana': 63,
    'paranapanema_rosana_inc': 6300,
    'paranapanema_salto_grande_l_n_garcez': 50,
    'paranapanema_salto_grande_l_n_garcez_inc': 5000,
    'paranapanema_taquarucu_escola_politecnica': 62,
    'paranapanema_taquarucu_escola_politecnica_inc': 6200,

    'parnaiba_boa_esperanca': 190,

    'sao_francisco_apolonio_sales': 173,
    'sao_francisco_apolonio_sales_inc': 1730,
    'sao_francisco_complexo_paulo_afonso': 176,
    'sao_francisco_complexo_paulo_afonso_inc': 1760,
    'sao_francisco_itaparica': 172,
    'sao_francisco_itaparica_inc': 1720,
    'sao_francisco_paulo_afonso': 175,
    'sao_francisco_paulo_afonso_inc': 1750,
    'sao_francisco_queimado': 158,
    'sao_francisco_retiro_baixo': 155,
    'sao_francisco_sobradinho': 169,
    'sao_francisco_sobradinho_inc': 1690,
    'sao_francisco_tres_marias': 156,
    'sao_francisco_tres_marias_inc': 1560,
    'sao_francisco_xingo': 178,
    'sao_francisco_xingo_inc': 1780,

    'tiete_bariri': 238,
    'tiete_bariri_inc': 2380,
    'tiete_barra_bonita': 273,
    'tiete_barra_bonita_inc': 2730,
    'tiete_billings': 118,
    'tiete_billings_mais_pedras': 119,
    'tiete_edgard_de_souza': 161,
    'tiete_edgard_de_souza_inc': 1610,
    'tiete_guarapiranga': 117,
    'tiete_ibitinga': 239,
    'tiete_ibitinga_inc': 2390,
    'tiete_nova_avanhandava': 242,
    'tiete_nova_avanhandava_inc': 2420,
    'tiete_ponte_nova': 160,
    'tiete_promissao': 240,
    'tiete_promissao_inc': 24000,
    'tiete_traicao': 104,
    'tiete_traicao_inc': 1040,
    'tiete_tres_irmaos': 243,
    'tiete_tres_irmaos_inc': 2430,

    'tocantins_cana_brava': 191,
    'tocantins_estreito_tocantins': 271,
    'tocantins_estreito_tocantins_inc': 2710,
    'tocantins_lajeado': 273,
    'tocantins_lajeado_inc': 2730,
    'tocantins_peixe_angical': 257,
    'tocantins_peixe_angical_inc': 2570,
    'tocantins_sao_salvador': 253,
    'tocantins_sao_salvador_inc': 2530,
    'tocantins_serra_da_mesa': 270,
    'tocantins_tucurui': 275,
    'tocantins_tucurui_inc': 2750,
    'tocantins_cana_brava_inc': 275,

    'uruguai_barra_grande': 215,
    'uruguai_campos_novos': 216,
    'uruguai_campos_novos_inc': 2160,
    'uruguai_foz_do_chapeco': 94,
    'uruguai_foz_do_chapeco_inc': 9400,
    'uruguai_garibaldi': 89,
    'uruguai_garibaldi_inc': 8900,
    'uruguai_ita': 92,
    'uruguai_ita_inc': 9200,
    'uruguai_machadinho': 217,
    'uruguai_machadinho_inc': 2170,
    'uruguai_monjolinho': 220,
    'uruguai_monjolinho_inc': 2200,
    'uruguai_passo_fundo': 93,
    'uruguai_passo_sao_joao': 103,
    'uruguai_passo_sao_joao_inc': 1030,
    'uruguai_quebra_queixo': 286,
    'uruguai_sao_jose': 102,
    'uruguai_sao_roque': 88}
