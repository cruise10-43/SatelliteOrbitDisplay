import skyfield.api
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np
import datetime

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


def get_sat_tle_info():
    sat_list = skyfield.api.load.tle_file('https://celestrak.org/NORAD/elements/gnss.txt', reload=1)
    print(len(sat_list))
    return sat_list


def update(impressions):
    param_year = 2023
    param_month = 2
    param_day = 23
    param_hour = 0
    param_minute = 0
    param_second = 0
    # 前のフレームの描画をクリアする。
    ax.cla()
    x = np.array([])
    y = np.array([])
    z = np.array([])
    for i in range(impressions):
        edit_time = ts.tt(param_year, param_month, param_day,
                          param_hour, param_minute, param_second)
        x = np.append(x, [sat.at(edit_time).position.km[0]])
        y = np.append(y, [sat.at(edit_time).position.km[1]])
        z = np.append(z, [sat.at(edit_time).position.km[2]])
        param_hour = param_hour + 5

    ax.scatter(x, y, z, s=3, c='blue')


if __name__ == '__main__':
    print('satellite_orbit')

    sats = get_sat_tle_info()
    ts = skyfield.api.load.timescale()
    sat = sats[0]
    base_time = datetime.datetime(2023, 2, 19, 12, 0, 0, 000)
    impressions = 50

    '''
    FuncAnimation() 引数
    fig: Figureオブジェクト
    func: 各フレームを生成する関数
    frames: 各フレームのデータ
        int: 現在のフレーム数がfuncに渡される。
        iterable, generator: 各要素がfuncに渡される。
    init_func: 各フレームを初期化する関数
    fargs: funcに渡す引数
    save_count: キャッシュするフレーム数
    interval: 各フレームのインターバルをmsで指定する。デフォルトは200ms
    repeat_delay: リピートする場合、リピートする前の遅延をmsで指定する。デフォルトはNone
    repeat: リピートするかどうか。デフォルトはTrue
    bilit: blittingを使用して描画を高速化するかどうか。デフォルトはFalse
    animation.FuncAnimation(fig, func, frames=None, init_func=None, fargs=None, save_count=None, **kwargs)
    '''

    # 描画エリアの作成

    anim = FuncAnimation(fig, update, frames=impressions, init_func=None, fargs=None, save_count=None, interval=1)

    anim.save("orbit_test2.gif", writer="imagemagick")
    # 描画
    #plt.show()
    plt.close()
