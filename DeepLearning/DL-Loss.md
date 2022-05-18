## DL-Loss

CE		  分类错误率

> $$\frac{错误数}{总数}$$

SSE		和方差（误差的平方）

> $$\sum_{i=1}^{m}{w_i(y_i-\hat y_i)^2}$$

MSE	   均方误差（误差平方的均值）

> $$\frac1n\sum_{i=1}^{m}{w_i(y_i-\hat y_i)^2}$$ 

RMSE	回归系统拟合标准差

> $$\sqrt{MSE}$$

Cross Entropy 交叉熵损失函数

> $$L_{Binary}=\frac{-1}N\sum_i{L_i}=\frac1N\sum_i{[y_i\cdot{log(p_i)+(1-y_i)\cdot{log(1-p_i)]}}}$$
>
> $$L=\frac{-1}N\sum_i{L_i}=\frac1N\sum_i{\sum_{c=1}^{M}{y_{ic}log(p_{ic})}}$$
>
> 其中：N为样本数量，M为类别数量，y为真实值(0/1)，p为预测值