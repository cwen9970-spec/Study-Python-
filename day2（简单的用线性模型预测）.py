import numpy as np 
import matplotlib.pyplot as plt 
np.random.seed(0)
#两个特征：Learning time and sleep time
X = np.random.rand(100,2)*10
y = 3*X[:,0]+2*X[:,1]+5+np.random.randn(100)
print("平均学习时间：",np.mean(X[:,0]))
print("平均睡眠时间：",np.mean(X[:,1]))
X_std = X - np.mean(X,axis = 0)
print("标准化后的总学习时间:",np.sum(X_std[:,0]))
print("标准化后的总睡眠时间",np.sum(X_std[:,1]))
print("学习时间最长的学生：",np.argmax(X_std[:,0]))
print("睡眠时间最少的学生：",np.argmin(X_std[:,1]))
lt_8 = X[X[:,0] > 8]
print("学习时间超过八小时的学生：",lt_8)
lt_bigger_st = X[X[:,0] > X[:,1]]
print("学习时间超过睡觉时间的学生：",lt_bigger_st )
y_bigger_mean = y[y > np.mean(y)]
print("预测值中超过平均值的部分：",y_bigger_mean)

#引入线性模型
w = np.array([3,2])
b = 5
y_pred = X@w + b
e = np.mean(y_pred - y)
print("标准误差：",e)
mse = np.mean((y_pred - y)**2)
print("MSE:",mse)

#可视化
plt.scatter(X[:,0],y)
plt.xlabel("study time")
plt.ylabel('score')
plt.show()
