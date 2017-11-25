#!/bin/bash

###
# This script calls remove_bias_pr_thiessen_rsm2008_gqm_des_daily.py in order to 
# remove daily precipitation bias from Weather Model (RSM2008).
###

#__author__ = 'Leidinice Silva'
#__email__  = 'leidinice.silva@funceme.br'
#__date__   = '10/23/2017'


for model in rsm2008; do
    for ydate in `seq 1981 2017`; do
	for mdate in `seq 1 12`; do
            
	    echo ${model} - ${ydate} - ${mdate}
	    ${HIDROPY_PYTHON} /home/musf/leidinice/hidropy/hidropy/operational/remove_bias_pr_thiessen_rsm2008_gqm_des_daily.py --month_target=${mdate} --year_target=${ydate} --model_name=${model} --micro   
		    
        done
    done
done
