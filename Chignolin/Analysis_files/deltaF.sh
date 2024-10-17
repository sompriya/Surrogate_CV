#!/bin/bash

python3 FES_from_Reweighting.py --colvar COLVAR_2.0us --cv 2 --sigma 0.05 --deltaFat -3.0 --temp 340 --stride 10000 --skiprows 0000
 
rm deltaF.dat
touch deltaF.dat

for i in {1..200}
do
        sed -n '4s/.\{14\}//p' fes-rew_$i.dat >> deltaF.dat
done
