import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
import plt_options


def main():
    m = 20
    logspace = False
    samples = 23

    if logspace:
        data = loadmat(f'data/SVD/SVDResult_Ns{samples}_m{m}_5to5000Hz_logspace.mat')
    else:
        data = loadmat(f'data/SVD/SVDResult_Ns{samples}_m{m}.mat')

    G = data['G']
    print(f'Snapshots is {samples}')
    print(f'G shape is {G.shape}')

    G_amp = np.absolute(G)
    bins = np.logspace(np.log10(G_amp.min()), np.log10(G_amp.max()), 10)
    if logspace:

        save = f"G_hist/s{samples}_m{m}_logged"
    else:
        save = f"G_hist/s{samples}_m{m}"

    plt_options.main()
    G_amp = G_amp.flatten()
    print(np.mean(G_amp))
    plt.hist(G_amp, bins=bins, alpha=0.7)
    plt.xscale("log")
    plt.xlabel("$|\mathbf{G}_{ij}|$")
    plt.ylabel("Frequency")
    plt.savefig(f"figures/G_hist_{save}.pdf")
    print(f"Saved to figures/G_hist_{save}.pdf")
    plt.show()


if __name__ == '__main__':
    main()
