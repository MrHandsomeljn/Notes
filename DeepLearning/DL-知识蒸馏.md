## DL-知识蒸馏

- 轻量化网络的技术路线：
  - 大模型压缩为小模型
    - 路线：
      - ★知识蒸馏
      - 权值精度压缩
      - 剪枝
        - 权重剪枝
        - 通道剪枝
  - 直接训练轻量化网络
  - 算法优化加速卷积运算
  - 硬件开发板部署
- 形象表述：Teacher Model -Distill->Student Model
- 场景：模型压缩；防止过拟合；无监督；少样本/零样本学习

- 
  - Response-Based Knowledge（预测结果作为Loss）
  - Feature-Based Knowledge（feature map计算Loss）
  - Relation-Based Knowledge（注意力图等计算Loss）
  - 在线蒸馏、离线蒸馏、自蒸馏、联邦蒸馏



- Soft Label

  - 蒸馏温度T：越大Soft Label更Soft（$$z_i\rightarrow q_i$$）
    - $$q_i=\frac{exp({z_i}/T)}{\sum_j{exp(z_/T)}}$$

- > $$input\rightarrow Teacher Model\rightarrow Soft Targets(ST)$$
  >
  > $$input\rightarrow Student Model\rightarrow SoftPredections(SP)$$
  >
  > **CE<A,B>: 交叉熵损失
  >
  > **GT: Ground Truth with Hard Label
  >
  > $$\begin{cases}L_{Distillation}=CE<SP,ST>\\L_{Student}=CE<SP,GT>\\Loss=\alpha L_{Distillation}+\beta L_{Student}\end{cases}$$

  