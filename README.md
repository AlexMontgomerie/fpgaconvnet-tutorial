
![fpgaconvnet-tutorial](https://github.com/AlexMontgomerie/fpgaconvnet-tutorial/assets/26148252/00ed7328-5025-4c4e-a689-3b6b41c42958)

__Welcome to the start of your fpgaConvNet journey!__

fpgaConvNet is an automated toolflow for designing Convolutional Neural Network (CNN) accelerators on FPGAs with state-of-the-art performance and efficiency. 
It takes an CNN model description (either PyTorch or ONNX) and platform constraints of an FPGA, and produces a bitstream of an accelerator which is optimised for the specific FPGA and model pair.
In this repo we will take you through the different aspects of the [fpgaConvNet toolflow](https://icidsl.github.io/fpgaconvnet-website) using examples of interacting with the API, from hardware component modelling all the way to end-to-end model to accelerator compilation.

The toolflow can be used to accelerate a number of applications, including: Image Classification, Object Detection, Segmentation, Human Action Recognition, Key Word Spotting, Anomaly Detection, and etc.

### Environment setup can be found at [0: Getting Started](tutorial/0_get_started/README.md).

You are also welcome to try our end-to-end development example [here](tutorial/1_simple_end_to_end).

## Project Structure

![tutorial-structure](https://github.com/AlexMontgomerie/fpgaconvnet-tutorial/assets/26148252/8efae979-0ab6-4a25-b578-0e1b396ff8b5)

The fpgaConvNet codebase is split into 4 invididual repositories: 

[fpgaconvnet-torch](https://github.com/Yu-Zhewen/fpgaconvnet-torch), a collection of pre-trained CNN models, providing emulated accuracy results for features such as quantization and sparsity. This repository is optional, if users can provide their own onnx model instead.

[fpgaconvnet-model](https://github.com/AlexMontgomerie/fpgaconvnet-model), providing hardware performance and resource modeling, and converting the onnx model to a json-format acclerator configuration.

[fpgaconvnet-optimiser](https://github.com/AlexMontgomerie/fpgaconvnet-optimiser), performing Design Space Exploration based on the model predictions to identify the optimal acclerator configuration.

[fpgaconvnet-hls](https://github.com/AlexMontgomerie/fpgaconvnet-hls), containing hls code templates,  translating the identified accelerator configuration into actual source files which can synthesized by Xilinx tools.
