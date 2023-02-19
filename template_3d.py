import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
if __name__ == '__main__':
    #描画エリアの作成
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    #numpyを使用してXYZの値を設定
    x = np.random.rand(1,1)
    y = np.random.rand(1,1)
    z = np.random.rand(1,1)

    #散布図の作成
    ax.scatter(x,y,z,s=1, c='red')

    #描画
    plt.show()