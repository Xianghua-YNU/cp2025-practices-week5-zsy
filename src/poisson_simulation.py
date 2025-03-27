import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def plot_poisson_pmf(lambda_param=8, max_l=20):
    """绘制泊松分布的概率质量函数
    
    参数:
        lambda_param (float): 泊松分布参数λ
        max_l (int): 最大的l值
    """
    # TODO: 实现泊松分布概率质量函数的计算和绘制
    # 提示：
    # 1. 使用np.arange生成l值序列
    l_values = np.arange(0, max_l)
    # 2. 使用给定公式计算PMF
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    # 3. 使用plt绘制图形并设置标签
    plt.figure(figsize=(8, 6))
    plt.stem(l_values, pmf, linefmt='b-', markerfmt='bo', basefmt='g--')
    plt.title(f'poisson distribution PMF (λ={lambda_param})')
    plt.xlabel('l')
    plt.ylabel('probability')
    plt.grid(True)
    
    # 保存图片
    plt.savefig('results/poisson_pmf.png', dpi=300)
    plt.show()
    
    return pmf  # 返回计算的PMF值

    

def simulate_coin_flips(n_experiments=10000, n_flips=100, p_head=0.08):
    """模拟多组抛硬币实验
    
    参数:
        n_experiments (int): 实验组数N
        n_flips (int): 每组抛硬币次数
        p_head (float): 正面朝上的概率
        
    返回:
        ndarray: 每组实验中正面朝上的次数
    """
    # TODO: 实现多组抛硬币实验
    # 提示：
    # 1. 使用np.random.choice模拟硬币抛掷
    flips = np.random.choice([0, 1], size=(n_experiments, n_flips), p=[1-p_head, p_head])
    # 2. 统计每组实验中正面的次数
    heads_count = np.sum(flips, axis=1)
    
    return heads_count

def compare_simulation_theory(n_experiments=10000, lambda_param=8):
    """比较实验结果与理论分布
    
    参数:
        n_experiments (int): 实验组数
        lambda_param (float): 泊松分布参数λ
    """
    # TODO: 实现实验结果与理论分布的对比
    # 提示：
    # 1. 调用simulate_coin_flips获取实验结果
    heads_count = simulate_coin_flips(n_experiments, 100, 0.08)
    # 2. 计算理论分布
    max_l = 20
    l_values = np.arange(0, max_l + 1)
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    theoretical_counts = pmf * n_experiments
    # 3. 绘制直方图和理论曲线
    plt.figure(figsize=(10, 6))
    plt.hist(heads_count, bins=np.arange(-0.5, max_l + 0.5), alpha=0.7, label='实验结果', density=False)
    plt.plot(l_values, theoretical_counts, 'ro-', label='理论分布')
    plt.title(f'Comparison of experiment and theory (λ={lambda_param})')
    plt.xlabel('Number of heads')
    plt.ylabel('frequency')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('results/simulation_theory_comparison.png', dpi=300)
    plt.show()
    
    # 4. 计算并打印统计信息
    print("Experimental results statistics:")
    print(f"  Experimental group number: {n_experiments}")
    print(f"  Mean head count: {np.mean(heads_count):.2f}")
    print(f"  standard deviation: {np.std(heads_count):.2f}")


if __name__ == "__main__":
    # 设置随机种子
    np.random.seed(42)
    
    # 1. 绘制理论分布
    plot_poisson_pmf()
    
    # 2&3. 进行实验模拟并比较结果
    compare_simulation_theory()
    
    plt.show()
