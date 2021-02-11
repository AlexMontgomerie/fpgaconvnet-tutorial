# fpgaConvNet Optimiser Tutorial

The [fpgaConvNet Optimiser](https://github.com/AlexMontgomerie/fpgaconvnet-optimiser) is the frontend for generating the dataflow hardware configuration for a given convolutional neural network. In this tutorial, The main aspects to this optimiser will be covered. A step by step guide of stages to the model to hardware description is given. Instructions on using the command-line interface are given towards the end.

## 1. Initialising a Hardware Model

The first step is parsing the CNN model into an initial hardware model. This initial hardware model is a very basic implementation, which maps the CNN layers to their hardware equivalent. 

The first step is to intialise a `Network` model. This class the top-level in the hierarchy of hardware model abstractions.

```python
from fpgaconvnet_optimiser.models.network import Network

lenet = Network("lenet", "examples/models/lenet.onnx")
```

At the moment, this hardware model of LeNet has no knowledge of the 

## 2. Applying Transforms


### Partitioning
