# Precise Calculation of the Natural Constant

The natural constant has a wide range of applications in science, nature, aerospace, manufacturing, and daily life.

In mathematics, formulas related to the natural constant often have concise properties.

More importantly, the natural constant originates from nature and shares similarities with the mathematical constant pi. Therefore, we can modify the method used to calculate pi to derive a method for calculating the natural constant.

This demonstrates the universality of the calculation method, which is worth researching and analyzing.

This project utilizes HPC (High-Performance Computing) for computation and is implemented using bash and Python.

# Introduction to HPC
HPC refers to the use of supercomputers and parallel processing techniques to solve complex computational problems. It involves using a large number of interconnected computers to collectively perform computations and data processing tasks at a faster and higher capacity than a single computer.

HPC is commonly used in scientific research, engineering, and other fields that require significant computational power. It enables researchers and scientists to simulate and analyze complex phenomena such as weather forecasting, climate modeling, molecular dynamics, and astrophysics.

HPC systems typically employ specialized hardware such as high-speed interconnections, parallel processing units, and large-scale storage systems to achieve high-performance levels. Parallel computing techniques, such as dividing tasks into smaller parts and processing them simultaneously, are used to effectively utilize available resources.

The application of HPC can significantly accelerate the discovery process, improve decision-making, and achieve breakthroughs in various disciplines.

# Advantages of Using HPC

The computation is distributed, making it suitable for HPC.

# Experimental Principle:
#### Mathematical Principle:

$$e^x = \sum_{n=0}^\infty\frac{x^n}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$$
where $n!$ denotes the factorial of $n$, i.e., $n! = 1\times2\times3\times\cdot\cdot\cdot\times n$.
When $n=1$, the series converges to $e$.
$$e = \sum_{n=0}^\infty\frac{1}{n!}=1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots$$
> Subsequently perform distribution operations.

Divide the original $\sum_{n=0}^\infty\frac{1}{n!}$ into 100 parts,
$$1+\sum_{n=0}^{\infty}\frac{1}{100n+1}+\frac{1}{100n+2}+\cdots+\frac{1}{100n+99}$$
Terminate the loop when the nth term is less than $10^{-500}$.

From a mathematical perspective, this method is indeed feasible.

###### The value of $e$ obtained using this method is extremely accurate, as the term $n!$ on the denominator contributes to very small errors.

#### Feasibility of Programming:
The sequence $n!$ has an evident recursive relationship, and the next term can be derived based on the previous one. Summing the terms yields $e$. The precision is affected by the number of expansion terms.
In general, the more expansion terms, the higher the precision.
Based on this idea, we can implement the computation using programming.

# File Introduction
## submit.sh
A bash script used to submit the job with sbatch.
## evalue_err.txt
Error log
## evalue_out.txt
Output log
## evalue.py
Implemented in Python, this program utilizes **multi-core programming** to calculate the natural constant $e$.

# Note
This README.md file is modified and adapted from my academic paper.

If you intend to cite or modify it, please be sure to provide proper attribution.

# Translate
* 【CN】[中文文档](https://github.com/ecahagain/Code_usual/blob/Paper/evalue_2023.8.6/README_CN.md)
