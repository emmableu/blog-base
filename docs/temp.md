$$

\text{BN}(x) = \frac{x - \mu_{\text{batch}}}{\sqrt{\sigma^2_{\text{batch}} + \epsilon}} \cdot \gamma + \beta

$$




$$

Q_t(c) = \text{当前模型在选择课程 } c \text{ 后的预期学习增益}

$$

$$

Q_{t+1}(c) = \alpha r_t(c) + (1 - \alpha) Q_t(c) \tag{1}

$$

- $$
    
    \mathcal{L}_{PG}(θ) = - \mathbb{E}_{(s,a)}[ \log π_θ(a|s) \cdot \hat{A} ]
    
    $$
- $$
    
    r_t(c) = \mathbb{E}_{x_i ∼ c}[|\hat{A}_{t,i}|] \tag{3}
    
    $$



1. $$
    
    p(c) = \frac{e^{Q_t(c)/\tau}}{\sum_i e^{Q_t(c_i)/\tau}}
    
    $$
