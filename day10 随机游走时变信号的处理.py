import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

np.random.seed(0)
A = 1
fs = 1000
t = np.linspace(0,1,1000)
dt = 1 / fs

f_low = np.zeros(len(t))
f_low[0] = 20
for i in range(1,len(t)):
    f_low[i] = f_low[i - 1] + np.random.randn() * 5
sig_low = A * np.sin(2 * np.pi * np.cumsum(f_low) * dt)
sig_low_fft = np.fft.fft(sig_low)

f_high = np.zeros(len(t))
f_high[0] = 80
for i in range(1,len(t)):
    f_high[i] = f_high[i - 1] + np.random.randn() * 5
sig_high = A * np.sin(2 * np.pi * np.cumsum(f_high) * dt )
sig_high_fft = np.fft.fft(sig_high)

plt.subplot(2,2,1)
plt.plot(t , sig_low)
plt.subplot(2,2,2)
plt.plot(sig_low_fft)
plt.title('low frequency signal with FFT')
plt.subplot(2,2,3)
plt.plot(t , sig_high)
plt.subplot(2,2,4)
plt.plot(sig_high_fft)
plt.title('high frequency signal with FFT')
plt.show()

#spectrogram
plt.figure(figsize = (12,6))
plt.subplot(2,1,1)
plt.specgram(sig_low, NFFT = 128, Fs = fs, noverlap = 64)
plt.title('Spectrogram of Low Frequency Signal')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar(label = 'Intensity')
plt.subplot(2,1,2)
plt.specgram(sig_high, NFFT = 128, Fs = fs, noverlap = 64)
plt.title('Spectrogram of High Frequency Signal')   
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar(label = 'Intensity')
plt.tight_layout()
plt.show()