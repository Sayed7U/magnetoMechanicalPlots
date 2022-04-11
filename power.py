from scipy.io import loadmat
from dataclasses import dataclass, field
import numpy as np


@dataclass()
class Power:
    load_name: str
    x_label = 'Frequency (Hz)'
    y_label = '$P^0(W)$'
    out4K: np.array = field(init=False)
    out77K: np.array = field(init=False)
    outOVC: np.array = field(init=False)

    def load(self):
        load_dir = f"data/powerEnergy/{self.load_name}"
        mat_data = loadmat(load_dir)
        print(f'Loaded {load_dir}')

        struct = mat_data['IntegratedFields'][0, 0]
        self.out4K = struct['OutPower4K'] * 4
        self.out77K = struct['OutPower77K'] * 4
        self.outOVC = struct['OutPowerOVC'] * 4
        output = [self.out4K, self.out77K, self.outOVC]
        return output
