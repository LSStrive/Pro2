import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()
# print(iris.data.shape)
# X = iris.data[:]
# X = iris.data[:,2:]

FlameData = np.loadtxt('Flame.txt', delimiter=',')
X = FlameData[:, :2]
# print(type(X))
print(X[:5])


# 绘制数据分布图
plt.scatter(X[:, 0], X[:, 1], c = 'red', marker='o', label='see')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2) # legend图例，loc:图例位置 2 代表upper left， title：图例标题
plt.show()

# 聚类
estimator = KMeans(n_clusters=2) # 构造聚类器
estimator.fit(X) # 对X进行聚类
label_pred = estimator.labels_ # 获取聚类标签
print('type(label_pred):', type(label_pred))
# 运行多次该程序，只是标签不一致，还是相同的簇

# 绘制k-means结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
# x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c = "red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c = "green", marker='*', label='label1')
# plt.scatter(x2[:, 0], x2[:, 1], c = "blue", marker='+', label='label2')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()

# 看到上面的聚类效果其实并不理想，这样我们选择鸢尾花的最后两个特征来看下效果：
# 首先修改数据为：
# X = iris.data[:,2:] ##表示我们只取特征空间中的后两个维度