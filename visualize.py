import torch
import argparse
from avsr.utils.model_builder import build_model
from vocabulary.utils import KsponSpeechVocabulary

def visualize_model(config_path, output_file):
    # Load configuration
    import yaml
    with open(config_path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    vocab = KsponSpeechVocabulary(unit=config['tokenize_unit'])

    # Initialize model
    model = build_model(
        vocab_size=len(vocab),
        pad_id=vocab.pad_id,
        architecture=config['architecture'],
        loss_fn=config['loss_fn'],
        front_dim=config['front_dim'],
        encoder_n_layer=config['encoder_n_layer'],
        encoder_d_model=config['encoder_d_model'],
        encoder_n_head=config['encoder_n_head'],
        encoder_ff_dim=config['encoder_ff_dim'],
        encoder_dropout_p=config['encoder_dropout_p'],
        decoder_n_layer=config['decoder_n_layer'],
        decoder_d_model=config['decoder_d_model'],
        decoder_n_head=config['decoder_n_head'],
        decoder_ff_dim=config['decoder_ff_dim'],
        decoder_dropout_p=config['decoder_dropout_p'],
        pass_visual_frontend=False
    )

    # Redirect print to a file
    with open(output_file, 'w') as file:
        print(model, file=file)
        try:
            from torchinfo import summary
            summary(model, input_size=(1, 1000), device="cpu", print_fn=lambda x: file.write(x + '\n'))
        except ImportError:
            print("torchinfo not installed, only printing basic model structure.", file=file)

def get_args():
    parser = argparse.ArgumentParser(description='Model visualization.')
    parser.add_argument('-c', '--config', type=str, required=True, help='Configuration file path')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file path')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_args()
    visualize_model(args.config, args.output)
