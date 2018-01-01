#!/bin/bash

# Author = 'Funceme'
# Credits = 'Leidinice Silva'
# Maintainer = 'Funceme'
# Date = 18/12/2017  (dd/mm/aaaa)
# Comment = 'Este script foi desenvolvido dentro do Termo de Cooperação 
#	     0050.0100467.16.9 entre Funceme e Petrobras sob o contexto do
#	     Projeto Projeção de Vazão Natural Afluente com base na escala 
#	     de tempo e clima.'
# Description = 'This script calls remove_bias_pr_thiessen_rsm2008_daily.py in
#                order to remove daily pr bias from climate Model (RSM2008).'


mdate=`date +%m`
ydate=`date +%Y`

for model in rsm2008; do
            
    echo ${model} - ${ydate} - ${mdate}
    ${HIDROPY_PYTHON} /home/musf/leidinice/hidropy/hidropy/operational/remove_bias_pr_thiessen_rsm2008_daily.py --month_target=${mdate} --year_target=${ydate} --model_name=${model} --micro   
		    
done



