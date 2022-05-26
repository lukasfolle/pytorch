import torch
from torch import Tensor

# class to store APoT quantized tensor
class APoT_tensor:
    TensorAPoT = torch.Tensor()

    @staticmethod
    def quantize_APoT(tensor2quantize: Tensor) -> Tensor:
        raise NotImplementedError

    @staticmethod
    def dequantize(self) -> Tensor:
        raise NotImplementedError

    def q_apot_alpha(self) -> float:
        raise NotImplementedError