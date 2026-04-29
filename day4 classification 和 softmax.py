import numpy as np 
import matplotlib.pyplot as plt 
np.random.seed(0)
X = np.random.randn(100,2)
y = np.zeros(100 , dtype = int)
y[X[:,0] + X[:,1] > 1] = 1
y[X[:,0] - X[:,1] > 1] = 2
W = np.random.randn(2,3) * 0.01
b = np.zeros(3)
lr = 0.95
scores = X @ W + b
exp_scores = np.exp(scores)
probs = exp_scores/np.sum(exp_scores , axis = 1 , keepdims = True)
num_class = 3
y_onehot = np.zeros((len(y),num_class))
y_onehot[np.arange(len(y)) , y] = 1
loss = -np.mean(np.sum(y_onehot * np.log(probs + 1e-8),axis = 1))
print('loss:',loss)
dscores = (probs - y_onehot) / len(y)
dW = X.T @ dscores
db = np.sum(dscores , axis = 0)
W = W - lr*dW
b = b - lr*db

#训练模型
Losses = []
for epoch in range(200):
    scores = X @ W + b
    exp_scores = np.exp(scores)
    probs = exp_scores/np.sum(exp_scores , axis = 1 , keepdims = True)
    loss = -np.mean(np.sum(y_onehot * np.log(probs + 1e-8),axis = 1))
    Losses.append(loss)
    dscores = (probs - y_onehot) / len(y)
    dW = X.T @ dscores
    db = np.sum(dscores , axis = 0)
    W = W - lr*dW
    b = b - lr*db
print("训练后Loss:",Losses[-1])

#ACCURACY
y_pred = np.argmax(probs,axis = 1)
acc = np.mean(y_pred == y)
print('accuracy:',acc)

#Loss曲线
plt.plot(Losses)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.title("Training Loss")
plt.show()
#分类结果
plt.scatter(X[:,0] , X[:,1], c = y_pred)
plt.title('Predict')
plt.show()

#决策边界（超平面）
x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 200),
    np.linspace(y_min, y_max, 200))
grid = np.c_[xx.ravel(), yy.ravel()]
scores = grid @ W + b
exp_scores = np.exp(scores)
probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
Z = np.argmax(probs, axis=1)
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:,0], X[:,1], c=y, edgecolors='k')
plt.title("Decision Boundary")
plt.show()
