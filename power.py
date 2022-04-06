from scipy.io import loadmat
from dataclasses import dataclass


@dataclass(frozen=True)
class Power:
    load_name: str
    x_label = 'Frequency (Hz)'
    y_label = '$P^0(\omega)$'

    def load(self):
        load_dir = f"data/powerEnergy/{self.load_name}"
        mat_data = loadmat(load_dir)
        print(f'Loaded {load_dir}')

        struct = mat_data['IntegratedFields'][0, 0]
        out4K = struct['OutPower4K'] * 4
        out77K = struct['OutPower77K'] * 4
        outOVC = struct['OutPowerOVC'] * 4
        output = [out4K, out77K, outOVC]
        return output
