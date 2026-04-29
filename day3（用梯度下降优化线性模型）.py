import numpy as np 
import matplotlib.pyplot as plt 
np.random.seed(0)
#两个特征：Learning time and sleep time
X = np.random.rand(100,2)*10
y = 3*X[:,0]+2*X[:,1]+5+np.random.randn(100)
X_std = ( X - np.mean(X,axis = 0) ) / np.std(X,axis = 0)

#引入线性模型
w = np.array([0.0,0.0])
b = 0
lr = 0.01
y_pred = X_std @ w + b
error = y_pred - y
mse = np.mean((error)**2)
print("初始MSE",mse)
Loss = []
for epoch in range(1000):
    y_pred = X_std @ w + b
    error = y_pred - y
    dw = 2 * np.mean(X_std * (error).reshape(-1,1),axis = 0)
    db = 2 * np.mean(error)
    w = w - lr * dw
    b = b - lr * db
    y_pred = X_std @ w + b
    error = y_pred - y
    mse_new = np.mean(error**2)
    Loss.append(mse_new)
print('新MSE：',Loss[-1])
print('w:',w)
print('b',b)

#可视化
plt.plot(Loss)
plt.xlabel('epoch')
plt.ylabel('mse')
plt.title('Training Surface')
plt.show()

#用训练后的数据预测
y_pred_final = X_std @ w + b
plt.scatter(X[:, 0], y, label="True", s=15)
plt.scatter(X[:, 0], y_pred_final, label="Pred", s=15)
plt.xlabel("Feature 1")
plt.ylabel("y")
plt.legend()
plt.title("Fit Check")
plt.show()


#还原数据
# 已有：w, b, 以及 X 的 mean/std
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

# 还原到原始特征下的参数
w_orig = w / std
b_orig = b - np.sum(w * mean / std)
print("w_std:", w)
print("b_std:", b)
print("w_orig:", w_orig)
print("b_orig:", b_orig)


#封装成函数
def Train_linear (X,y,epoch=100,lr=0.01) :
    w = np.zeros(X.shape[1])
    b = 0
    lr = 0.01
    Losses = []
    for epoch in range(1000):
        y_pred = X_std @ w + b
        error = y_pred - y
        dw = 2 * np.mean(X_std * (error).reshape(-1,1),axis = 0)
        db = 2 * np.mean(error)
        w = w - lr * dw
        b = b - lr * db
        y_pred = X_std @ w + b
        error = y_pred - y
        mse_new = np.mean(error**2)
        Losses.append(mse_new)
    return w,b,Losses