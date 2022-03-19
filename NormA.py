from scipy.io import loadmat


class NormA:
    def __init__(self, load_name):
        self.load_name = load_name
        self.data = self.__load()
        self.x_label = 'Frequency (Hz)'
        self.y_label = '$||\mathbf{A}^{AC}_{\epsilon, hp}||$ (Vs$m^-1$)'

    def __load(self):
        mat_data = loadmat(f"data/normA/{self.load_name}")
        print(f'Loaded {self.load_name}')
        struct = mat_data['IntegratedNormA']
        output = [struct[0, 0][i] for i in range(3)]
        return output
