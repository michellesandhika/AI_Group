import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeRegressor
from mlxtend.plotting import plot_decision_regions
from matplotlib import pylab as plt
""" 
Group member: 
Michelle Karen Natasya Putri SANDHIKA 18078659d
Randall NICHOLAS 18079343D
Nicholas Matthew KURNIADI 18079267D

"""
## 1 - 3
np.random.seed(42)
m = 200
X = np.random.rand(m, 1)

y = 4 * (X - 0.5) ** 2
Y = y + np.random.randn(m, 1) / 10

plt.scatter(X,Y)
plt.show()

tree_clf = DecisionTreeRegressor(max_depth=2)
tree_clf.fit(X,Y)
export_graphviz(
        tree_clf,
        out_file="artifical_data.dot",
        rounded=True,
        filled=True
    )

## 4
newx = np.linspace(0,1,m)
newX = newx.reshape(m,1)
newy = 4 * (newX - 0.5) ** 2
newY = newy + np.random.randn(m, 1) / 10

plt.scatter(newX,newY)
plt.show()

tree_clf.fit(newX,newY)
export_graphviz(
        tree_clf,
        out_file="artifical_data_2.dot",
        rounded=True,
        filled=True
    )

## 5
newtree_clf = DecisionTreeRegressor(max_depth=3)


from mlxtend.plotting import plot_decision_regions
from matplotlib import pylab as plt
fig, ax = plt.subplots(figsize=(7, 7))
plot_decision_regions(newX, newY, clf=newtree_clf)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()




fig, ax = plt.subplots(figsize=(7, 7))
plot_decision_regions(newx, Y.astype(np.integer), clf=tree_clf)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
