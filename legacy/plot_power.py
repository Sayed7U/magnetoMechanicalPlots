import plots
import numpy as np
from power import Power


def main():
    Options = {'POD': 'PODI', 'neural_network': True, 'feed_forward_net': True, 'segmented': False, 'per_mode': True,
               'N_s': 45, 'm': 20,
               'N_o': 499, 'x_axis_logged': False, 'No_segments': 20, 'layers': 1, 'chosen_sample': 'log space',
               'neurons': 1, 'solver': 'adam', 'activation': 'identity', 'ffn_layers': 2, 'ffn_neurons': 16,
               'ffn_solver': 'trainbr',
               'custom_saveload': True, 'save_name': '', 'load_name': '', 'min_grad': 1e-10}

    # Comparisons
    LAGRANGE_PODI = True
    NEURAL_NETWORK = False

    globals().update(Options)
choice = f"PODP_Ns{N_s}_CondOVCmarcos"

    Options['load_name'] = f'{choice}/FrequencySweepMHIGradXPowerEnergy'

    freq_out = np.linspace(15, 15 + (Options['N_o'] - 1) * 10, Options['N_o'])
    # freq_out = np.linspace(5, 105, N_o)
    # freq_out = np.linspace(15, 5000, Options['N_o'])
    Options['freqout'] = freq_out
    if NEURAL_NETWORK:
        power_nn = Power(Options)
        y_nn, save_name_nn = power_nn.load()
        plot_options_nn = power_nn.plot_options()
        labels_nn = plot_options_nn['labels']

        xlabel = plot_options_nn['xlabel']
        ylabel = plot_options_nn['ylabel']

    if LAGRANGE_PODI:
        Options['POD'] = 'PODI'
        Options['neural_network'] = False

        power_lagr = Power(Options)
        y_lagr, save_name_lagr = power_lagr.load()
        plot_options_lagr = power_lagr.plot_options()
        labels_lagr = plot_options_lagr['labels']

        xlabel = plot_options_lagr['xlabel']
        ylabel = plot_options_lagr['ylabel']

    if LAGRANGE_PODI:
        plots.list_log_plot(freq_out, y_lagr, xlabel, ylabel, labels_lagr, save_name_lagr)
    elif NEURAL_NETWORK:
        plots.list_log_plot(freq_out, y_nn, xlabel, ylabel, labels_nn, save_name_nn)

    print(f"Successfully plotted for: \n {Options}")


if __name__ == '__main__':
    main()
