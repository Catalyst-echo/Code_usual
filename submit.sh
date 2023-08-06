#!/bin/bash
#SBATCH --job-name=helloworld    # 设置作业名称
#SBATCH -p $partion$ #分区名称
#SBATCH --output=evalue_out.txt      # 设置输出文件名
#SBATCH --error=evalue_err.txt       # 设置错误输出文件名
#SBATCH --nodes=1                # 设置节点数为1
#SBATCH --ntasks-per-node=1      # 每个节点执行一个进程
#SBATCH --cpus-per-task=16        # 设置每个任务使用的CPU核心数量
#SBATCH --mem=800MB                 # 设置每个进程使用的内存
#SBATCH --time=00:10:00           # 设置运行时间为1个小时

#激活venv环境
~/miniconda3/bin/python

# 切换到代码所在目录
cd /public/home/$local$

# 运行Python代码
python evalue.py