import matplotlib.pyplot as plt
import numpy as np

def random_walk_2d(steps):
    """生成二维随机行走轨迹
    
    参数:
        steps (int): 随机行走的步数
        
    返回:
        tuple: 包含x和y坐标序列的元组 (x_coords, y_coords)
    """
    # TODO: 实现随机行走算法
    # 提示：
    # 1. 使用 np.random.choice 生成随机步长 ([-1, 1])
    directions = np.random.choice([-1, 1], size=(steps, 2))
    # 2. 分别生成x和y方向的步长序列
    x_coords = np.cumsum(directions[:, 0])
    y_coords = np.cumsum(directions[:, 1])
    # 3. 使用 cumsum() 计算累积和得到轨迹
    return (x_coords, y_coords)


def plot_single_walk(path):
    """绘制单个随机行走轨迹
    
    参数:
        path (tuple): 包含x和y坐标序列的元组
    """
    # TODO: 实现单个轨迹的绘制
    # 提示：
    # 1. 使用 plt.plot 绘制轨迹线
    x_coords, y_coords = path
    
    plt.figure(figsize=(8, 8))
    plt.plot(x_coords, y_coords, label='随机行走轨迹')
    # 2. 使用 plt.scatter 标记起点和终点
    plt.scatter([0], [0], color='green', label='起点', zorder=2)
    plt.scatter([x_coords[-1]], [y_coords[-1]], color='red', label='终点', zorder=2)
    # 3. 设置坐标轴比例相等
    plt.title('二维随机行走轨迹（1000步）')
    plt.xlabel('x坐标')
    plt.ylabel('y坐标')
    plt.axis('equal')
    # 4. 添加图例
    plt.legend()
    plt.grid(True)

    plt.savefig('results/single_walk.png', dpi=300)
    plt.show()

def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机行走轨迹"""
    # TODO: 实现多个轨迹的绘制
    # 提示：
    # 1. 创建2x2的子图布局
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    # 2. 对每个子图重复以下步骤：
    #    - 生成随机行走轨迹
    fig.suptitle('四个不同的二维随机行走轨迹（1000步）')
    for i in range(2):
        for j in range(2):
            x_coords, y_coords = random_walk_2d(1000)
    #    - 绘制轨迹线
     axs[i, j].plot(x_coords, y_coords)
            axs[i, j].scatter([0], [0], color='green', zorder=2)
            axs[i, j].scatter([x_coords[-1]], [y_coords[-1]], color='red', zorder=2)
            axs[i, j].set_title(f'轨迹 {i*2+j+1}')
            axs[i, j].axis('equal')
            axs[i, j].grid(True)
    plt.tight_layout()
    plt.savefig('results/multiple_walks.png', dpi=300)
    plt.show()
   
    

if __name__ == "__main__":
    # TODO: 完成主程序逻辑
    # 1. 生成并绘制单个轨迹
    single_path = random_walk_2d(1000)
    plot_single_walk(single_path)
    # 2. 生成并绘制多个轨迹
    plot_multiple_walks()
