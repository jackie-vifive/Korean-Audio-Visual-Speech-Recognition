import torch
from torch.utils.data import Dataset
import torchaudio
from torch.utils.data import DataLoader

class AudioDataLoader(Dataset):
    def __init__(self, text_path, wav_scp_path):
        with open(text_path, 'r') as f:
            self.labels = {line.split()[0]: " ".join(line.split()[1:]) for line in f.readlines() if len(line.split()) > 1}
            # self.labels = {line.split()[0]: " ".join(line.split()[1:]) for line in f.readlines()}
        
        with open(wav_scp_path, 'r') as f:
            self.audio_paths = {line.split()[0]: line.split()[1] for line in f.readlines()  if len(line.split()) > 1}

        self.utterances = list(self.audio_paths.keys())

    def __len__(self):
        return len(self.utterances)

    def __getitem__(self, idx):
        utt_id = self.utterances[idx]
        audio_path = self.audio_paths[utt_id]
        label = self.labels[utt_id]

        waveform, sample_rate = torchaudio.load(audio_path)
        # Optional: Transform waveform here (e.g., resampling, feature extraction)
        return waveform, sample_rate, label

    @staticmethod
    def collate_fn(batch):
        # Handle batching here if necessary
        waveforms, sample_rates, labels = zip(*batch)
        # Optional: Pad waveforms to the same length, stack, etc.
        return waveforms, sample_rates, labels

# Paths to your processed data
train_text_path = '/home/jupyter/Korean-Audio-Visual-Speech-Recognition/kaldi_formatted_data/train/text'
train_wav_scp_path = '/home/jupyter/Korean-Audio-Visual-Speech-Recognition/kaldi_formatted_data/train/wav.scp'
valid_text_path = '/home/jupyter/Korean-Audio-Visual-Speech-Recognition/kaldi_formatted_data/valid/text'
valid_wav_scp_path = '/home/jupyter/Korean-Audio-Visual-Speech-Recognition/kaldi_formatted_data/valid/wav.scp'

# Create dataset instances
train_dataset = AudioDataLoader(train_text_path, train_wav_scp_path)
valid_dataset = AudioDataLoader(valid_text_path, valid_wav_scp_path)

# Create DataLoader instances
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=AudioDataLoader.collate_fn)
valid_loader = DataLoader(valid_dataset, batch_size=32, shuffle=False, collate_fn=AudioDataLoader.collate_fn)
print(train_dataset)
print(train_loader)
