# Korean-Audio-Visual-Speech-Recognition

Jackie Ryu (br2543)

May 6th 2024

## Abstract
This paper presents a novel method to enhance Korean Audio-Visual Speech Recognition (AVSR) using the Open Large-Scale Korean Audio-Visual Speech (OLKAVS) dataset. We propose a Dual-Stream Transformer Network that processes audio and visual streams independently by means of distinct encoders and Transformer layers. A crucial part of this network is the cross-modal attention, which combines audio and visual streams in a dynamic fashion, and gives a broader context for speech recognition. We further include a lip-estimator to the visual stream, focusing on the most relevant lip movement visual cues, in order to increase noise robustness and save computational cost. We expect our method to significantly outperform traditional hybrid conformer models and establish a new state-of-the-art for Korean AVSR systems.

## Tools
[aihubshell](https://aihub.or.kr/devsport/apishell/list.do?currMenu=403&topMenu=100) - for downloading data from AIHub
[OLKAVS Paper](https://arxiv.org/pdf/2301.06375)

## Directory Structure
```plaintext
.
├── aihubshell                   # Shell scripts for automating dataset downloads and preprocessing
├── avsr
│   ├── models                   # Model definitions
│   │   ├── conformer            # Conformer model for audio processing
│   │   └── resnet               # ResNet model for visual processing
│   ├── scheduler                # Learning rate schedulers
│   └── utils                    # Utility scripts including data loaders and metric definitions
├── configs                      # Configuration for training and inference
├── dataset                      # Dataset modules including augmentation and feature extraction
├── inference.py                 # Script for inference
├── preprocess                   # Scripts for data preprocessing
├── raw_data                     # Raw dataset directories
├── requirements.txt             # Python dependencies
├── sample_data                  # Sample processed data for quick tests
├── train.py                     # Training script
├── trained_model                # Directory for trained models
```

## Setup and Run
1. Install dependencies

`pip isntall -r requirements.txt`

2. Prepare the dataset (Skip for testing)

`python download.py`
`./process.sh`
`python romanize_directories.py`
`python label_preprocess.py`

3. Run Training

`python train.py -c configs/av_train.yaml`

5. Run Inference

`python inference.py -c configs/inference.yaml`

6. Check Error Rate

`python visualize.py`

7. Check for output in sample_data/
