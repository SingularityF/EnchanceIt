import subprocess
import os
import uuid

def waifu2x_chainer(path_input):
    path_output = make_output_path('png')
    process = subprocess.Popen([
        'python3',
        'waifu2x.py',
        '-m',
        'noise_scale',
        '-n',
        '2',
        '-i',
        path_input,
        '-o',
        path_output,
        '-a',
        '1',
        ],
        cwd='algorithms/waifu2x-chainer',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    assert (len(stderr)==0), "Error running algorithm"
    return path_output


def make_output_path(ext):
    if not os.path.exists('processed'):
        os.mkdir('processed')
    filename = str(uuid.uuid4())
    filepath = f"processed/{filename}.{ext}"
    return os.path.abspath(filepath)


if __name__ == "__main__":
    path_input = "/home/haitianl95/EnhanceIt/src/downloads/2e1d68bb-0105-40ba-b67e-279feafc0b75.jpeg"
    waifu2x_chainer(path_input)
