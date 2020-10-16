import numpy as np
""" 
Group member: 
Michelle Karen Natasya Putri SANDHIKA 18078659d
Randall NICHOLAS 18079343D
Nicholas Matthew KURNIADI 18079267D

"""



np.random.seed(42)
m = 200
X = np.random.rand(m, 1)
y = 4 * (X - 0.5) ** 2
Y = y + np.random.randn(m, 1) / 10