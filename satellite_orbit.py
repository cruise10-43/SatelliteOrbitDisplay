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


def update():
    sats = get_sat_tle_info()
    ts = skyfield.api.load.timescale()
    sat = sats[0]
    print(ts.now())

    x = np.array([])
    y = np.array([])
    z = np.array([])

    minutes = 0
    base_time = datetime.datetime(2023, 2, 19, 12, 0, 0, 000)
    for num in range(100):
        edit_time = ts.tt(base_time.year, base_time.month, base_time.day,
                          base_time.hour, base_time.minute, base_time.second)
        print(sat.at(edit_time).position.km)
        x = np.append(x, [sat.at(edit_time).position.km[0]])
        y = np.append(y, [sat.at(edit_time).position.km[1]])
        z = np.append(z, [sat.at(edit_time).position.km[2]])
        # 5minutes add
        base_time = base_time + datetime.timedelta(hours=5)

    ax.scatter(x, y, z, s=1, c='red')


if __name__ == '__main__':
    print('satellite_orbit')

    # 描画エリアの作成

    anim = FuncAnimation(fig, update())


    # 描画
    plt.show()
