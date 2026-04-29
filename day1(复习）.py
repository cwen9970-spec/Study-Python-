import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
score=np.random.randint(50,101,size=(100,3))
print(np.shape(score))
print("每科目平均分",np.mean(score,axis=0))
total_score=np.sum(score,axis=1)
print("分数最高者",np.argmax(total_score))
print('数学最高的同学：',np.argmax(score[:,0]))

#2
math_90 = score[score[:,0] >= 90]
print("数学高于90的学生",math_90)
total_260 = score[np.sum(score,axis=1) >  260]
print("总分高于260的学生",total_260)

math_physics_80 = score[(score[:,0] >=80) & (score[:,2] >= 80)]
print("物理数学都高于80的学生",math_physics_80)

English_or_Physics_60 = score[(score[:,1] <= 60) | (score[:,2] <= 60)]
print("英语或物理低于60的学生",English_or_Physics_60)

#3
total_score=np.sum(score,axis=1)
idx=np.argsort(-total_score)
print("成绩排名",total_score[idx])

#4
plt.figure(figsize=(8,8))
x=score[:,0]
y=score[:,2]
plt.scatter(x,y)
plt.xlabel('math')
plt.ylabel("physics")
plt.tight_layout()
plt.show()

#5

y_pred = 0.8 * x + 10
error = np.mean(y - y_pred)
sqr_error = np.mean((y - y_pred)**2)
print("标准误差",error)
print("平方误差",sqr_error)
