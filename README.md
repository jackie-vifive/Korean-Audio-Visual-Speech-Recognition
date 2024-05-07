# Korean-Audio-Visual-Speech-Recognition

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
