#!/bin/bash
CONDA_BASE=$(conda info --base)
source ${CONDA_BASE}/etc/profile.d/conda.sh
conda activate fpgaconvnet-tutorial

# checkout fpgaconvnet repo
TUTORIAL_ROOT_PATH=$(git rev-parse --show-toplevel)

git clone https://github.com/Yu-Zhewen/fpgaconvnet-torch ${TUTORIAL_ROOT_PATH}/fpgaconvnet-torch
cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-torch
make torch-cpu
cd ..


git clone https://github.com/AlexMontgomerie/fpgaconvnet-optimiser ${TUTORIAL_ROOT_PATH}/fpgaconvnet-optimiser
cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-optimiser
git checkout dev
python -m pip install -e .
cd ..

git clone https://github.com/AlexMontgomerie/fpgaconvnet-model ${TUTORIAL_ROOT_PATH}/fpgaconvnet-model
cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-model
git checkout dev
python -m pip install -e .
cd ..

git clone https://github.com/AlexMontgomerie/fpgaconvnet-hls ${TUTORIAL_ROOT_PATH}/fpgaconvnet-hls
cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-hls
git checkout dev
git submodule update --init --recursive
python -m pip install -e .
cd ..

# install jupyter notebook and netron
pip install ipykernel jupyter netron
