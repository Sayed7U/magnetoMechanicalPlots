from scipy.io import loadmat


class NormA:
    def __init__(self, load_name):
        self.load_name = load_name
        self.data = self.__load()
        self.x_label = 'Frequency (Hz)'
        self.y_label = '$||\mathbf{A}^{AC}_{\epsilon, hp}||$ (Vs$m^-1$)'

    def __load(self):
        load_dir = f"data/normA/{self.load_name}"
        mat_data = loadmat(load_dir)
        print(f'Loaded {load_dir}')
        struct = mat_data['IntegratedNormA']
        output = [struct[0, 0][i] for i in range(3)]
        return output
