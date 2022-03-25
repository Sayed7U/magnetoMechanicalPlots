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
    # freq_out = np.linspace(5, 5000, N_o)

    del_freq_out = 10
    freq_out = np.linspace(10, 10 + (N_o-1)*del_freq_out, N_o)
    folder = f"PODI_freq_Ns{N_s}_logspace_l{layers}_n{neurons}"
    save_folder = f'figures/powerEnergy/{folder}'
    save_dir = f"{save_folder}/power_NN_l{layers}_n{neurons}_Ns{N_s}_No{N_o}_logspace_againstFullOrder.pdf"
    # ------------------------------------------------------------------

    load_name = f"{folder}/FrequencySweepMHIGradXPowerEnergy.mat"
    obj = Power(load_name)
    y = obj.data
    x_label = obj.x_label
    y_label = obj.y_label

    if not os.path.exists(f'{save_folder}'):
        os.makedirs(f'{save_folder}')

    q = 3
    p = 3
    load_name_full_order = f"FullOrder_q{q}_p{p}/FrequencySweepMHIGradXPowerEnergy.mat"
    obj_full = Power(load_name_full_order)
    y_full = obj_full.data

    labels = ["NN PODI: 4K", "NN PODI: 77K", "NN PODI: OVC"]
    labels_full = ["Full order: 4K", "Full order: 77K", "Full order: OVC"]
    plt_options.main()
    for i in range(len(y_full)):
        plt.plot(freq_out, y_full[i], label=labels_full[i])
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
