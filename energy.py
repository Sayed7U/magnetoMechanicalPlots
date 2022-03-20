from scipy.io import loadmat
import numpy as np


class Energy:
    def __init__(self, load_name):
        self.load_name = load_name
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

        omega = 31415.93

        struct = mat_data['IntegratedFields'][0, 0]
        out4K = np.square(struct['DisplacementNorm4K']) * 2 * rho4K * (omega ** 2)
        out77K = np.square(struct['DisplacementNorm77K']) * 2 * rho77K * (omega ** 2)
        outOVC = np.square(struct['DisplacementNormOVC']) * 2 * rhoOVC * (omega ** 2)
        output = [out4K, out77K, outOVC]
        return output
