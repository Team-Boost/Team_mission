import torch
import torch.nn as nn
import torchvision.datasets as dest
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

training_epochs = 15
batch_size = 100

root = './data'
train_dataset = dest.MNIST(root=root, train=True, transform=transforms.ToTensor(), download=True)
test_dataset = dest.MNIST(root=root, train=False, transform=transforms.ToTensor(), download=True)