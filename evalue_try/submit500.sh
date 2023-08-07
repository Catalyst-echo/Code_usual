#!/bin/bash
#SBATCH --job-name=helloworld500    # 设置作业名称
#SBATCH -p ty_public #分区名称
#SBATCH --output=helloworld500.out      # 设置输出文件名
#SBATCH --error=helloworld500.err       # 设置错误输出文件名

#激活venv环境
~/miniconda3/bin/python

# 切换到代码所在目录
cd /public/home/sxu202200903104/helloalone

# 运行Python代码
python evalue500.py