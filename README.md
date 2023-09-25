# PneumoGuard

A deep learning based on the ResNet152 architecture that detects pneumonia from CT scans of lungs. 
The dataset used for training this model can be found [here](https://data.mendeley.com/datasets/rscbjbr9sj/3).

## Methodology

The model was trained for 100 epochs, with early stopping set to kick in at 10, with a batch size of 32. The model was trained on RTX 3080 Ti.

## Model Architecture

The model uses a base layer of ResNet152.

<p align='center'>
    <img src="Images/PneumoGuard_architecture.png" alt='PneumoGuard Model Architecture' width="20%" height="20%">
    <br>
    <p align='center'>Figure 1: PneumoGuard Model Architecture</p>
</p>

### ResNet-152

Residual Networks, or ResNets, learn residual functions with reference to the layer inputs, instead of learning unreferenced functions. Instead of hoping each few stacked layers directly fit a desired underlying mapping, residual nets let these layers fit a residual mapping. They stack residual blocks ontop of each other to form network.
ResNet-152, short for "Residual Network 152," is a deep convolutional neural network architecture that belongs to the ResNet family. ResNet-152 is specifically known for its depth, consisting of 152 layers, making it a relatively deep neural network.

## Results

PneumoGuard achieved a training accuracy of 95.23%, training loss of 15.59%, validation accuracy of 89.74%, validation loss of 25.33%, testing accuracy of 87.34%, and testing loss of 38.14%. The accuracy can be further improved by training the model for more epochs and modifying the model architecture.

<div style="display: flex; justify-content: space-between;">
    <div style="flex: 1;">
        <img src="Images/PneumoGuard_accuracy.png" alt="PneumoGuard Accuracy Plot" style="max-width: 50%;">
        <figcaption align='center'>Figure 2: PneumoGuard Accuracy Plot</figcaption>
    </div>
    <div style="flex: 1;">
        <img src="Images/PneumoGuard_loss.png" alt="PneumoGuard Loss Plot" style="max-width: 50%;">
        <figcaption align='center'>Figure 3: PneumoGuard Loss Plot</figcaption>
    </div>
</div>
