from pathlib import Path
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import joblib
import matplotlib.pyplot as plt

# 加载数据
X, y = load_digits(return_X_y=True)
X = X / 16.0
# 划分数据
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# 读取模型
base_dir = Path(__file__).resolve().parent.parent
results_dir = base_dir / "results"
model = joblib.load(results_dir / "model.pkl")
# 取图
sample_images = X_test[:100]
sample_labels = y_test[:100]
pred_labels = model.predict(sample_images)
# 创建 figure
plt.figure(figsize=(8, 8))
for i in range(100):
    plt.subplot(10, 10, i + 1)
    plt.imshow(sample_images[i].reshape(8, 8), cmap="gray")
    plt.title(f"T:{sample_labels[i]} P:{pred_labels[i]}")
    plt.axis("off")



plt.tight_layout()
plt.savefig(results_dir / "samples.png", dpi=150)
plt.show()