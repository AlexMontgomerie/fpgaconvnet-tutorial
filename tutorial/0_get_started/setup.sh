#!/bin/bash

# checkout fpgaconvnet repo
TUTORIAL_ROOT_PATH=$(git rev-parse --show-toplevel)

git clone https://github.com/Yu-Zhewen/fpgaconvnet-torch ${TUTORIAL_ROOT_PATH}/fpgaconvnet-torch
cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-torch
make torch-cpu
export FPGACONVNET_TORCH=${WORK_DIR}
export PYTHONPATH=$PYTHONPATH:$FPGACONVNET_TORCH
cd ..


git clone https://github.com/AlexMontgomerie/fpgaconvnet-optimiser ${TUTORIAL_ROOT_PATH}/fpgaconvnet-optimiser
cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-optimiser
git checkout dev-petros
python -m pip install -e .
cd ..

git clone https://github.com/AlexMontgomerie/fpgaconvnet-model ${TUTORIAL_ROOT_PATH}/fpgaconvnet-model
cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-model
git checkout dev-petros
python -m pip install -e .
cd ..

git clone https://github.com/AlexMontgomerie/fpgaconvnet-hls ${TUTORIAL_ROOT_PATH}/fpgaconvnet-hls

# install jupyter notebook
pip install ipykernel jupyter
