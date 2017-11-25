# -*- coding:utf-8 -*-

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

        basin name - if macro:'macro name', if micro:'macro_micro name'.

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

hidropy_basins_directory = 'hidropy/shapes/basins/'

basins = {
1:{'basin':'amazonas'           , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
2:{'basin':'atlantico_leste'    , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
3:{'basin':'atlantico_sudeste'  , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
4:{'basin':'atlantico_sul'      , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
5:{'basin':'doce'               , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
6:{'basin':'grande'             , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
7:{'basin':'iguacu'             , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
8:{'basin':'jacui'              , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
9:{'basin':'paraguai'           , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
10:{'basin':'paraiba_do_sul'    , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
11:{'basin':'parana'            , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
12:{'basin':'paranaiba'         , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
13:{'basin':'paranapanema'      , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
14:{'basin':'parnaiba'          , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
15:{'basin':'sao_francisco'     , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },   
16:{'basin':'tiete'             , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
17:{'basin':'tocantins'         , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },   
18:{'basin':'uruguai'           , 'subbasin':''                                , 'macro':1, 'micro':0, 'tot':0, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },   

19:{'basin':'amazonas'          , 'subbasin':'balbina'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':269, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BALBINA'    },
20:{'basin':'amazonas'          , 'subbasin':'belo_monte'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':288, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PIMENTAL'   },
21:{'basin':'amazonas'          , 'subbasin':'cachoeira_caldeirao'             , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':204, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CACH.CALDEI'},
22:{'basin':'amazonas'          , 'subbasin':'coaracy_nunes'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':280, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'COARACY NUN'},
23:{'basin':'amazonas'          , 'subbasin':'coaracy_nunes_inc'               , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },       
24:{'basin':'amazonas'          , 'subbasin':'colider'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':228, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'COLIDER'    },
25:{'basin':'amazonas'          , 'subbasin':'colider_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },    
26:{'basin':'amazonas'          , 'subbasin':'curua_una'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':277, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CURUA-UNA'  },
27:{'basin':'amazonas'          , 'subbasin':'dardanelos'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':291, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'DARDANELOS' },
28:{'basin':'amazonas'          , 'subbasin':'ferreira_gomes'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':297, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'FERREIRA GO'},
29:{'basin':'amazonas'          , 'subbasin':'ferreira_gomes_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },      
30:{'basin':'amazonas'          , 'subbasin':'guapore'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':296, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'GUAPORE'    },
31:{'basin':'amazonas'          , 'subbasin':'jirau'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':285, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'JIRAU'      },
32:{'basin':'amazonas'          , 'subbasin':'jirau_inc'                       , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },      
33:{'basin':'amazonas'          , 'subbasin':'rondon_ii'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':145, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'RONDON II'  },
34:{'basin':'amazonas'          , 'subbasin':'samuel'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':279, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SAMUEL'     },
35:{'basin':'amazonas'          , 'subbasin':'santo_antonio'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':287, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'STO ANTONIO'},
36:{'basin':'amazonas'          , 'subbasin':'santo_antonio_inc'               , 'macro':0, 'micro':1, 'tot':0, 'form':1, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },      
37:{'basin':'amazonas'          , 'subbasin':'santo_antonio_do_jari'           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':290, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'STO ANT JAR'},
38:{'basin':'amazonas'          , 'subbasin':'sao_manuel'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':230, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SAO MANUEL' },
39:{'basin':'amazonas'          , 'subbasin':'sao_manuel_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        
40:{'basin':'amazonas'          , 'subbasin':'sinop'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':227, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SINOP'      },
41:{'basin':'amazonas'          , 'subbasin':'teles_pires'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':229, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'TELES PIRES'},
42:{'basin':'amazonas'          , 'subbasin':'teles_pires_inc'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },       

43:{'basin':'atlantico_leste'   , 'subbasin':'irape'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':255, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'IRAPE'      },
44:{'basin':'atlantico_leste'   , 'subbasin':'itapebi'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':188, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITAPEBI'    },
45:{'basin':'atlantico_leste'   , 'subbasin':'itapebi_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },         
46:{'basin':'atlantico_leste'   , 'subbasin':'pedra_do_cavalo'                 , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':254, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'P.CAVALO'   },
47:{'basin':'atlantico_leste'   , 'subbasin':'santa_clara'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':283, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'STA CLARA P'},
#48:{'basin':'atlantico_sudeste', 'subbasin':'henry_borden_art'                , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':318, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        

49:{'basin':'atlantico_sudeste' , 'subbasin':'lajes_fontes_nova_pereira_passos', 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':202, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'LAJES'      },
#50:{'basin':'atlantico_sudeste', 'subbasin':'pedras'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':116, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        
51:{'basin':'atlantico_sudeste' , 'subbasin':'rosal'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':196, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ROSAL'      },

52:{'basin':'atlantico_sul'     , 'subbasin':'capivari_cachoeira'              , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':115, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'G.P.SOUZA'  },
53:{'basin':'atlantico_sul'     , 'subbasin':'salto_pilao'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':101, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SALTO PILAO'},

54:{'basin':'doce'              , 'subbasin':'aimores'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':148, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'AIMORES'    },
55:{'basin':'doce'              , 'subbasin':'aimores_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        
56:{'basin':'doce'              , 'subbasin':'baguari'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':141, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BAGUARI'    },
57:{'basin':'doce'              , 'subbasin':'baguari_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        
58:{'basin':'doce'              , 'subbasin':'cadonga'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':149, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CANDONGA'   },
59:{'basin':'doce'              , 'subbasin':'guilman'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':262, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'GUILMAN-AMO'},
60:{'basin':'doce'              , 'subbasin':'mascarenhas'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':144, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'MASCARENHAS'},
61:{'basin':'doce'              , 'subbasin':'mascarenhas_inc'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        
62:{'basin':'doce'              , 'subbasin':'porto_estrela'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':263, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'P. ESTRELA' },
63:{'basin':'doce'              , 'subbasin':'porto_estrela_inc'               , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        
64:{'basin':'doce'              , 'subbasin':'sa_carvalho'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':183, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SA CARVALHO'},
65:{'basin':'doce'              , 'subbasin':'sa_carvalho_inc'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        
66:{'basin':'doce'              , 'subbasin':'salto_grande'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':134, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SALTO GRAND'},

67:{'basin':'grande'            , 'subbasin':'agua_vermelha'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':18 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'A. VERMELHA'},      
68:{'basin':'grande'            , 'subbasin':'agua_vermelha_inc'               , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
69:{'basin':'grande'            , 'subbasin':'as_oliveira'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':16 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'A.S.OLIVEIR'},
70:{'basin':'grande'            , 'subbasin':'as_oliveira_inc'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        
71:{'basin':'grande'            , 'subbasin':'caconde'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':14 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CACONDE'    },
72:{'basin':'grande'            , 'subbasin':'camargos'                        , 'macro':0, 'micro':1, 'tot':1, 'form':1, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':1  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CAMARGOS'   },        
73:{'basin':'grande'            , 'subbasin':'euclides_da_cunha'               , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':15 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'E. DA CUNHA'},
74:{'basin':'grande'            , 'subbasin':'euclides_da_cunha_inc'           , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },       
75:{'basin':'grande'            , 'subbasin':'funil_grande'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':211, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'FUNIL-GRAND'},
76:{'basin':'grande'            , 'subbasin':'funil_grande_inc'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },         
77:{'basin':'grande'            , 'subbasin':'furnas'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':6  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'FURNAS'     },        
78:{'basin':'grande'            , 'subbasin':'furnas_inc'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },       
79:{'basin':'grande'            , 'subbasin':'igarapava'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':10 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'IGARAPAVA'  },
80:{'basin':'grande'            , 'subbasin':'igarapava_inc'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },        
81:{'basin':'grande'            , 'subbasin':'itutinga'                        , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':2  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITUTINGA'   }, 
82:{'basin':'grande'            , 'subbasin':'itutinga_inc'                    , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
83:{'basin':'grande'            , 'subbasin':'jaguara'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':9  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'JAGUARA'    },
84:{'basin':'grande'            , 'subbasin':'jaguara_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
85:{'basin':'grande'            , 'subbasin':'lc_barreto'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':8  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ESTREITO'   },
86:{'basin':'grande'            , 'subbasin':'lc_barreto_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
87:{'basin':'grande'            , 'subbasin':'marimbondo'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':17 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'MARIMBONDO' },
88:{'basin':'grande'            , 'subbasin':'marimbondo_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
89:{'basin':'grande'            , 'subbasin':'mascarenhas_de_moraes'           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod': 7 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'M. DE MORAE'},
90:{'basin':'grande'            , 'subbasin':'mascarenhas_de_moraes_inc'       , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
91:{'basin':'grande'            , 'subbasin':'porto_colombia'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':12 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'P. COLOMBIA'},
92:{'basin':'grande'            , 'subbasin':'porto_colombia_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
93:{'basin':'grande'            , 'subbasin':'volta_grande'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':11 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'VOLTA GRAND'},
94:{'basin':'grande'            , 'subbasin':'volta_grande_inc'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },

95:{'basin':'iguacu'            , 'subbasin':'baixo_iguacu'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':81 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BAIXO IGUAC'},
96:{'basin':'iguacu'            , 'subbasin':'baixo_iguacu_inc'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
97:{'basin':'iguacu'            , 'subbasin':'foz_do_areia'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':74 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'G.B.MUNHOZ' },
98:{'basin':'iguacu'            , 'subbasin':'fundao'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':72 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'FUNDAO'     },
99:{'basin':'iguacu'            , 'subbasin':'fundao_inc'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
100:{'basin':'iguacu'           , 'subbasin':'gov_jose_richa'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':222, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SALTO CAXIA'},
101:{'basin':'iguacu'           , 'subbasin':'gov_jose_richa_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
102:{'basin':'iguacu'           , 'subbasin':'jordao'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':73 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'JORDAO'     },
103:{'basin':'iguacu'           , 'subbasin':'jordao_inc'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
104:{'basin':'iguacu'           , 'subbasin':'salto_osorio'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':78 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SALTO OSORI'},
105:{'basin':'iguacu'           , 'subbasin':'salto_osorio_inc'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
106:{'basin':'iguacu'           , 'subbasin':'salto_santiago'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':77 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SLT.SANTIAG'},
107:{'basin':'iguacu'           , 'subbasin':'salto_santiago_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
108:{'basin':'iguacu'           , 'subbasin':'santa_clara'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':71 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'STA CLARA P'},
109:{'basin':'iguacu'           , 'subbasin':'segredo'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':76 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SEGREDO'    },
110:{'basin':'iguacu'           , 'subbasin':'segredo_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
 
111:{'basin':'jacui'            , 'subbasin':'14_de_julho'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':284, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'14 DE JULHO'},
112:{'basin':'jacui'            , 'subbasin':'14_de_julho_inc'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
113:{'basin':'jacui'            , 'subbasin':'castro_alves'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':98 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CASTRO ALVE'},
114:{'basin':'jacui'            , 'subbasin':'dona_francisca'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':114, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'D.FRANCISCA'},
115:{'basin':'jacui'            , 'subbasin':'dona_francisca_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
116:{'basin':'jacui'            , 'subbasin':'ernestina'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':110, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ERNESTINA'  },
117:{'basin':'jacui'            , 'subbasin':'itauba'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':113, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITAUBA'     },
118:{'basin':'jacui'            , 'subbasin':'itauba_inc'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
119:{'basin':'jacui'            , 'subbasin':'jacui'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':112, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'JACUI'      }, 
120:{'basin':'jacui'            , 'subbasin':'jacui_inc'                       , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
121:{'basin':'jacui'            , 'subbasin':'monte_claro'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':97 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'MONTE CLARO'},
122:{'basin':'jacui'            , 'subbasin':'monte_claro_inc'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
123:{'basin':'jacui'            , 'subbasin':'passo_real'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':111, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PASSO REAL' },
124:{'basin':'jacui'            , 'subbasin':'passo_real_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },

125:{'basin':'paraguai'         , 'subbasin':'itiquira'                        , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':259, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITIQUIRA I' },
126:{'basin':'paraguai'         , 'subbasin':'jauru'                           , 'macro':0, 'micro':1, 'tot':1, 'form':1, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':295, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'JAURU'      },
127:{'basin':'paraguai'         , 'subbasin':'manso'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':278, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'MANSO'      },
128:{'basin':'paraguai'         , 'subbasin':'ponte_de_pedra'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':281, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PONTE PEDRA'},

129:{'basin':'paraiba_do_sul'   , 'subbasin':'anta'                            , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':129, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ANTA'       },
130:{'basin':'paraiba_do_sul'   , 'subbasin':'anta_inc'                        , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
131:{'basin':'paraiba_do_sul'   , 'subbasin':'funil'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':123, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'FUNIL'      },
132:{'basin':'paraiba_do_sul'   , 'subbasin':'funil_inc'                       , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
133:{'basin':'paraiba_do_sul'   , 'subbasin':'ilha_dos_pombos'                 , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':130, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'I. POMBOS'  },
134:{'basin':'paraiba_do_sul'   , 'subbasin':'ilha_dos_pombos_inc'             , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
135:{'basin':'paraiba_do_sul'   , 'subbasin':'jaguari'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':120, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'JAGUARI'    },
136:{'basin':'paraiba_do_sul'   , 'subbasin':'itaocara_i'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':199, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITAOCARA I' },
137:{'basin':'paraiba_do_sul'   , 'subbasin':'itaocara_i_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
138:{'basin':'paraiba_do_sul'   , 'subbasin':'paraibuna'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':121, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PARAIBUNA'  },
139:{'basin':'paraiba_do_sul'   , 'subbasin':'picada'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':197, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PICADA'     },
140:{'basin':'paraiba_do_sul'   , 'subbasin':'santa_branca'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':122, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SANTA BRANC'},
141:{'basin':'paraiba_do_sul'   , 'subbasin':'santa_branca_inc'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
142:{'basin':'paraiba_do_sul'   , 'subbasin':'santa_cecilia'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':125, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'STA CECILIA'},
143:{'basin':'paraiba_do_sul'   , 'subbasin':'santa_cecilia_inc'               , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
144:{'basin':'paraiba_do_sul'   , 'subbasin':'santana'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':203, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SANTANA'    },
145:{'basin':'paraiba_do_sul'   , 'subbasin':'santana_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
146:{'basin':'paraiba_do_sul'   , 'subbasin':'sobragi'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':198, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SOBRAGI'    },
147:{'basin':'paraiba_do_sul'   , 'subbasin':'sobragi_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
148:{'basin':'paraiba_do_sul'   , 'subbasin':'tocos'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':201, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'TOCOS'      },

149:{'basin':'parana'           , 'subbasin':'ilha_solteira'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':34 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'I.SOLTEIRA' },
150:{'basin':'parana'           , 'subbasin':'ilha_solteira_inc'               , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
151:{'basin':'parana'           , 'subbasin':'ilha_solteira_equivalente'       , 'macro':0, 'micro':1, 'tot':1, 'form':1, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':244, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'I.SOLT. EQV'},
152:{'basin':'parana'           , 'subbasin':'ilha_solteira_equivalente_inc'   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
153:{'basin':'parana'           , 'subbasin':'itaipu'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':266, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITAIPU'     },
154:{'basin':'parana'           , 'subbasin':'itaipu_inc'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
155:{'basin':'parana'           , 'subbasin':'jupia'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':245, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'JUPIA'      },
156:{'basin':'parana'           , 'subbasin':'jupia_inc'                       , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
157:{'basin':'parana'           , 'subbasin':'porto_primavera'                 , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':246, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'P.PRIMAVERA'},
158:{'basin':'parana'           , 'subbasin':'porto_primavera_inc'             , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },

159:{'basin':'paranaiba'        , 'subbasin':'barra_dos_coqueiros'             , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':248, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BARRA DOS C'},
160:{'basin':'paranaiba'        , 'subbasin':'barra_dos_coqueiros_inc'         , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
161:{'basin':'paranaiba'        , 'subbasin':'batalha'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':22 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BATALHA'    },
162:{'basin':'paranaiba'        , 'subbasin':'cachoeira_dourada'               , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':32 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CACH.DOURAD'},
163:{'basin':'paranaiba'        , 'subbasin':'cachoeira_dourada_inc'           , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
164:{'basin':'paranaiba'        , 'subbasin':'cacu'                            , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':247, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CACU'       },
165:{'basin':'paranaiba'        , 'subbasin':'capim_branco_i'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':207, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CAPIM BRANC'},
166:{'basin':'paranaiba'        , 'subbasin':'capim_branco_i_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
167:{'basin':'paranaiba'        , 'subbasin':'capim_branco_ii'                 , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':28 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CAPIM BRANC'},
168:{'basin':'paranaiba'        , 'subbasin':'capim_branco_ii_inc'             , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
169:{'basin':'paranaiba'        , 'subbasin':'corumba_i'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':209, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CORUMBA I'  },
170:{'basin':'paranaiba'        , 'subbasin':'corumba_i_inc'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
171:{'basin':'paranaiba'        , 'subbasin':'corumba_iii'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':23 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CORUMBA III'},
172:{'basin':'paranaiba'        , 'subbasin':'corumba_iii_inc'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
173:{'basin':'paranaiba'        , 'subbasin':'corumba_iv'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':205, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CORUMBA IV' },
174:{'basin':'paranaiba'        , 'subbasin':'emborcacao'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':24 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'EMBORCACAO' },
175:{'basin':'paranaiba'        , 'subbasin':'emborcacao_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
176:{'basin':'paranaiba'        , 'subbasin':'espora'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':99 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ESPORA'     },
177:{'basin':'paranaiba'        , 'subbasin':'foz_do_rio_claro'                , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':261, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'FOZ DO RIO' },
178:{'basin':'paranaiba'        , 'subbasin':'foz_do_rio_claro_inc'            , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
179:{'basin':'paranaiba'        , 'subbasin':'itumbiara'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':31 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITUMBIARA'  },
180:{'basin':'paranaiba'        , 'subbasin':'itumbiara_inc'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
181:{'basin':'paranaiba'        , 'subbasin':'miranda'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':206, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'MIRANDA'    },
182:{'basin':'paranaiba'        , 'subbasin':'miranda_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
183:{'basin':'paranaiba'        , 'subbasin':'nova_ponte'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':25 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'NOVA PONTE' },
184:{'basin':'paranaiba'        , 'subbasin':'salto'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':294, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SALTO'      },
185:{'basin':'paranaiba'        , 'subbasin':'salto_rio_verdinho'              , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':241, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SALTO DO RI'},
186:{'basin':'paranaiba'        , 'subbasin':'salto_rio_verdinho_inc'          , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
187:{'basin':'paranaiba'        , 'subbasin':'sao_simao'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':33 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SAO SIMAO'  },
188:{'basin':'paranaiba'        , 'subbasin':'sao_simao_inc'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
189:{'basin':'paranaiba'        , 'subbasin':'serra_do_facao'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':251, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SERRA FACAO'},
190:{'basin':'paranaiba'        , 'subbasin':'serra_do_facao_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },

191:{'basin':'paranapanema'     , 'subbasin':'canoas_i'                        , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':52 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CANOAS I'   },
192:{'basin':'paranapanema'     , 'subbasin':'canoas_i_inc'                    , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
193:{'basin':'paranapanema'     , 'subbasin':'canoas_ii'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':51 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CANOAS II'  },
194:{'basin':'paranapanema'     , 'subbasin':'canoas_ii_inc'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
195:{'basin':'paranapanema'     , 'subbasin':'capivara'                        , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':61 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CAPIVARA'   },
196:{'basin':'paranapanema'     , 'subbasin':'capivara_inc'                    , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
197:{'basin':'paranapanema'     , 'subbasin':'chavantes'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':49 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CHAVANTES'  },
198:{'basin':'paranapanema'     , 'subbasin':'chavantes_inc'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
199:{'basin':'paranapanema'     , 'subbasin':'jurumirim'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':47 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'A.A.LAYDNER'},
200:{'basin':'paranapanema'     , 'subbasin':'maua'                            , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':57 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'MAUA'       },
201:{'basin':'paranapanema'     , 'subbasin':'ourinhos'                        , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':249, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'OURINHOS'   },
202:{'basin':'paranapanema'     , 'subbasin':'ourinhos_inc'                    , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
203:{'basin':'paranapanema'     , 'subbasin':'piraju'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':48 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PIRAJU'     },
204:{'basin':'paranapanema'     , 'subbasin':'piraju_inc'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
205:{'basin':'paranapanema'     , 'subbasin':'rosana'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':63 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ROSANA'     },
206:{'basin':'paranapanema'     , 'subbasin':'rosana_inc'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
207:{'basin':'paranapanema'     , 'subbasin':'salto_grande_l_n_garcez'         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':50 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'L.N. GARCEZ'},
208:{'basin':'paranapanema'     , 'subbasin':'salto_grande_l_n_garcez_inc'     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
209:{'basin':'paranapanema'     , 'subbasin':'taquarucu_escola_politecnica'    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':62 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'TAQUARUCU'  },
210:{'basin':'paranapanema'     , 'subbasin':'taquarucu_escola_politecnica_inc', 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },

211:{'basin':'parnaiba'         , 'subbasin':'boa_esperanca'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':190, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'B. ESPERANC'},

212:{'basin':'sao_francisco'    , 'subbasin':'apolonio_sales'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':173, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'MOXOTO'     },
213:{'basin':'sao_francisco'    , 'subbasin':'apolonio_sales_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
214:{'basin':'sao_francisco'    , 'subbasin':'complexo_paulo_afonso'           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':176, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'COMP. MOXOT'},
215:{'basin':'sao_francisco'    , 'subbasin':'complexo_paulo_afonso_inc'       , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
216:{'basin':'sao_francisco'    , 'subbasin':'itaparica'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':172, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITAPARICA'  },
217:{'basin':'sao_francisco'    , 'subbasin':'itaparica_inc'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':171, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITAPARICA F'},
##### MUDAR OS NUMEROS A PARTIR DAQUI
219:{'basin':'sao_francisco'    , 'subbasin':'paulo_afonso'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':175, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'P.AFONSO 12'},
220:{'basin':'sao_francisco'    , 'subbasin':'paulo_afonso_inc'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
221:{'basin':'sao_francisco'    , 'subbasin':'queimado'                        , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':158, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'QUEIMADO'   },
222:{'basin':'sao_francisco'    , 'subbasin':'retiro_baixo'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':155, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'RETIRO BAIX'},
223:{'basin':'sao_francisco'    , 'subbasin':'sobradinho'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':169, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SOBRADINHO' },
224:{'basin':'sao_francisco'    , 'subbasin':'sobradinho_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':168, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SOBRADINHO' },
225:{'basin':'sao_francisco'    , 'subbasin':'tres_marias'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':156, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'TRES MARIAS'},
226:{'basin':'sao_francisco'    , 'subbasin':'tres_marias_inc'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
227:{'basin':'sao_francisco'    , 'subbasin':'xingo'                           , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':178, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'XINGO'      },
228:{'basin':'sao_francisco'    , 'subbasin':'xingo_inc'                       , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },

229:{'basin':'tiete'            , 'subbasin':'bariri'                          , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':238, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'A.S.LIMA'   },
230:{'basin':'tiete'            , 'subbasin':'bariri_inc'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
231:{'basin':'tiete'            , 'subbasin':'barra_bonita'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':237, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BARRA BONIT'},
232:{'basin':'tiete'            , 'subbasin':'barra_bonita_inc'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
233:{'basin':'tiete'            , 'subbasin':'billings'                        , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':118, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BILLINGS'   },
234:{'basin':'tiete'            , 'subbasin':'billings_mais_pedras'            , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':119, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BILLINGS'   },
235:{'basin':'tiete'            , 'subbasin':'edgard_de_souza'                 , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':161, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'E.SOUZA'    },
236:{'basin':'tiete'            , 'subbasin':'edgard_de_souza_inc'             , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
237:{'basin':'tiete'            , 'subbasin':'guarapiranga'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':117, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'GUARAPIRANG'},
238:{'basin':'tiete'            , 'subbasin':'ibitinga'                        , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':239, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'IBITINGA'   },
239:{'basin':'tiete'            , 'subbasin':'ibitinga_inc'                    , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
240:{'basin':'tiete'            , 'subbasin':'nova_avanhandava'                , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':242, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'NAVANHANDAV'},
241:{'basin':'tiete'            , 'subbasin':'nova_avanhandava_inc'            , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
242:{'basin':'tiete'            , 'subbasin':'ponte_nova'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':160, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ALTO TIETE' },
243:{'basin':'tiete'            , 'subbasin':'promissao'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':240, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PROMISSAO'  },
244:{'basin':'tiete'            , 'subbasin':'promissao_inc'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
245:{'basin':'tiete'            , 'subbasin':'traicao'                         , 'macro':0, 'micro':1, 'tot':1, 'form':1, 'inc':0, 'art':0, 'totinc':1, 'cab':1, 'cod':104, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'TRAICAO'    },
246:{'basin':'tiete'            , 'subbasin':'traicao_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
247:{'basin':'tiete'            , 'subbasin':'tres_irmaos'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':243, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'T.IRMAOS'   },
248:{'basin':'tiete'            , 'subbasin':'tres_irmaos_inc'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },

249:{'basin':'tocantins'        , 'subbasin':'cana_brava'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':191, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CANA BRAVA' },
250:{'basin':'tocantins'        , 'subbasin':'estreito_tocantins'              , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':271, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ESTREITO TO'},
251:{'basin':'tocantins'        , 'subbasin':'estreito_tocantins_inc'          , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
252:{'basin':'tocantins'        , 'subbasin':'lajeado'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':273, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'LAJEADO'    },
253:{'basin':'tocantins'        , 'subbasin':'lajeado_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
254:{'basin':'tocantins'        , 'subbasin':'peixe_angical'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':257, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PEIXE ANGIC'},
255:{'basin':'tocantins'        , 'subbasin':'peixe_angical_inc'               , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
256:{'basin':'tocantins'        , 'subbasin':'sao_salvador'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':253, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SAO SALVADO'},
257:{'basin':'tocantins'        , 'subbasin':'sao_salvador_inc'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
258:{'basin':'tocantins'        , 'subbasin':'serra_da_mesa'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':270, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SERRA MESA' },
259:{'basin':'tocantins'        , 'subbasin':'tucurui'                         , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':275, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'TUCURUI'    },
260:{'basin':'tocantins'        , 'subbasin':'tucurui_inc'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
261:{'basin':'tocantins'        , 'subbasin':'cana_brava_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },

262:{'basin':'uruguai'          , 'subbasin':'barra_grande'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':215, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BARRA GRAND'},
263:{'basin':'uruguai'          , 'subbasin':'campos_novos'                    , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':216, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'CAMPOS NOVO'},
264:{'basin':'uruguai'          , 'subbasin':'campos_novos_inc'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
265:{'basin':'uruguai'          , 'subbasin':'foz_do_chapeco'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':94 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'FOZ CHAPECO'},
266:{'basin':'uruguai'          , 'subbasin':'foz_do_chapeco_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
267:{'basin':'uruguai'          , 'subbasin':'garibaldi'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':89 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'GARIBALDI'  },
268:{'basin':'uruguai'          , 'subbasin':'garibaldi_inc'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
269:{'basin':'uruguai'          , 'subbasin':'ita'                             , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':92 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITA'        },
270:{'basin':'uruguai'          , 'subbasin':'ita_inc'                         , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
271:{'basin':'uruguai'          , 'subbasin':'machadinho'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':217, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'MACHADINHO' },
272:{'basin':'uruguai'          , 'subbasin':'machadinho_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
273:{'basin':'uruguai'          , 'subbasin':'monjolinho'                      , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':220, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'MONJOLINHO' },
274:{'basin':'uruguai'          , 'subbasin':'monjolinho_inc'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
275:{'basin':'uruguai'          , 'subbasin':'passo_fundo'                     , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':93 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PASSO FUNDO'},
276:{'basin':'uruguai'          , 'subbasin':'passo_sao_joao'                  , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':1, 'cab':0, 'cod':103, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PASSO SAO J'},
277:{'basin':'uruguai'          , 'subbasin':'passo_sao_joao_inc'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':1, 'art':0, 'totinc':0, 'cab':0, 'cod':0  , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':0            },
278:{'basin':'uruguai'          , 'subbasin':'quebra_queixo'                   , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':286, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'QUEBRA QUEI'},
279:{'basin':'uruguai'          , 'subbasin':'sao_jose'                        , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':102, 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SAO JOSE'   },
280:{'basin':'uruguai'          , 'subbasin':'sao_roque'                       , 'macro':0, 'micro':1, 'tot':1, 'form':0, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':88 , 'data':1, 'thiessen':1, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SAO ROQUE'  },


281:{'basin':'paraguai'         , 'subbasin':'itiquira_ii'                     , 'macro':0, 'micro':1, 'tot':1, 'form':1, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':252, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITIQUIRA II'},


282:{'basin':'tiete'            , 'subbasin':'barra_bonita_art'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':37 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BARRA BONIT'},
283:{'basin':'tiete'            , 'subbasin':'bariri_art'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':38 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'A.S.LIMA'   },
284:{'basin':'tiete'            , 'subbasin':'ibitinga_art'                    , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':39 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'IBITINGA'   },
285:{'basin':'tiete'            , 'subbasin':'promissao_art'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':40 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PROMISSAO'  },
286:{'basin':'tiete'            , 'subbasin':'nova_avanhandava_art'            , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':42 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'NAVANHANDAV'},
287:{'basin':'tiete'            , 'subbasin':'tres_irmaos_art'                 , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':43 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'T.IRMAOS'   },
288:{'basin':'parana'           , 'subbasin':'ilha_solteira_equivalente_art'   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':44 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'I.SOLT. EQV'},
289:{'basin':'parana'           , 'subbasin':'jupia_art'                       , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':45 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'JUPIA'      },
290:{'basin':'parana'           , 'subbasin':'porto_primavera_art'             , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':46 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'P.PRIMAVERA'},
291:{'basin':'parana'           , 'subbasin':'itaipu_art'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':66 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITAIPU'     },
292:{'basin':'iguacu'           , 'subbasin':'jordao_art'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':70 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'JORDAO'     },
293:{'basin':'iguacu'           , 'subbasin':'segredo_mais_desvio_art'         , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':75 , 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SEGREDO'    },
295:{'basin':'tiete'            , 'subbasin':'pedreira'                        , 'macro':0, 'micro':1, 'tot':1, 'form':1, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':109, 'data':0, 'thiessen':0, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':'PEDREIRA'   },
296:{'basin':'atlantico_sudeste', 'subbasin':'pedras'                          , 'macro':0, 'micro':1, 'tot':1, 'form':1, 'inc':0, 'art':0, 'totinc':0, 'cab':1, 'cod':116, 'data':0, 'thiessen':0, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':'PEDRAS'     },
297:{'basin':'tiete'            , 'subbasin':'billings_mais_pedras'            , 'macro':0, 'micro':1, 'tot':1, 'form':1, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':119, 'data':0, 'thiessen':0, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':0            },
298:{'basin':'paraiba_do_sul'   , 'subbasin':'simplicio_art'                   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':126, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SIMPLICIO'  },
299:{'basin':'paraiba_do_sul'   , 'subbasin':'anta_art'                        , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':127, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ANTA_ARTF'  },
300:{'basin':'paraiba_do_sul'   , 'subbasin':'nilo_pecanha_art'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':131, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'NILO PECANH'},
301:{'basin':'paraiba_do_sul'   , 'subbasin':'lajes_art'                       , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':132, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'LAJES'      },
302:{'basin':'tiete'            , 'subbasin':'edgard_de_souza_sem_tributarios' , 'macro':0, 'micro':1, 'tot':1, 'form':1, 'inc':0, 'art':0, 'totinc':0, 'cab':0, 'cod':164, 'data':0, 'thiessen':0, 'flow_mod':1, 'flow_petclim':1, 'art_flow_mod':0, 'art_flow_petclim':0, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':'E.SOUZA'    },

304:{'basin':'amazonas'         , 'subbasin':'belo_monte_principal_art'        , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':292, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BELO MONTE' },
305:{'basin':'paraiba_do_sul'   , 'subbasin':'santa_cecilia_bombeamento_art'   , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':298, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'STA CECILIA'},
306:{'basin':'paraiba_do_sul'   , 'subbasin':'ilhas_pombos_art'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':299, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'I. POMBOS'  },
307:{'basin':'amazonas'         , 'subbasin':'belo_monte_complementar_art'     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':302, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PIMENTAL AR'},
308:{'basin':'paraiba_do_sul'   , 'subbasin':'fontes_art'                      , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':303, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'FONTES'     },
309:{'basin':'paraiba_do_sul'   , 'subbasin':'santana_vertimento_art'          , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':304, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SANTANA'    },
310:{'basin':'paraiba_do_sul'   , 'subbasin':'pereira_passos_art'              , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':306, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'P. PASSOS'  },
311:{'basin':'paraiba_do_sul'   , 'subbasin':'itaocara_i_art'                  , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':314, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'ITAOCARA I' },
312:{'basin':'paraiba_do_sul'   , 'subbasin':'santana_art'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':315, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'SANTANA'    },
313:{'basin':'paraiba_do_sul'   , 'subbasin':'vigario_art'                     , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':316, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':0, 'vaz_totinc':0, 'vaz_tot_petclim':0, 'vaz_totinc_petclim':0, 'newave_name':'VIGARIO'    },
314:{'basin':'paraiba_do_sul'   , 'subbasin':'tocos_vertimento_art'            , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':317, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'TOCOS'      },
315:{'basin':'atlantico_sudeste', 'subbasin':'henry_borden_art'                , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':1, 'cod':318, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'PEDRAS'     },
316:{'basin':'tiete'            , 'subbasin':'billings_art'                    , 'macro':0, 'micro':1, 'tot':0, 'form':0, 'inc':0, 'art':1, 'totinc':0, 'cab':0, 'cod':319, 'data':0, 'thiessen':0, 'flow_mod':0, 'flow_petclim':0, 'art_flow_mod':1, 'art_flow_petclim':1, 'vaz_tot':1, 'vaz_totinc':1, 'vaz_tot_petclim':1, 'vaz_totinc_petclim':1, 'newave_name':'BILLINGS'   }
}


# Remember:0 == False and 1 == True

def basinsf(macro=0, micro=0, tot=0, form=0, inc=0, art=0, totinc=0, cab=0, cod=0, data=0, thiessen=0, flow_mod=0, flow_petclim=0, art_flow_mod=0, art_flow_petclim=0, vaz_tot=0, vaz_totinc=0, vaz_tot_petclim=0, vaz_totinc_petclim=0, newave_name=0):
    """
    macro:              Return list with only macro names if macro=1. Return macro name if macro=basin_subbasin (eg: macro=amazonas_balbina --> amazonas);
    micro:              Return list with macro_micro names if micro=1. Return micros of specific macro if micro=basin (eg: micro=grande --> ['grande_agua_vermelha', 'grande_agua_vermelha_inc', ...];
    tot:                Return list with macro_micro names (only total basins), eg:amazonas_balbina;
    form:               Return list with macro_micro names (only basins computed by equations), eg:tiete_traicao;
    inc:                Return list with macro_micro names (only incremental basins), ex:amazonas_balbina;
    art:                Return list with macro_micro names (only artificial basins), ex:amazonas_balbina;
    totinc:             Return list with macro_micro names (only basins computed by sum of incremental basins), ex:amazonas_ferreira_gomes_inc;
    cab:                Return list with macro_micro names (only hillslope watershed basins), ex:amazonas_ferreira_gomes;
    cod:                Return list with basins code (codes number(s)), eg:basinsf(cod='amazonas_belo_monte') ===> [288] or basinsf(cod=['amazonas_belo_monte','amazonas_balbina']) ===> [269, 288]
    data:               Return list with macro_micro names (only basins with data);
    thiessen:           Return list with macro_micro names (only basins with thiessen);
    flow_mod:           Return list with macro_micro names (only natural basins with flow computed by models);
    flow_petclim:       Return list with macro_micro names (only natural basins with flow computed by climatological pet);
    art_flow_mod:       Return list with macro_micro names (only artificial basins with flow computed by models);
    art_flow_petclim:   Return list with macro_micro names (only artificial basins with flow computed by climatological pet);
    vaz_tot:            Return list with macro_micro names (only basins);
    vaz_totinc:         Return list with macro_micro names (only basins computed by sum of incremental basins);
    vaz_tot_petclim:    Return list with macro_micro names (only basins computed by climatological pet);
    vaz_totinc_petclim: Return list with macro_micro names (only basins computed by sum of incremental basins and by climatological pet);
    newave_name:        Return list with cod, newave_name, macro, micro, cab (eg: [1,CAMARGOS,grande,camargos,0] );
    """
    
    lmacro              = []
    lmicro              = []
    ltot                = []
    lform               = []
    linc                = []
    lart                = []
    ltotinc             = []
    lcab                = []
    lcod                = []
    ldata               = []
    lthiessen           = []
    lflow_mod           = []
    lflow_petclim       = []
    lart_flow_mod       = []
    lart_flow_petclim   = []
    lvaz_tot            = []
    lvaz_totinc         = []
    lvaz_tot_petclim    = []
    lvaz_totinc_petclim = []
    lcodnames           = []
    lnewave_name        = []
    
    lbasin = []
    
    if macro==1:
        for i in basins:
            if basins[i]['macro']==1:
                lmacro.append(basins[i]['basin'])
    else:
        for i in basins:
            basin_name = basins[i]['basin']+"_"+basins[i]['subbasin']
            if basin_name == macro:
                return basins[i]['basin']
    
    if micro==1:
        for i in basins:
            if basins[i]['micro']==1:
                lmicro.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    if type(micro) == str:
        macro = 1
        for i in basins:
            ##print basins[i]['basin'], micro
            if (basins[i]['basin'] == micro) and basins[i]['subbasin'] != '':
                ##print i
                lmicro.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if tot==1:
        for i in basins:
            if basins[i]['tot']==1:
                ltot.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if form==1:
        for i in basins:
            if basins[i]['form']==1:
                ltot.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if inc==1:
        for i in basins:
            if basins[i]['inc']==1:
                linc.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if art==1:
        for i in basins:
            if basins[i]['art']==1:
                lart.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if totinc==1:
        for i in basins:
            if basins[i]['totinc']==1:
                ltotinc.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if cab == 1:
        for i in basins:
            if basins[i]['cab']==1:
                lcab.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if type(cab) == str:
        for i in basins:
            basin_name = basins[i]['basin']+"_"+basins[i]['subbasin']
            if basin_name==cab:
                return basins[i]['cab']
            
           
    if cod != 0:
        if cod=='all':
            for i in basins:
                basin_name = basins[i]['basin']+"_"+basins[i]['subbasin']
                if basins[i]['cod']!=0:
                    lcod.append(basins[i]['cod'])
                    lcodnames.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
                    
        if isinstance(cod, list):
            
            if isinstance(cod[0], str):
                for i in basins:
                    basin_name = basins[i]['basin']+"_"+basins[i]['subbasin']
                    for j in range(len(cod)): # Case passing a list of basin_subbasin name
                        if basin_name == cod[j]:
                            codes = basins[i]['cod']
                            lcod.append(codes)
                    if basin_name == cod:
                        codes = basins[i]['cod']
                        lcod.append(codes)
            
            elif isinstance(cod[0], int):
                for i in basins:
                    basin_name = basins[i]['basin']+"_"+basins[i]['subbasin']
                    for j in range(len(cod)): # Case passing a list of basins code
                        if basins[i]['cod'] == cod[j]:
                            lcod.append(basin_name)
                            
        elif isinstance(cod, str):
            for i in basins:
                basin_name = basins[i]['basin']+"_"+basins[i]['subbasin']
                if basin_name == cod:
                    codes = basins[i]['cod']
                    lcod.append(codes)
        
        elif isinstance(cod, int):
            for i in basins:
                basin_name = basins[i]['basin']+"_"+basins[i]['subbasin']
                if basins[i]['cod'] == cod:
                    # lcod.append(basin_name)
                    lcod.append(basin_name)
                           
        if lcodnames != []:
            """
            START TEST
            """
            # cod_list    = []
            # var_sum = 0
            # for i in lcod:
                # append_list = []
                # append_list.append(lcod[var_sum])
                # append_list.append(lcodnames[var_sum])
                # cod_list.append(append_list)
                # var_sum += 1
            # return cod_list
            """
            END
            """
            return lcod, lcodnames
        else:
            return lcod
    
    if data==1:
        for i in basins:
            if basins[i]['data']==1:
                ldata.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if thiessen==1:
        for i in basins:
            if basins[i]['thiessen']==1:
                lthiessen.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if flow_mod==1:
        for i in basins:
            if basins[i]['flow_mod']==1:
                lflow_mod.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if flow_petclim==1:
        for i in basins:
            if basins[i]['flow_petclim']==1:
                lflow_petclim.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if art_flow_mod==1:
        for i in basins:
            if basins[i]['art_flow_mod']==1:
                lart_flow_mod.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if art_flow_petclim==1:
        for i in basins:
            if basins[i]['art_flow_petclim']==1:
                lart_flow_petclim.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if vaz_tot==1:
        for i in basins:
            if basins[i]['vaz_tot']==1:
                lvaz_tot.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if vaz_totinc==1:
        for i in basins:
            if basins[i]['vaz_totinc']==1:
                lvaz_totinc.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if vaz_tot_petclim==1:
        for i in basins:
            if basins[i]['vaz_tot_petclim']==1:
                lvaz_tot_petclim.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if vaz_totinc_petclim==1:
        for i in basins:
            if basins[i]['vaz_totinc_petclim']==1:
                lvaz_totinc_petclim.append(basins[i]['basin']+"_"+basins[i]['subbasin'])
    
    if newave_name==1:
        for i in basins:
            tmp_cod =           []
            tmp_newave_name =   []
            tmp_basin =         []
            tmp_subbasin =      []
            tmp_cab =           []
            if (basins[i]['newave_name'] != '') and (basins[i]['newave_name'] != 0):
                tmp_cod         = basins[i]['cod']
                tmp_newave_name = basins[i]['newave_name']
                tmp_basin       = basins[i]['basin']
                tmp_subbasin    = basins[i]['subbasin']
                tmp_cab         = basins[i]['cab']
                tmp_newn        = [tmp_cod, tmp_newave_name, tmp_basin, tmp_subbasin, tmp_cab]
                lnewave_name.append(tmp_newn)
    
    lbasin = lmacro + lmicro + ltot + lform + linc + lart + ltotinc + lcab + ldata + \
             lthiessen + lflow_mod + lflow_petclim + lart_flow_mod + lart_flow_petclim + \
             lvaz_tot + lvaz_totinc + lvaz_tot_petclim + lvaz_totinc_petclim + lnewave_name

    return lbasin




# print basinsf(macro='tiete_traicao')
# print basinsf(cod='all')
# print basinsf(cod='paraguai_itiquira_ii')
# print basinsf(cod=['paraguai_itiquira_ii' , 'grande_camargos'])
# print basinsf(cod=252)
# print basinsf(cod=252)
# print basinsf(inc=1)
# print basinsf(form=1)
# print len(basinsf(form=1))
# print
# print basinsf(vaz_totinc=1)
# codigos,ncodigos = basinsf(cod='all')
# for i, j in enumerate(codigos):
    # print j, ncodigos[i]

# code_side = []
# for i in lcod:
    # icod      = "{0}".format(lcod[i])
    # icodname  = "{0}".format(lcodename[i])
    # code_side.append(icod, icodname)
# 
# print code_side

# print basinsf(cod=['amazonas_balbina','doce_cadonga'])




###### APAGAR QUANDO JA ESTIVER NO hidropy_utils.py ######

import subprocess

def lsname(path):
    """
    list a files or path using *.
    Return: the input path with ls output.
    """
    fname = subprocess.check_output("ls {}; exit 0".format(path),stderr=subprocess.STDOUT,shell=True)[0:-1]
    return fname
    
