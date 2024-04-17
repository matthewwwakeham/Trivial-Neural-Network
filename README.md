# Trivial Neural Network
An example of a trivial neural network. I explore the concepts of forward propagation, a loss function (MSE), backpropagation, optimization, and convergence.

# Example
Suppose we want to build and train a neural network to draw a line. The network must learn the correct values (see below) of **w** and **b** that align with the given data points.

## Forward Propagation
Consider the line **\hat{y} = wx + b** which can also be understood as a linear regression model.

**w** = weight; the slope of the line  
**b** = bias; adjusting the line vertically  
**x** = input  
**\hat{y}** = predicted output  

## Loss Function - Mean Squared Error
The loss function we will use is **MSE = (1/n) * Σ(i=1 to n) (y_i - ŷ_i)^2**.

**N** = number of data points  
**y_i** = true output for the ith point  
**ŷ_i** = predicted output for the ith point  

Note the following:  
**y_i** are entries in the prediction vector y  
**ŷ_i** are entries in the ground truth label ŷ  

## Backpropagation and Optimization
Adjust **w** and **b** to minimize loss. Calculate the gradient (partial derivative) of the loss function with respect to **w** and **b** and then update the parameters in the opposite direction of the gradient.

**&alpha;** = learning rate  

Equation to calculate the gradient of the loss function with respect to **w** -> **w := w - α * (∂MSE/∂w)**  
Equation to calculate the gradient of the loss function with repsect to **b** -> **b := b - α * (∂MSE/∂b)**

**:=** meaning defined to be  
**(w - &alpha;) and (b - &alpha;)** for adjustments

## Convergence
Through iterative updates the model converges to values of **ww** and **b** that minimize MSE. Thus the model aligns to the predicted **ŷ** values.

# Example Using Mathematics
We will work through the above example with the provided values below.

## Values
Let **w = 0.5** and **b = 1**.  

Let **y = 2x - 1** be a line.  

Let **x = [-1, 0, 1]** and **y = [-3, -1, 1]** be data points. There are **n = 3** sets.  

Let **&alpha; = 0.01**.  

## Forward Pass for a Single Point
Choose **x = 1** and companion **y = 1**.  

Calculate **ŷ = wx + b** -> **ŷ = (0.5)(1) + 1 = 1.5**.  

Calculate **MSE = (1/n) * Σ(i=1 to n) (y_i - ŷ_i)^2**  
Focus on the core point for now: **(y_i - ŷ_i)^2** -> **(1 - 1.5)^2 = (-0.5)^2 = 0.25**.  

## Calculate the Gradients to Adjust w and b
**∂MSE / ∂ŷ = (y_i - ŷ_i)^2** -> invoke the power rule ->  
**∂MSE / ∂ŷ = 2(y_i - ŷ_i)** -> **2(1 - 1.5) = 2(-1) = -1**.

Continue calculation...  

For **w**:  
**∂MSE / ∂ŷ = 1/3 Σ(i=1 to 3) 2(y_i - ŷ_i)**  

Note that **2(y_i - ŷ_i) = 2(1 - 1.5) = 2(-0.5) = -0.5 or 1/2**.   

Expand sigma:  
**1/3 [2(y_i - ŷ_i) + 2(y_i - ŷ_i) + 2(y_i - ŷ_i)]**  

**1/3 [2(-1/2) + 2(-1/2) + 2(-1/2)]** -> **1/3 2[(-1/2) + (-1/2) + (-1/2)]** -> **1/3(-3) = -1**.  

**∂MSE / ∂w = ∂MSE / ∂ŷ * x = -1(1)(-1) = 1.**

Similarly for **b** when **b = 1**:  
**∂MSE / ∂b = ∂MSE / ∂ŷ * x = -1(1)(-1) = 1.**  

## Adjustments
**w := w - α * (∂MSE/∂w)** & **b := b - α * (∂MSE/∂b)**  

Gradient of the loss function with respect to **w** -> **w := 0.5 - 0.01(∂MSE / ∂w) = 0.5 - 0.01(-1) = 0.49**.  
Gradient of the loss function with respect to **b** -> **b := 1 - 0.01(∂MSE / ∂b) = 0.5 - 0.01(-1) = 0.99**.  

# Translating the Math into Python
Keep in mind that we are now using all of **x** and **y_true** rather than only a single point.

```
# Given values
w = 0.5
b = 1
x = [-1, 0, 1]
y_true = [-3, -1, 1] 
alpha = 0.01

# Forward Pass
y_pred = [w * xi + b for xi in x]

# Calculate MSE
n = len (y_true)
mse = (1 / n) * sum ((yi - ypi) ** 2 for yi, ypi in zip(y_true, y_pred))

# Calculate the Gradients
d_mse_dw = (2 / n) * sum((ypi - yi) * xi for yi, ypi, xi in zip(y_true, y_pred, x))
d_mse_db = (2 / n) * sum(ypi - yi for yi, ypi in zip(y_true, y_pred))

# Adjustments for w and b
w -= alpha * d_mse_dw
b -= alpha * d_mse_db

# Print Updated Weight(s) and Bias
print("Updated w:", w)
print("Updated b:", b)
```

## Output
We receive a similar result when calculating for all points compared to a single point.

```
Updated w: 0.52
Updated b: 0.96
```
