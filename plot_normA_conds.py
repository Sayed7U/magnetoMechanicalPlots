import numpy as np
from NormA import NormA
import os
import plt_options
import matplotlib.pyplot as plt


def main():
    # ------------------------------------------------------------------
    N_s = 45
    layers = 2
    neurons = 16
    N_o = 40
    m = 20
    freq_out = np.linspace(5, 5000, N_o)
    folder = f"4K_20Rows_Ns{N_s}"
    save_folder = f'figures/normA/{folder}'
    save_name = f"{save_folder}/NormA_4K_Conds_l{layers}_n{neurons}_m{m}_Ns{N_s}_No{N_o}.pdf"
    # ------------------------------------------------------------------

    load_name = f"{folder}/FrequencySweepMHIGradXNormA.mat"
    obj = NormA(load_name)
    y = obj.data
    x_label = obj.x_label
    y_label = obj.y_label

    if not os.path.exists(f'{save_folder}'):
        os.makedirs(f'{save_folder}')

    cond_factor_out = np.loadtxt(f'data/normA/{folder}/CondFactorOut.txt', skiprows=1, delimiter=",")
    print(f"{cond_factor_out.shape=}")
    cond_factor_out_4k = cond_factor_out[:, 0]

    y_conds = list(np.split(y[0], len(cond_factor_out_4k), axis=0))
    labels = [f"NN conductivity = {i}" for i in cond_factor_out_4k]

    plt_options.main()
    for i in range(len(y_conds)):
        plt.plot(freq_out, y_conds[i], label=labels[i])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.yscale("log")
    plt.savefig(save_name)
    print(f'Saved figure to {save_name}')
    plt.show()


if __name__ == "__main__":
    main()
