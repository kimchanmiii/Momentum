#실행할 메인 코드

import Momentum.Optimization as Optimization
from Momentum.Momentum import *
from Momentum.rosenbrock import *
from Momentum.unittest import *

#시작점
init = [1.75, 1.75]

test_uniitest(Momentum(), Rosenbrock(), init)

