import numpy as np
from normA import NormA
import os
import plt_options
import matplotlib.pyplot as plt


def main():
    # ------------------------------------------------------------------
    N_o = 500
    rows = 1
    # freq_out = np.linspace(5, 5000, N_o)
    del_freq_out = 10
    freq_out = np.linspace(10, 10 + (N_o - 1) * del_freq_out, N_o)

    folder = f"freq/Ns45_logspaced_marcos2_lagrange"
    save_folder = f'figures/normA/{folder}'
    save_dir = f"{save_folder}/normA_againstDefaultFullOrder.pdf"
    # save_dir = f"{save_folder}/normA_4K_conds_l{layers}_n{neurons}_m{m}_Ns{N_s}_No{N_o}.pdf"
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

    # y_conds = list(np.split(y, cond_factor_out.shape[0], axis=0))
    shields = ["4K", "77K", "OVC"]
    labels = [f"{j} conductivity = {i}" for i, j in zip(cond_factor_out, shields)]
    labels_def = [f"{i} conductivity = 1.0" for i in shields]

    load_name_def = f"freq/FullOrder/default/FrequencySweepMHIGradXNormA.mat"
    obj_def = NormA(load_name_def)
    y_def = obj_def.data

    plt_options.main()
    for i in range(len(y_def)):
        plt.plot(freq_out, y_def[i], label=labels_def[i])
    for i in range(len(y)):
        plt.plot(freq_out, y[i], label=labels[i])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.yscale("log")
    plt.savefig(save_dir)
    print(f'Saved figure to {save_dir}')
    plt.show()


if __name__ == "__main__":
    main()
