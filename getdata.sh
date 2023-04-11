#!/bin/bash
# install kaggle api on default conda env
ml anaconda3/2021.5
source /hpc/packages/minerva-centos7/anaconda3/2021.5/etc/profile.d/conda.sh
conda activate base
conda install -c conda-forge kaggle
# load git module on minerva
ml git
git clone https://github.com/chrisporras/xgdiss.git
# install Kaggle public api
# Make sure preinstalled in own env
# pip install -q kaggle
# Choose the kaggle.json file that you downloaded
mkdir ~/.kaggle
cp ./xgdiss/kaggle.json ~/.kaggle/
# Make directory named kaggle and copy kaggle.json file there.
chmod 600 ~/.kaggle/kaggle.json
# Change the permissions of the file.
kaggle datasets list

### Uncomment datasets to dl ###
# Download 5gb reduced data
kaggle datasets download -d arianghasemi/mayo-clinic-resized-5gb
mkdir 5gb
mv mayo-clinic-resized-5gb.zip 5gb/
unzip 5gb/mayo-clinic-resized-5gb.zip
# # Download resized images
# kaggle datasets download -d daviddirethucus/mayoclinicai-224456600-resized-training-images
# unzip mayoclinicai-224456600-resized-training-images.zip
# # Download normalized dataset
# kaggle datasets download -d tr1gg3rtrash/mayo-clinic-strip-ai-normalized-dataset
# unzip mayo-clinic-strip-ai-normalized-dataset.zip
# # Download thresholded tiled data
# kaggle datasets download -d tr1gg3rtrash/mayo-clinic
# unzip mayo-clinic.zip
# # Download 12gb tiled data
# kaggle datasets download -d yasufuminakama/mayo-train-images-size1024-n16
# unzip mayo-train-images-size1024-n16.zip
# # Download full data
# kaggle competitions download -c mayo-clinic-strip-ai
# unzip mayo-clinic-strip-ai.zip
