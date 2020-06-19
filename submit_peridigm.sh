#!/bin/bash
#SBATCH --time=3:00:00
#SBATCH --nodes=1 --ntasks-per-node=6

module load peridigm

mpiexec -np 6 Peridigm meso_peri.peridigm