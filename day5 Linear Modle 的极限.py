import numpy as np 
import matplotlib.pyplot as plt 
X = np.random.randn(1000,2)
y = np.zeros(1000,dtype = int)
y[X[:,0]**2 + X[:,1]**2 > 1] = 1
y[X[:,0]**2 - X[:,1]**2 <= 1] = 0
W = np.random.randn(2,2) * 0.01
b = np.zeros(2)
scores = X @ W + b
lr = 0.05
def softmax(scores):
    exp_z = np.exp(scores)
    probs = exp_z / np.sum(np.exp(scores), axis = 1,keepdims = True)
    return probs
num_class = 2
y_onehot = np.zeros((len(y),num_class))
y_onehot[np.arange(len(y)),y] = 1
loss = -np.mean(np.sum(y_onehot * np.log(softmax(scores) + 1e-8),axis = 1))
print("初始LOSS:",loss)
losses = []
for epoch in range(2000):
    scores = X @ W + b
    loss = -np.mean(np.sum(y_onehot * np.log(softmax(scores) + 1e-8),axis = 1))
    losses.append(loss)
    dscores = (softmax(scores) - y_onehot) / len(y)
    dW = X.T @ dscores
    db = np.sum(dscores, axis = 0)
    W = W - lr*dW
    b = b - lr*db
print('训练后loss:',losses[-1])

y_pred = np.argmax(softmax(scores),axis = 1)
acc = np.mean(y_pred == y)
print('accuracy:',acc)

#Loss曲线
plt.plot(losses)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.title("Training Loss")
plt.show()
#分类结果
plt.scatter(X[:,0] , X[:,1], c = y_pred)
plt.title('Predict')
plt.show()



