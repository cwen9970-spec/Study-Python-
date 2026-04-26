#train
from pathlib import Path
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import GridSearchCV

#加载手写数字的数据集合
X, y = load_digits(return_X_y=True)
#归一化，让像素值处于更合适的范围
X = X / 16.0
#划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print("Training model...")
#定义一个模型
model = SVC(kernel="rbf",C=10,gamma=0.1)
model.fit(X_train, y_train)
#预测
y_pred = model.predict(X_test)
#计算准确率
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.4f}")
# 用脚本文件自己的位置来找 results 文件夹
base_dir = Path(__file__).resolve().parent.parent
results_dir = base_dir / "results"
results_dir.mkdir(exist_ok=True)
#保存模型
joblib.dump(model, results_dir / "model.pkl")
#记录准确率
with open(results_dir / "accuracy.txt", "w", encoding="utf-8") as f:
    f.write(str(acc))
print("Done.")

