import torch
import torch.optim as optim
from torch.nn import CTCLoss

# Assuming `model` is your model instance and `data_loader` is your DataLoader for training data
optimizer = optim.Adam(model.parameters(), lr=0.001)
ctc_loss = CTCLoss(blank=0)  # Assuming blank token is at index 0

for epoch in range(num_epochs):
    model.train()
    for inputs, targets, input_lengths, target_lengths in data_loader:
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(inputs)
        outputs = outputs.log_softmax(2)  # CTC Loss expects log probabilities

        # Compute loss, assuming outputs are (T, N, C)
        loss = ctc_loss(outputs, targets, input_lengths, target_lengths)
        
        # Backward pass and optimizer step
        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch}, Loss: {loss.item()}")