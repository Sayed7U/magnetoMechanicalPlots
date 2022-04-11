import numpy as np
from power import Power
import os
import matplotlib.pyplot as plt
import plt_options


def main():
    # ------------------------------------------------------------------
    N_o = 499
    q = 3
    p = 3
    # freq_out = np.linspace(5, 5000, N_o)
    POD = "PODI"
    plot_shield = "4K"
    del_freq_out = 10
    freq_out = np.linspace(15, 15 + (N_o - 1) * del_freq_out, N_o)
    folder = f"{POD}_q{q}_p{p}"
    save_folder = f'figures/powerEnergy/{folder}'
    save_dir = f"{save_folder}/power_{POD}_shield{plot_shield}_No{N_o}_againstFullOrder.pdf"
    # ------------------------------------------------------------------

    load_name23 = f"{folder}/Ns23/FrequencySweepMHIGradXPowerEnergy.mat"
    load_name45 = f"{folder}/Ns45/FrequencySweepMHIGradXPowerEnergy.mat"
    load_name90 = f"{folder}/Ns90/FrequencySweepMHIGradXPowerEnergy.mat"
    load_name180 = f"{folder}/Ns180/FrequencySweepMHIGradXPowerEnergy.mat"

    powers = [Power(load_name23), Power(load_name45), Power(load_name90), Power(load_name180)]
    [item.load() for item in powers]

    x_label = Power.x_label
    y_label = Power.y_label

    if not os.path.exists(f'{save_folder}'):
        os.makedirs(f'{save_folder}')

    load_name_full_order = f"FullOrder_q{q}_p{p}/No{len(freq_out)}/FrequencySweepMHIGradXPowerEnergy.mat"
    power_full_order = Power(load_name_full_order)
    power_full_order.load()

    labels = ["$N_s = 23$", "$N_s = 45$", "$N_s = 90$", "$N_s = 180$"]

    plt_options.main()
    # freq_out_full = np.linspace(10, 10 + (N_o - 1) * del_freq_out, 500)
    plt.plot(freq_out, getattr(power_full_order, f'out{plot_shield}'), label="Full Order")
    for i in range(4):
        plt.plot(freq_out, getattr(powers[i], f'out{plot_shield}'), label=labels[i])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.yscale("log")
    plt.savefig(save_dir)
    print(f'Saved figure to {save_dir}')
    plt.show()


if __name__ == "__main__":
    main()
