#!/bin/bash

###
# This script calls remove_bias_flow_rsm2008_daily_eqm_des.py in order to 
# remove daily flow bias from Weather Model (RSM2008).
###

#__author__ = 'Leidinice Silva'
#__email__  = 'leidinice.silva@funceme.br'
#__date__   = '10/23/2017'


for model in hymod smap; do
    for ydate in `seq 1981 2017`; do
    	for mdate in `seq 1 12`; do
            
	    echo ${model} - ${ydate} - ${mdate}
            ${HIDROPY_PYTHON} /home/musf/leidinice/hidropy/hidropy/operational/remove_bias_flow_rsm2008_eqm_des_daily.py --month_target=${mdate} --year_target=${ydate} --model_name rsm2008 --hydro_model=${model} --micro       
	               
        done
    done
done



