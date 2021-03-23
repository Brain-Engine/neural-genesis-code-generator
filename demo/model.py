import torch
from torch import nn


class MyModel(nn.Module):
    def __init__(self,  ):
        super(MyModel, self).__init__()
        self.Conv2d_g34 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3)
        self.BatchNorm2d_g37 = nn.BatchNorm2d(num_features=16)
        self.ReLU_g38 = nn.ReLU(inplace=True)
        self.Conv2d_g41 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=0)
        self.BatchNorm2d_g42 = nn.BatchNorm2d(num_features=32)
        self.ReLU_g43 = nn.ReLU(inplace=True)
        self.MaxPool2d_g53 = nn.MaxPool2d(kernel_size=2)
        self.AdaptiveAvgPool2d_g71 = nn.AdaptiveAvgPool2d(output_size=1)
        self.Linear_g83 = nn.Linear(in_features=32, out_features=10)
        self.Flatten_g89 = nn.Flatten()

    def forward(self, x):
        g34 = self.Conv2d_g34(x)
        g37 = self.BatchNorm2d_g37(g34)
        g38 = self.ReLU_g38(g37)
        g53 = self.MaxPool2d_g53(g38)
        g41 = self.Conv2d_g41(g53)
        g42 = self.BatchNorm2d_g42(g41)
        g71 = self.AdaptiveAvgPool2d_g71(g42)
        g43 = self.ReLU_g43(g71)
        g89 = self.Flatten_g89(g43)
        return g89
