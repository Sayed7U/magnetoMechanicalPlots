import plots
import numpy as np
import os
from power import Power


def main():
    Options = {'POD': 'PODI', 'neural_network': True, 'feed_forward_net': True, 'segmented': False, 'per_mode': True,
               'N_s': 45, 'm': 20,
               'N_o': 499, 'x_axis_logged': False, 'No_segments': 20, 'layers': 1, 'chosen_sample': 'log space',
               'neurons': 1, 'solver': 'adam', 'activation': 'identity', 'ffn_layers': 2, 'ffn_neurons': 16,
               'ffn_solver': 'trainbr',
               'custom_saveload': True, 'save_name': '', 'load_name': '', 'min_grad': 1e-10}

    globals().update(Options)

    choice = f"PODP_Ns{N_s}_CondOVCmarcos"
    Options['load_name'] = f'{choice}/FrequencySweepMHIGradXPowerEnergy'

    freq_out = np.linspace(15, 15 + (Options['N_o'] - 1) * 10, Options['N_o'])
    # freq_out = np.linspace(5, 105, N_o)
    # freq_out = np.linspace(15, 5000, Options['N_o'])
    Options['freqout'] = freq_out

    power = Power(Options)
    y1, _ = power.load()
    plot_options = power.plot_options()
    labels = plot_options['labels']

    xlabel = plot_options['xlabel']
    ylabel = plot_options['ylabel']

    cond_factor_out = np.loadtxt(f'data/powerEnergy/{choice}/CondFactorOut.txt', skiprows=1, delimiter=",")
    print(f"{cond_factor_out.shape}")
    cond_factor_out_OVC = cond_factor_out[:, 2]

    y_conds = list(np.split(y1[0], len(cond_factor_out_OVC), axis=0))
    labels = [f"NN conductivity = {i}" for i in cond_factor_out_OVC]
    save_folder = f'power/{choice}'

    if not os.path.exists(f'figures/{save_folder}'):
        os.makedirs(f'figures/{save_folder}')

    save_name = f'{save_folder}/power_OVC_Conds_Ns{N_s}_No{N_o}_{m}modes_{int(freqout[0])}to{int(freqout[-1])}Hz'
    plots.list_log_plot(freq_out, y_conds, xlabel, ylabel, labels, save_name)


if __name__ == "__main__":
    main()
