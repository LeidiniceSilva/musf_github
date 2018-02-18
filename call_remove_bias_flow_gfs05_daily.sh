#!/bin/bash

# Author = 'Funceme'
# Credits = 'Leidinice Silva'
# Maintainer = 'Funceme'
# Date = 18/12/2017  (dd/mm/aaaa)
# Comment = 'Este script foi desenvolvido dentro do Termo de Cooperação 
#	     0050.0100467.16.9 entre Funceme e Petrobras sob o contexto do
#	     Projeto Projeção de Vazão Natural Afluente com base na escala 
#	     de tempo e clima.'
# Description = 'This script calls remove_bias_flow_gfs05_daily.py in
#                order to remove daily flow bias from climate Model (GFS05).'


mdate=`date +%m`
ydate=`date +%Y`

for model in hymod smap; do
            
    echo ${model} - ${ydate} - ${mdate}
    ${HIDROPY_PYTHON} /home/musf/leidinice/hidropy/hidropy/operational/remove_bias_flow_gfs05_daily.py --month_target=${mdate} --year_target=${ydate} --model_name gfs05 --hydro_model=${model} --micro       
	               
done
