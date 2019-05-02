import os
import subprocess


def get_gpu(really=True):
    if really:
        # try:
        #     command = 'nvidia-smi --query-gpu=memory.free,memory.total --format=csv |tail -n+2| ' \
        #           'awk \'BEGIN{FS=" "}{if ($1/$3 > 0.98) print NR-1}\''
        #     gpu_idx = subprocess.check_output(command, shell=True).rsplit(b'\n')[0].decode('utf-8')
        #     print('Using GPU {}.'.format(gpu_idx))
        # except subprocess.CalledProcessError:
        #     raise ValueError('No GPUs seems to be available.')
        gpu_idx = '0'
    else:
        gpu_idx = '-1'
    os.environ['CUDA_VISIBLE_DEVICES'] = gpu_idx
