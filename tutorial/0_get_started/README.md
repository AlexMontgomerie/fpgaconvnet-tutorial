# Get started: Install and Run fpgaConvNet


## Installation Steps

In this section, we demonstrate how to set up the environment for fpgaConvNet.

As a prerequisite, install the following software on your machine:

1. **miniconda:**  [https://docs.conda.io/projects/miniconda/en/latest/](https://docs.conda.io/projects/miniconda/en/latest/)

2. **grahviz:** [https://graphviz.org/download/](https://graphviz.org/download/)

23. **protocol buffer compiler:** [https://grpc.io/docs/protoc-installation/](https://grpc.io/docs/protoc-installation/)


4. **vivado 2019.1/2:** [https://www.xilinx.com/support/download.html](https://www.xilinx.com/support/download.html)

5. **vivado Y2K22 patch:** [https://support.xilinx.com/s/article/76960?language=en_US](https://support.xilinx.com/s/article/76960?language=en_US)

Afterwards, create a new conda environment named as `fpgaconvnet-tutorial` and run the provided srcipt `setup.sh` to finish the setup 

```
conda create -n fpgaconvnet-tutorial python=3.10
conda activate fpgaconvnet-tutorial
bash setup.sh
```

To check the installation is successful, run the following commands in your bash shell, and make sure there is no error showing.

```
python -c "import torch"
python -c "import fpgaconvnet"
```
