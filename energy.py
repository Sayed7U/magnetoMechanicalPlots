from scipy.io import loadmat
import numpy as np


class Energy:
    __slots__ = ('load_name', 'freq_out', 'data', 'x_label', 'y_label')

    def __init__(self, load_name, freq_out):
        self.load_name = load_name
        self.freq_out = freq_out
        self.data = self.__load()
        self.x_label = 'Frequency (Hz)'
        self.y_label = 'Kinetic energy (J)'

    def __load(self):
        load_dir = f"data/powerEnergy/{self.load_name}"
        mat_data = loadmat(load_dir)
        print(f'Loaded {load_dir}')

        # density
        rho4K = 2710
        rho77K = 2698
        rhoOVC = 7900

        omega = 2 * np.pi * self.freq_out

        struct = mat_data['IntegratedFields'][0, 0]
        out4K = 2 * rho4K * np.multiply(np.square(struct['DisplacementNorm4K'].reshape(-1)), np.square(omega))
        out77K = 2 * rho77K * np.multiply(np.square(struct['DisplacementNorm77K'].reshape(-1)), np.square(omega))
        outOVC = 2 * rhoOVC * np.multiply(np.square(struct['DisplacementNormOVC'].reshape(-1)), np.square(omega))

        output = [out4K, out77K, outOVC]
        return output
