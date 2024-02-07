#!/bin/bash
CONDA_BASE=$(conda info --base)
source ${CONDA_BASE}/etc/profile.d/conda.sh
conda activate fpgaconvnet-tutorial

TUTORIAL_ROOT_PATH=$(git rev-parse --show-toplevel)

cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-torch
git pull
export FPGACONVNET_TORCH=${TUTORIAL_ROOT_PATH}/fpgaconvnet-torch
export PYTHONPATH=$PYTHONPATH:$FPGACONVNET_TORCH
cd ..

cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-optimiser
git pull
cd ..

cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-model
git pull
cd ..

cd ${TUTORIAL_ROOT_PATH}/fpgaconvnet-hls
git pull
cd ..

jupyter notebook