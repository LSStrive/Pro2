# 该例子与demo1特别相似
from sklearn import datasets
from sklearn.linear_model import LinearRegression # 机器学习一个回归方法
import matplotlib.pyplot as plt

#使用以后的数据集进行线性回归（这里是波士顿房价数据）
loaded_data=datasets.load_boston()
data_X=loaded_data.data
data_y=loaded_data.target

model=LinearRegression()
model.fit(data_X,data_y)

print(model.predict(data_X[:4,:])) # 预测值
print(data_y[:4]) # 真实值

#使用生成线性回归的数据集，最后的数据集结果用散点图表示
X,y=datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=1)   #n_samples表示样本数目，n_features特征的数目  n_tragets y输出的维数  noise噪音
plt.scatter(X,y)
plt.show()