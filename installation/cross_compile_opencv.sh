#!/bin/bash
# A very gross script to cross compile opencv for arm-linux-gnueabihf arch

NUMCORES=`nproc`

sudo apt update && \
sudo apt install -y gcc-arm-linux-gnueabihf \
                    g++-arm-linux-gnueabihf \
                    cmake \
                    pkgconf

cd ~ && \
git clone https://github.com/opencv/opencv && \ 
cd opencv/platforms/linux && \
mkdir -p armhf && \
cd armhf && \
cmake -DCMAKE_TOOLCHAIN_FILE=../arm-gnueabi.toolchain.cmake ../../.. && \
make -j$NUMCORES
