import torch
from torch.backends import cudnn

cuda_available = torch.cuda.is_available()

if cuda_available:
    print("CUDA is available")
else:
    print("CUDA is not available")


cudnn_available = cudnn.is_available()

if cudnn_available:
    print("cuDNN is available")
else:
    print("cuDNN is not available")

cuda_version = torch.version.cuda

print("CUDA version:", cuda_version)

def gpu_info() -> str:
    info = ''
    for id in range(torch.cuda.device_count()):
        p = torch.cuda.get_device_properties(id)
        info += f'CUDA:{id} ({p.name}, {p.total_memory / (1 << 20):.0f}MiB)\n'
    return info[:-1]

if __name__ == '__main__':
    print('GPU info: ', gpu_info())