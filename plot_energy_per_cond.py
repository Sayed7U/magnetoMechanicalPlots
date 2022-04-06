import numpy as np
from energy import Energy
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
    # freq_out = np.linspace(5, 5000, N_o)

    del_freq_out = 10
    freq_out = np.linspace(10, 10 + (N_o - 1) * del_freq_out, N_o)
    shield = "OVC"
    plot_shield = "4K"
    folder = f"PODP_Ns{N_s}_{shield}_3Rows_marcos3"
    save_folder = f'figures/powerEnergy/{folder}'
    save_dir = f"{save_folder}/energy_{shield}_conds_PODP_marcos_Ns{N_s}_No{N_o}_plotShield{plot_shield}.pdf"
    # ------------------------------------------------------------------

    cond_factor_out = np.loadtxt(f'data/powerEnergy/{folder}/CondFactorOut.txt', skiprows=1, delimiter=",")
    print(f"{cond_factor_out.shape=}")
    load_name = f"{folder}/FrequencySweepMHIGradXPowerEnergy.mat"
    obj = Energy(load_name, np.tile(freq_out, cond_factor_out.shape[0]))
    y = obj.load()
    x_label = obj.x_label
    y_label = obj.y_label

    if not os.path.exists(f'{save_folder}'):
        os.makedirs(f'{save_folder}')

    shield_no = {"4K": 0, "77K": 1, "OVC": 2}
    cond_factor_out_shield = cond_factor_out[:, shield_no[shield]]

    y_conds = list(np.split(y[shield_no[plot_shield]], len(cond_factor_out_shield), axis=0))
    labels = [f"PODP conductivity = {i}" for i in cond_factor_out_shield]

    obj_full_order = Energy("FullOrder_q3_p3_15Hz/FrequencySweepMHIGradXPowerEnergy.mat", 15)
    y_full_order = obj_full_order.load()
    y_full_order_shield = np.split(y_full_order[shield_no[plot_shield]], len(cond_factor_out_shield), axis=0)
    print(y_full_order_shield)

    plt_options.main()
    for i in range(len(y_conds)):
        plt.plot(freq_out, y_conds[i], label=labels[i])
        plt.plot(15, y_full_order_shield[i], 'o', label=labels[i])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.yscale("log")
    plt.savefig(save_dir)
    print(f'Saved figure to {save_dir}')
    plt.show()


if __name__ == "__main__":
    main()