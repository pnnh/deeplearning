import torch

# 演示如何设置pytorch占用的显存大小
# 默认情况下，pytorch会占用所有可用的显存

# 设置每个进程使用的显存比例为0.5
torch.cuda.set_per_process_memory_fraction(0.5)

# 检查显卡是否可用
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using GPU:", torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")
    print("Using CPU")

# 创建一个随机张量
x = torch.rand(1000, 1000).to(device)

# 打印张量大小
print("Tensor size:", x.size())