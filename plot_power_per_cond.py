import numpy as np
from power import Power
import os
import matplotlib.pyplot as plt
import plt_options


def main():
    # ------------------------------------------------------------------
    N_s = 45
    layers = 2
    neurons = 16
    N_o = 500
    m = 20
    freq_out = np.linspace(5, 5000, N_o)
    shield = "4K"
    plot_shield = "4K"
    folder = f"PODP_Ns{N_s}_{shield}_3Rows_marcos"
    save_folder = f'figures/powerEnergy/{folder}'
    save_dir = f"{save_folder}/power_{shield}_conds_PODP_marcos_Ns{N_s}_No{N_o}.pdf"
    # ------------------------------------------------------------------

    load_name = f"{folder}/FrequencySweepMHIGradXPowerEnergy.mat"
    obj = Power(load_name)
    y = obj.data
    x_label = obj.x_label
    y_label = obj.y_label

    if not os.path.exists(f'{save_folder}'):
        os.makedirs(f'{save_folder}')

    cond_factor_out = np.loadtxt(f'data/powerEnergy/{folder}/CondFactorOut.txt', skiprows=1, delimiter=",")
    print(f"{cond_factor_out.shape=}")
    shield_no = {"4K": 0, "77K": 1, "OVC": 2}
    cond_factor_out_shield = cond_factor_out[:, shield_no[shield]]

    y_conds = list(np.split(y[shield_no[plot_shield]], len(cond_factor_out_shield), axis=0))
    labels = [f"PODP conductivity = {i}" for i in cond_factor_out_shield]

    plt_options.main()
    for i in range(len(y_conds)):
        plt.plot(freq_out, y_conds[i], label=labels[i])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.yscale("log")
    plt.savefig(save_dir)
    print(f'Saved figure to {save_dir}')
    plt.show()


if __name__ == "__main__":
    main()