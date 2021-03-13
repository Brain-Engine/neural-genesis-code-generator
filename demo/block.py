import torch
from torch import nn


class MyModel(nn.Module):
    def __init__(self, in_channel, out_channel):
        super(MyModel, self).__init__()
        self.conv = nn.Conv2d(in_channel, out_channel, (3, 3))

    @staticmethod
    def forward(x):
        x = x
        return x