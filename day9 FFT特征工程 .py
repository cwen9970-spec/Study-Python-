import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

np.random.seed(4)
A = 1
t = np.linspace(0,1,1000)
X = []
Y = []
for _ in range (200):
    fs = 1000
    f_low = np.random.uniform(1,10)
    sig_low = A * np.sin(2 * np.pi * f_low * t )+ np.random.randn(len(t)) * 1
    sig_low_fft = np.fft.fft(sig_low)
    freqs_low = np.fft.fftfreq(len(sig_low), d=1/fs)
    mag_low = np.abs(sig_low_fft)
    mag_low = mag_low[:len(mag_low)//2]
    freqs_half_low = freqs_low[:len(freqs_low)//2]
    peak_sig_low_index = np.argmax(mag_low[1:]) + 1
    main_freq_low = freqs_half_low[peak_sig_low_index]
    X.append([main_freq_low])
    Y.append(0)
    
    f_high = np.random.uniform(50,100)
    sig_high = A * np.sin(2 * np.pi * f_high * t ) + np.random.randn(len(t)) * 1
    sig_high_fft = np.fft.fft(sig_high)
    mag_high = np.abs(sig_high_fft)
    mag_high = mag_high[:len(mag_high)//2]
    freqs_high = np.fft.fftfreq(len(sig_high), d=1/fs)
    freqs_half_high = freqs_high[:len(freqs_high)//2]
    peak_sig_high_index = np.argmax(mag_high[1:]) + 1
    main_freq_high = freqs_half_high[peak_sig_high_index]
    X.append([main_freq_high])
    Y.append(1)
X = np.array(X)
Y = np.array(Y)

plt.subplot(2,2,1)
plt.plot(sig_low)
plt.title('Low Frequency Signal(time domain)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(2,2,2)
plt.plot(sig_low_fft)
plt.title('Low Frequency FFT(frequency domain)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.subplot(2,2,3)
plt.plot(sig_high)
plt.title('High Frequency Signal(time domain)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(2,2,4)
plt.plot(sig_high_fft)
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('High Frequency FFT(frequency domain)')
plt.tight_layout()
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 42)
model = make_pipeline(StandardScaler(), LogisticRegression())
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
print('TRAINING MODEL...')
acc = accuracy_score(Y_test,Y_pred)
print('Accuracy:',acc)




