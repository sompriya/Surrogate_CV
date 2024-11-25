#!/bin/bash

#Change the deltaFat based on the free energy profile
python3 FES_from_Reweighting.py --colvar COLVAR --cv 2 --sigma 0.005 --deltaFat -3.0 --temp 340 --stride 10000 --skiprows 250000
 
rm deltaF.dat
touch deltaF.dat

for i in {1..225}
do
        sed -n '4s/.\{14\}//p' fes-rew_$i.dat >> deltaF.dat
done
