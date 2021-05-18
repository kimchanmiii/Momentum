class Rosenbrock:
    def __init__(self, a=1, b=100):
        self.a = a
        self.b = b
        self.dim = 2
    def get_value(self, X):
        return (self.a-X[0])**2 + self.b*(X[1]-X[0]**2)**2

    def get_diff_value(self, X):
        x_diff_value = 2*X[0] - self.a*2 - 4 * self.b * (X[1] - X[0] ** 2) * X[0]
        y_diff_value = self.b*(2*X[1] - 2*X[0]**2)
        return [x_diff_value, y_diff_value]


