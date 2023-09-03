
#!/bin/bash
#SBATCH --job-name=randkey    # 设置作业名称
#SBATCH -p paration #分区名称
#SBATCH --output=randomkey.txt      # 设置输出文件名
#SBATCH --error=randkey.err       # 设置错误输出文件名


# 切换到代码所在目录
cd "$CODE_DIR"

# 运行Python代码
python random_key.py