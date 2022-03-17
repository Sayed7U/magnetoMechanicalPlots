import funcs
import plots
import os
import numpy as np
from scipy.io import loadmat
from normA import NormA

def main():
    Options = {'POD': 'PODI','neural_network': True, 'feed_forward_net': True, 'segmented': False, 'per_mode': True, 'N_s': 45, 'm': 20,
            'N_o': 40, 'x_axis_logged': False, 'No_segments': 20, 'layers': 1, 'chosen_sample': 'log space',
            'neurons': 1, 'solver': 'adam', 'activation': 'identity', 'ffn_layers': 2, 'ffn_neurons': 16, 'ffn_solver': 'trainbr',
               'custom_saveload':True,'save_name': '', 'load_name': '', 'min_grad': 1e-10}
    
    freq_out = np.linspace(15, 5000, Options['N_o'])
    Options['freqout'] = freq_out

    globals().update(Options)

    # cond_factor_choice = "4K_3Rows"
    # cond_factor_choice = "4K_10Rows_rand"
    cond_factor_choice = f"4K_20Rows_Ns{N_s}"
    cond_factor_choice_approxD = f"4K_20Rows_Ns{N_s}_approxD"

    APPROX_D = False


    Options['load_name'] = f'{cond_factor_choice}/FrequencySweepMHIGradXNormA'
    
    
    normA = NormA(Options)
    y1, save_name_1 = normA.load()
    plot_options = normA.plot_options()
    xlabel = plot_options['xlabel']
    ylabel = plot_options['ylabel']
    print(f"{y1[0].shape=}")

    cond_factor_out = np.loadtxt(f'data/normA/{cond_factor_choice}/CondFactorOut.txt', skiprows=1, delimiter=",")
    print(f"{cond_factor_out.shape}")
    cond_factor_out_4k = cond_factor_out[:, 0]

    y_conds = list(np.split(y1[0], len(cond_factor_out_4k), axis=0))
    labels = [f"NN conductivity = {i}" for i in cond_factor_out_4k]
    save_folder = f'normA/{cond_factor_choice}'
    
    if not os.path.exists(f'figures/{save_folder}'):
        os.makedirs(f'figures/{save_folder}')
 
    

    if APPROX_D:
        Options['load_name'] = f'{cond_factor_choice_approxD}/FrequencySweepMHIGradXNormA'
        normA_approxD = NormA(Options)
        y_approxD, _ = normA_approxD.load()
        y_approxDs = list(np.split(y_approxD[0], len(cond_factor_out_4k), axis=0))
        approxD_freqs = np.logspace(np.log10(5),np.log10(5000),N_s)
        save_name = f'{save_folder}/NormA_4K_Conds_{POD}_ffn_{ffn_solver}_l{ffn_layers}_n{ffn_neurons}_Ns{N_s}_No{N_o}_{m}modes_{int(freqout[0])}to{int(freqout[-1])}Hz_approxDcompare'
        labels_approxD = [f"approxD conductivity = {i}" for i in cond_factor_out_4k]
        plots.list_scatter_line_log_y1y2_plot(approxD_freqs,freq_out,y_approxDs,y_conds, xlabel, ylabel, labels_approxD, labels, save_name)
    else:
        save_name = f'{save_folder}/NormA_4K_Conds_{POD}_ffn_{ffn_solver}_l{ffn_layers}_n{ffn_neurons}_Ns{N_s}_No{N_o}_{m}modes_{int(freqout[0])}to{int(freqout[-1])}Hz'
        plots.list_log_plot(freq_out,y_conds, xlabel, ylabel, labels, save_name)
    

if __name__ == '__main__':
    main()
