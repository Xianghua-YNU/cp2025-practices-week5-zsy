import numpy as np
import matplotlib.pyplot as plt

def random_walk_displacement(num_steps, num_simulations):
    """
    模拟随机行走并返回每次模拟的最终位移

    参数:
    num_steps (int): 随机行走的步数
    num_simulations (int): 模拟的次数

    返回:
    numpy.ndarray: 形状为(2, num_simulations)的数组，表示每次模拟的最终位移
    """
    # TODO: 检查输入参数的有效性
    if num_steps <= 0 or num_simulations <= 0:
        raise ValueError("步数和模拟次数必须为正整数")
    # TODO: 实现随机行走算法
    # 提示：
    # 1. 使用 np.random.choice 生成随机步长 ([-1, 1])
    # 2. 生成形状为 (2, num_simulations, num_steps) 的数组
    directions = np.random.choice([-1, 1], size=(2, num_simulations, num_steps))
    # 3. 对步数维度求和得到最终位移
    final_displacements = np.cumsum(directions, axis=2)[:, :, -1]
    
    return final_displacements

    

def plot_displacement_distribution(final_displacements, bins=30):
    """
    绘制位移分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    # TODO: 实现位移分布的直方图绘制
    # 1. 计算每次模拟的最终位移
    x_displacements = final_displacements[0]
    y_displacements = final_displacements[1]
    # 2. 使用plt.hist绘制直方图
    plt.figure(figsize=(8, 6))
    plt.hist(x_displacements, bins=bins, alpha=0.5, label='Displacement in x direction')
    plt.hist(y_displacements, bins=bins, alpha=0.5, label='Displacement in y direction')
    # 3. 添加标题和标签
    plt.title('Displacement distribution histogram')
    plt.xlabel('displacement')
    plt.ylabel('frequency')
    plt.legend()
    
    plt.savefig('results/displacement_distribution.png', dpi=300)
    plt.show()

def plot_displacement_square_distribution(final_displacements, bins=30):
    """
    绘制位移平方分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    # TODO: 实现位移平方分布的直方图绘制
    # 1. 计算位移平方
    x_displacements = final_displacements[0]
    y_displacements = final_displacements[1]
    displacement_squares = x_displacements**2 + y_displacements**2
    # 2. 使用plt.hist绘制直方图
    plt.figure(figsize=(8, 6))
    plt.hist(displacement_squares, bins=bins, alpha=0.7)
    # 3. 添加标题和标签
    plt.title('Displacement square distribution histogram')
    plt.xlabel('Displacement squared')
    plt.ylabel('frequency')
    
    plt.savefig('results/displacement_square_distribution.png', dpi=300)
    plt.show()
    

if __name__ == "__main__":
    # 可调整的参数
    num_steps = 1000  # 随机行走的步数
    num_simulations = 1000  # 模拟的次数
    bins = 30  # 直方图的组数

    # TODO: 完成主程序逻辑
    # 1. 调用random_walk_displacement获取模拟结果
    displacements = random_walk_displacement(num_steps, num_simulations)
    # 2. 绘制位移分布直方图
    plot_displacement_distribution(displacements, bins)
    # 3. 绘制位移平方分布直方图
    plot_displacement_square_distribution(displacements, bins)
