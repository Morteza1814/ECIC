#!/bin/bash

BINARY_NAME=${1}
N_WARM=${2}
N_SIM=${3}


ls -q $PWD/dpc3_traces/ | while read trace
do
    sleep 2
    array=($(pidof $BINARY_NAME))
    echo ${#array[@]}
    while [ ${#array[@]} -ge 8 ]
    do
        sleep 5
	array=($(pidof $BINARY_NAME))
    done

    echo $trace
    ./run_champsim.sh $BINARY_NAME $N_WARM $N_SIM ${trace##*/}  _config &
done
wait
exit 0

