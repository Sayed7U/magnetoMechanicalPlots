from scipy.io import loadmat


class Power:
    def __init__(self, load_name):
        self.load_name = load_name
        self.data = self.__load()
        self.x_label = 'Frequency (Hz)'
        self.y_label = '$P^0(\omega)$'

    def __load(self):
        load_dir = f"data/powerEnergy/{self.load_name}"
        mat_data = loadmat(load_dir)
        print(f'Loaded {load_dir}')

        struct = mat_data['IntegratedFields'][0, 0]
        out4K = struct['OutPower4K'] * 4
        out77K = struct['OutPower77K'] * 4
        outOVC = struct['OutPowerOVC'] * 4
        output = [out4K, out77K, outOVC]
        return output
