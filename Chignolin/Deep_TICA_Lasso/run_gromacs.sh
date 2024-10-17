#!/bin/bash

source source_gpu_gromacs.sh

gmx_mpi grompp -f md.mdp -c folded.gro -p topol_01.top -o input.tpr

export OMP_NUM_THREADS=2

mpiexec -n 1 gmx_mpi mdrun -s input.tpr -deffnm chignolin -plumed plumed.dat -nsteps 1250000000 -pin on -pinoffset 4 -gpu_id 0
