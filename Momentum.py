from . import methods

class Momentum:
    def __init__(self, lr=0.0013, momentum=0.1):
        self.lr = lr
        self.momentum = momentum
        self.gradient_moment = 0

    def update(self, x, gradient):
        # 기울기 구하기
        self.gradient_moment = methods.__moment__(self.momentum, self.gradient_moment, gradient)
        # 새로운 좌표 구하기
        new_x = methods.__update__(x, self.lr, self.gradient_moment)
        return new_x

