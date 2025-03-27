import numpy as np
import matplotlib.pyplot as plt

def random_walk_finals(num_steps, num_walks):
    """生成多个二维随机游走的终点位置
    
    通过模拟多次随机游走，每次在x和y方向上随机选择±1移动，
    计算所有随机游走的终点坐标。每个随机游走都从原点(0,0)开始。

    参数:
        num_steps (int): 每次随机游走的步数
        num_walks (int): 随机游走的次数
        
    返回:
        tuple: 包含两个numpy数组的元组 (x_finals, y_finals)
            - x_finals: 所有随机游走终点的x坐标数组，长度为num_walks
            - y_finals: 所有随机游走终点的y坐标数组，长度为num_walks
            
    示例:
        >>> x_finals, y_finals = random_walk_finals(1000, 100)
        >>> print(f"第一个终点坐标: ({x_finals[0]}, {y_finals[0]})")
    """
    # TODO: 实现随机游走算法
    # 提示：
    if num_steps <= 0:
        return (np.zeros(num_walks), np.zeros(num_walks))
        
    # 1. 使用np.zeros初始化坐标数组
    x = np.zeros((num_walks, num_steps))
    y = np.zeros((num_walks, num_steps))
    # 2. 对每次游走使用np.random.choice生成±1的随机步长
    for i in range(num_steps - 1):
        step_x = np.random.choice([-1, 1], size=num_walks)
        step_y = np.random.choice([-1, 1], size=num_walks)
        x[:, i+1] = x[:, i] + step_x
        y[:, i+1] = y[:, i] + step_y
    # 3. 使用np.sum计算总位移
    x_finals = x[:, -1]
    y_finals = y[:, -1]
    
    return (x_finals, y_finals)
    

def plot_endpoints_distribution(endpoints):
    """绘制二维随机游走终点的空间分布散点图
    
    将多次随机游走的终点在二维平面上可视化，观察其空间分布特征。
    图形包含所有终点的散点图，并保持x和y轴的比例相同。

    参数:
        endpoints: 包含x和y坐标的元组 (x_coords, y_coords)
            - x_coords: numpy数组，所有终点的x坐标
            - y_coords: numpy数组，所有终点的y坐标
            
    示例:
        >>> endpoints = random_walk_finals(1000, 1000)
        >>> plot_endpoints_distribution(endpoints)
        >>> plt.show()
    """
    # TODO: 实现散点图绘制
    # 提示：
    # 1. 使用endpoints解包获取x和y坐标
    x_coords, y_coords = endpoints
    # 2. 使用plt.scatter绘制散点图
    plt.figure(figsize=(8, 6))
    # 3. 设置坐标轴比例、标题和标签
    plt.scatter(x_coords, y_coords, alpha=0.5)
    plt.title('随机游走终点分布')
    plt.xlabel('x坐标')
    plt.ylabel('y坐标')
    plt.axis('equal')
    
    plt.savefig('results/endpoints_distribution.png', dpi=300)
    plt.show()
    

def analyze_x_distribution(endpoints):
    """分析二维随机游走终点x坐标的统计特性
    
    对随机游走终点的x坐标进行统计分析，计算样本均值和样本方差，
    并通过直方图和理论正态分布曲线可视化其分布特征。理论上，
    大量随机游走的终点x坐标应该服从正态分布。

    参数:
        endpoints: 包含x和y坐标的元组 (x_coords, y_coords)
            - x_coords: numpy数组，所有终点的x坐标
            - y_coords: numpy数组，所有终点的y坐标
    
    返回:
        tuple: (mean, variance)
            - mean (float): x坐标的样本均值
            - variance (float): x坐标的样本方差（使用n-1作为分母）
            
    示例:
        >>> endpoints = random_walk_finals(1000, 1000)
        >>> mean, var = analyze_x_distribution(endpoints)
        >>> print(f"均值: {mean:.2f}, 方差: {var:.2f}")
    """
    # TODO: 实现统计分析和可视化
    # 提示：
    # 1. 提取x坐标数据
    x_coords, _ = endpoints
    # 2. 使用numpy计算均值和方差
    mean = np.mean(x_coords)
    variance = np.var(x_coords, ddof=1)
    # 3. 绘制直方图
    plt.figure(figsize=(8, 6))
    plt.hist(x_coords, bins=20, density=True, alpha=0.6, label='直方图')
    # 4. 添加理论正态分布曲线
    x = np.linspace(mean - 3*np.sqrt(variance), mean + 3*np.sqrt(variance), 100)
    norm_dist = (1 / (np.sqrt(2*np.pi*variance))) * np.exp(-(x - mean)**2 / (2*variance))
    plt.plot(x, norm_dist, 'r-', label='理论正态分布')
    # 5. 设置图形属性并打印统计结果
    plt.title('x坐标分布分析')
    plt.xlabel('x坐标')
    plt.ylabel('频率/密度')
    plt.legend()
    
    plt.savefig('results/x_distribution_analysis.png', dpi=300)
    plt.show()
    
    return (mean, variance)
    
if __name__ == "__main__":
    np.random.seed(42)  # 设置随机种子以保证可重复性
    
    # 生成数据
    endpoints = random_walk_finals(1000, 1000)

    # 创建图形
    plt.figure(figsize=(12, 5))
    
    # 绘制终点分布
    plt.subplot(121)
    plot_endpoints_distribution(endpoints)
    
    # 分析x坐标分布
    plt.subplot(122)
    analyze_x_distribution(endpoints)
    
    plt.tight_layout()
    plt.show()
