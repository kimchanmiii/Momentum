import tensorflow as tf
import numpy as np
import Momentum.Optimization as Optimization
from Momentum.drawing import *


class Model(object):
    def __init__(self, a, b, init):
        self.x = tf.Variable(float(init[0]))
        self.y = tf.Variable(float(init[1]))
        self.a = tf.Variable(float(a))
        self.b = tf.Variable(float(b))

    def __call__(self):
        return (self.a - self.x) ** 2 + self.b * (self.y - self.x ** 2) ** 2

def test_uniitest(optimizer, f, init):
    Opt = Optimization.Optimization(optimizer=optimizer, funct=f)
    result, iter_X, iter_Y, iter_cnt = Opt.optimize(init)
    print(type(optimizer).__name__, " ==> ", f"position(x,y): {result}, z: {iter_Y[-1]:.3f}, iteration: {iter_cnt}")
    show(f, iter_X, iter_Y, iter_cnt)


