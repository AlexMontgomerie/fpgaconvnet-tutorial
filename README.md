# fpgaConvNet Tutorial

A collection of tutorials for the fpgaConvNet framework. It is recommeneded to
start with the [end-to-end-example](end-to-end-example.ipynb).

## Setup

### Python Tools

It is recommended to use
[conda](https://docs.conda.io/en/latest/miniconda.html#installing) to manage
your python environment. Also, a python version above 3.8 is required.

```
conda create -n fpgaconvnet python=3.8
```

SAMO and fpgaConvNet packages are also required.

```
python -m pip install samo fpgaconvnet-model fpgaconvnet-hls
```

### Vivado

The [fpgaconvnet-hls](https://github.com/AlexMontgomerie/fpgaconvnet-hls)
project relies on Vivado 2019.1. To install, first [download](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/2019-1.html)
from the Xilinx website.

Once installed, you will need to add a license server to your .bashrc file. You
will also need to add Vivado to your path. To do so, add the following to your
`.basrc`:

```
export PATH=/tools/Xilinx/Vivado/2019.1/bin:$PATH
export PATH=/tools/Xilinx/SDK/2019.1/bin:$PATH
```


You will need to setup JTAG drivers to program a device. To do so, execute the
following script:

```
/tools/Xilinx/Vivado/2019.1/data/xicom/cable_drivers/lin64/install_script/install_drivers/install_drivers
```

For more information, visit [here](https://www.xilinx.com/support/answers/59128.html).

#### Bug Workarounds

The [Y2K22 patch](https://support.xilinx.com/s/article/76960?language=en_US) is
required to fix issues with exporting designs in HLS. Please follow the
instructions [here](https://support.xilinx.com/s/article/76960?language=en_US).

Also, there is a known
[bug](http://svn.clifford.at/handicraft/2017/vivadobugs/vivadobug04.txt) to do
with C++ libraries. A workaround for this is adding the `mpfr.h` and `gmp.h`
headers manually. For this project, you need to create a header file
`fpgaconvnet/hls/hardware/system.hpp` which includes the following:

```C
#ifndef SYSTEM_HPP_
#define SYSTEM_HPP_

#include "(path to Vivado 2019.1)/include/gmp.h"
#include "(path to Vivado 2019.1)/include/mpfr.h"

#endif
```

> this isn't always necessary, so you can just create a blank header file if
your system doesn't encounter this bug

## Jupyter Setup

All the tutorials are done with jupyter notebook. Firstly, `ipykernel` and
`jupyter` need to be installed.

```
conda install -c anaconda ipykernel jupyter
```

To run the notebooks locally, firstly you will need to add the python
environment to `ipykernel`.

```
python -m ipykernel install --user --name=fpgaconvnet
```

Now you can start the notebook. Follow the instructions in the command line to
view it in your browser.

```
jupyter notebook --no-browser --port=8888
```


