#!/bin/bash

#SBATCH --job-name=randkeymore    # 设置作业名称
#SBATCH -p paration #分区名称
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=16
#SBATCH --time=00:10:00
#SBATCH --output=randomkeymore.txt      # 设置输出文件名
#SBATCH --error=error.txt       # 设置错误输出文件名


# 进入工作目录
cd “$CODE_DIR”

# 运行Python代码
python random_keymore.py