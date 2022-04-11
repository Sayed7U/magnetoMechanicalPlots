import plt_options
import numpy as np
import matplotlib.pyplot as plt


def main():
    N_s = 180
    del_f1 = 10
    del_f2 = 50

    s1 = np.arange(10, 1000, del_f1)
    s2 = np.arange(1000, 5000+1, del_f2)
    piece_wise_linear = np.concatenate([s1, s2])

    log_spacing = np.logspace(np.log10(5), np.log10(5000), N_s)

    number = np.arange(1, 180+1, 1)

    plt_options.main()
    plt.plot(number, piece_wise_linear, 'x', label='Piece-wise Linear')
    plt.plot(number, log_spacing, 'x', label='Log-spacing')
    plt.xticks(np.arange(0, 180+1, 20))
    plt.xlabel('Index')
    plt.ylabel('Frequency (Hz)')
    plt.legend()
    plt.savefig('figures/linear_vs_log_freqs.pdf')
    plt.show()


if __name__ == '__main__':
    main()
