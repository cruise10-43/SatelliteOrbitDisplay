import skyfield.api


def get_sat_tle_info():
    sat_list = skyfield.api.load.tle_file('https://celestrak.org/NORAD/elements/gnss.txt', reload=1)
    print(len(sat_list))
    return sat_list


if __name__ == '__main__':
    print('satellite_orbit')
    sats = get_sat_tle_info()
    ts = skyfield.api.load.timescale()
    sat = sats[0]
    print(ts.now().utc_datetime())
    print(sat.at(ts.now()))
