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
tree_reg2 = DecisionTreeRegressor(max_depth=3)
tree_reg3 = DecisionTreeRegressor(max_depth=4)
tree_reg2.fit(X, Y)
tree_reg3.fit(X, Y)


def regression_prediction(tree, x, y, axis=[0, 1, -0.2, 1]):
   
    
    y_pred = tree.predict(newX)
    plt.axis(axis)
    plt.xlabel('x', fontsize = 18)
    plt.ylabel('y', fontsize = 18)
    plt.plot(X, y, 'b.')
    plt.plot(newX, y_pred, 'r.-', linewidth = 2)


regression_prediction(tree_reg2, X, Y)
plt.title('max_depth={}'.format(tree_reg2.max_depth), fontsize=14)
plt.show()


regression_prediction(tree_reg3, X, Y)
plt.title('max_depth={}'.format(tree_reg3.max_depth), fontsize=14)
plt.show()
tree_clf.fit(newX,newY)
export_graphviz(
        tree_clf,
        out_file="artifical_data_2.dot",
        rounded=True,
        filled=True
    )


