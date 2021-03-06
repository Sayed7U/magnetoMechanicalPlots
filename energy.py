from scipy.io import loadmat
from dataclasses import dataclass, field
import numpy as np


@dataclass()
class Energy:
    load_name: str
    freq_out: np.array
    x_label = 'Frequency (Hz)'
    y_label = 'Kinetic energy (J)'
    out4K: np.array = field(init=False)
    out77K: np.array = field(init=False)
    outOVC: np.array = field(init=False)

    def load(self):
        load_dir = f"data/powerEnergy/{self.load_name}"
        mat_data = loadmat(load_dir)
        print(f'Loaded {load_dir}')

        # density
        rho4K = 2710
        rho77K = 2698
        rhoOVC = 7900

        freq_out = np.reshape(self.freq_out, (-1, 1))
        omega = 2 * np.pi * freq_out

        struct = mat_data['IntegratedFields'][0, 0]
        omega = np.repeat(omega, struct[0].shape[1], axis=1)
        self.out4K = 2 * rho4K * np.multiply(np.square(struct['DisplacementNorm4K']), np.square(omega))
        self.out77K = 2 * rho77K * np.multiply(np.square(struct['DisplacementNorm77K']), np.square(omega))
        self.outOVC = 2 * rhoOVC * np.multiply(np.square(struct['DisplacementNormOVC']), np.square(omega))

        output = [self.out4K, self.out77K, self.outOVC]
        return output
