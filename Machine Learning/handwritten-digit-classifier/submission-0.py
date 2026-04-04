import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        self.f1 = nn.Linear(784,512)
        self.relu = nn.ReLU()
        self.drop = nn.Dropout(p=0.2)
        self.out = nn.Linear(512, 10)
        self.sigmoid = nn.Sigmoid()

        # Define the architecture here
    
    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        return self.sigmoid(self.out(self.relu(self.drop(self.f1(images)))))
        # Return the model's prediction to 4 decimal places
