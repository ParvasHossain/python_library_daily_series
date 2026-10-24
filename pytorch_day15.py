import torch

# Tensor with gradient tracking enabled
x = torch.tensor([2.0, 3.0], requires_grad=True, device="cpu")

# Dynamic forward pass builds computation graph on the fly
y = x ** 2 + 3 * x + 1
z = y.sum()

# Autograd traverses DAG backwards to calculate derivatives (dz/dx = 2x + 3)
z.backward()

print("Inputs:", x)
print("Computed Gradients (dz/dx):", x.grad) # Output: tensor([7., 9.])