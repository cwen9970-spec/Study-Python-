import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

t = np.linspace(0,1,200)
A = 1 

#批量生成信号并利用FFT进行标签
X = []
Y = []
for _ in range(100):
    f_low = np.random.uniform(1,5) #低频信号频率
    sig_low = A * np.sin(2 * np.pi * f_low * t) + np.random.randn(len(t)) * 1.5 #低频信号
    #对低频信号做FFT处理
    sig_low_fft = np.fft.fft(sig_low)
    X.append(np.abs(sig_low_fft))
    Y.append(0) #低频信号标签为0
    
    f_high = np.random.uniform(10,20) #高频信号频率
    sig_high = A * np.sin(2 * np.pi * f_high * t) + np.random.randn(len(t)) * 1.5 #高频信号
    #对高频信号做FFT处理
    sig_high_fft = np.fft.fft(sig_high)
    X.append(np.abs(sig_high_fft))
    Y.append(1) #高频信号标签为1
X = np.array(X)
Y = np.array(Y)

#划分训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 42)
model = make_pipeline(StandardScaler(), LogisticRegression())
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
print('TRAINING MODEL...')
acc = accuracy_score(Y_test,Y_pred)
print('Accuracy:',acc)

#加噪声前后信号对比
sig_low_p =sig_low = A * np.sin(2 * np.pi * f_low * t)
sig_low_n = A * np.sin(2 * np.pi * f_low * t) + np.random.randn(len(t)) * 1.5
sig_high_p = A * np.sin(2 * np.pi * f_high * t)
sig_high_n = A * np.sin(2 * np.pi * f_high * t) + np.random.randn(len(t)) * 1.5
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.plot(t,sig_low_p)
plt.title('Low Frequency Signal (Clean)')
plt.subplot(2,2,2)
plt.plot(t,sig_low_n)
plt.title('Low Frequency Signal (Noisy)')
plt.subplot(2,2,3)
plt.plot(t,sig_high_p)
plt.title('High Frequency Signal (Clean)')
plt.subplot(2,2,4)
plt.plot(t,sig_high_n)
plt.title('High Frequency Signal (Noisy)')
plt.tight_layout()
plt.show()
#FFT频谱对比
sig_low_p_fft = np.fft.fft(sig_low_p)
sig_low_n_fft = np.fft.fft(sig_low_n)
sig_high_p_fft = np.fft.fft(sig_high_p)
sig_high_n_fft = np.fft.fft(sig_high_n)
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.plot(np.abs(sig_low_p_fft))
plt.title('Low Frequency Signal FFT (Clean)')
plt.subplot(2,2,2)
plt.plot(np.abs(sig_low_n_fft))
plt.title('Low Frequency Signal FFT (Noisy)')
plt.subplot(2,2,3)
plt.plot(np.abs(sig_high_p_fft))
plt.title('High Frequency Signal FFT (Clean)')
plt.subplot(2,2,4)
plt.plot(np.abs(sig_high_n_fft))
plt.title('High Frequency Signal FFT (Noisy)')
plt.tight_layout()
plt.show()