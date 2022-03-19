import matplotlib.pyplot as plt


def main():
    # plot line colours, 10 colors all together
    CB91_Blue = '#2CBDFE'
    CB91_Green = '#47DBCD'
    CB91_Pink = '#F3A0F2'
    CB91_Purple = '#9D2EC5'
    CB91_Violet = '#661D98'
    CB91_Amber = '#F5B14C'
    CB91_Red = '#EA1200'
    CB91_Navy = '#1F618D'
    CB91_Grey = '#797D7f'
    CB91_Black = '#17202A'

    color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,
                  CB91_Purple, CB91_Violet, CB91_Red, CB91_Navy, CB91_Grey, CB91_Black]

    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['axes.labelsize'] = 16
    plt.rcParams['axes.titlesize'] = 16
