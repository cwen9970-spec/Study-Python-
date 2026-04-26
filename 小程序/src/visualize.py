from pathlib import Path
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import joblib
import matplotlib.pyplot as plt

# 加载数据
X, y = load_digits(return_X_y=True)
X = X / 16.0
# 划分数据
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# 加载模型
base_dir = Path(__file__).resolve().parent.parent
results_dir = base_dir / "results"
model = joblib.load(results_dir / "model.pkl")
# 预测
y_pred = model.predict(X_test)
# 计算混淆矩阵
cm = confusion_matrix(y_test, y_pred)
# 画图
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
plt.figure(figsize=(8, 8))
disp.plot(cmap='Blues', values_format='d')
plt.title("Confusion Matrix")
# 保存图片
plt.savefig(results_dir / "confusion_matrix.png")
# 显示
plt.show()