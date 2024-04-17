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