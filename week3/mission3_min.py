import numpy as np


"""
Q1
"""
arr1 = np.random.rand(5,3)
arr2 = np.random.rand(3,4)

dot = np.dot(arr1, arr2)
print(dot, dot.shape)


"""
Q2
"""
arr1 = np.array([[5,7],[9,11]], float)
arr2 = np.array([[2,4],[6,8]], float)

concat_1 = np.concatenate((arr1, arr2), axis=0)
concat_2 = np.concatenate((arr1, arr2), axis=1)

print(concat_1)
print(concat_2)


"""
Q3
"""
xy=np.array([[1., 2. ,3. ,4. ,5. ,6.],
            [10., 20., 30., 40., 50., 60.]])

x_train=xy[0]
y_train=xy[1]

print(x_train, x_train.shape)
print(y_train, y_train.shape)


"""
Q4
"""
beta_gd = np.random.rand(1)
bias = np.random.rand(1)

print(beta_gd, bias)


"""
Q5
"""
xy = np.array([[1., 2. ,3. ,4. ,5. ,6.],
            [3., 6., 9., 12., 15., 18.]])

x_train = xy[0]
y_train = xy[1]
beta_gd = np.random.rand(1)
bias = np.random.rand(1)
learning_rate = 0.01

for i in range(1000):
    pred  = (beta_gd*x_train) + bias
    error = ((pred - y_train) ** 2).mean()
    gd_w  = ((pred - y_train) * 2 * x_train).mean()
    gd_b  = ((pred - y_train) * 2).mean()

    beta_gd -= learning_rate * gd_w
    bias -= learning_rate * gd_b

    if i % 100 ==0 :
        print('Epoch ({:10d}/1000) cost(error): {:10f}, w(beta_gd):{:10f}, bias:{:10f}'.format(i, error, beta_gd.item(), bias.item()))
