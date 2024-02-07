# [fpgaConvNet](https://icidsl.github.io/fpgaconvnet-website/)

fpgaConvNet is an automated toolflow for designing Convolutional Neural Network (CNN) accelerators on FPGAs with state-of-the-art performance and efficiency. 

The toolflow can be used to accelerate a number of applications, including: Classification, Object Detection, Segmentation, Human Action Recognition, Key Word Spotting, Anomaly Detection, and etc.


## Project Structure

The fpgaConvNet codebase is split into 4 invididual repositories: 

[fpgaconvnet-torch](https://github.com/Yu-Zhewen/fpgaconvnet-torch), a collection of pre-trained CNN models, providing emulated accuracy results for features such as quantization and sparsity. This repository is optional, if users can provide their own onnx model instead.

[fpgaconvnet-model](https://github.com/AlexMontgomerie/fpgaconvnet-model), providing hardware performance and resource modeling, and converting the onnx model to a json-format acclerator configuration.

[fpgaconvnet-optimiser](https://github.com/AlexMontgomerie/fpgaconvnet-optimiser), performing Design Space Exploration based on the model predictions to identify the optimal acclerator configuration.

[fpgaconvnet-hls](https://github.com/AlexMontgomerie/fpgaconvnet-hls), containing hls code templates,  translating the identified accelerator configuration into actual source files which can synthesized by Xilinx tools.

The relationship between these repositories are shown as the figrue below.
<img src="toolflow.png">


## Get Started

To set up the environment, please follow the steps [here](tutorial/0_get_started/README.md).

You are also welcome to try our end-to-end development example [here](tutorial/1_simple_end_to_end).
