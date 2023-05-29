#!/bin/tcsh -e
#SBATCH --job-name=mitoEM 
#SBATCH --nodes=1 
#SBATCH --ntasks=1
#SBATCH --gpus-per-node=4
#SBATCH --cpus-per-task=32 
#SBATCH --mem=128GB # how much RAM to allocate
#SBATCH --time=120:00:00 # job execution time limit hrs:min:sec
#SBATCH --mail-type=BEGIN,END,FAIL. # mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=ezhil@bc.edu # where to send mail
#SBATCH --partition=weidf # see sinfo for available partitions

#SBATCH --output=main_%j.out

hostname

python scripts/amg.py --checkpoint ./sam_vit_h_4b8939.pth --model-type default --input /mmfs1/data/ezhil/BC/crops/high_res --output ./outputs_high --box-nms-thresh 0.4
