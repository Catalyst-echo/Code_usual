#!/bin/bash
#SBATCH --job-name=helloworld500    # Set the job name
#SBATCH -p ty_public # Set the partition name
#SBATCH --output=helloworld500out      # Set the output file name
#SBATCH --=helloworld500err.txt       # Set the error output file name

# You need to independently control the file path

# Run Python code
python evalue500.py