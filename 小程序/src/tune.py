from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC

# 加载数据
X, y = load_digits(return_X_y=True)
X = X / 16.0
# 划分数据（必须和之前一致）
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# 定义参数搜索范围
param_grid = {'C': [0.1, 1, 10],'gamma': [0.01, 0.05, 0.1, 'scale']}
# 创建模型
svc = SVC(kernel='rbf')
# 网格搜索
grid = GridSearchCV(
    svc,
    param_grid,
    cv=5,           
    scoring='accuracy')
print("开始自动调参...")
# 开始训练 + 调参
grid.fit(X_train, y_train)
# 输出结果
print("最佳参数：", grid.best_params_)
print("最佳交叉验证得分：", grid.best_score_)