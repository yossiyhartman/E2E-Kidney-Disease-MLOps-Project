import torch

from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
from pathlib import Path

from KidneyDiseasePrediction.entity.config_entity import ModelTrainingConfig


class Training:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = torch.load(self.config.modified_base_model_path, weights_only=False)

    def train_valid_generators(self):

        transform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor(), transforms.Normalize(mean=[0.5], std=[0.5])])
        dataset = datasets.ImageFolder(root=self.config.training_data, transform=transform)

        train_size = int(0.8 * len(dataset))
        valid_size = len(dataset) - train_size
        train_dataset, valid_dataset = random_split(dataset, [train_size, valid_size])

        self.train_loader = DataLoader(train_dataset, batch_size=self.config.params_batch_size, shuffle=True)
        self.valid_loader = DataLoader(valid_dataset, batch_size=self.config.params_batch_size, shuffle=False)

    def train_model(self):
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=self.config.params_learning_rate)

        for epoch in range(self.config.params_epochs):
            self.model.train()
            for images, labels in self.train_loader:
                optimizer.zero_grad()
                outputs = self.model(images)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

            print(f"Epoch [{epoch + 1}/{self.config.params_epochs}], Loss: {loss.item():.4f}")

        self.save_model(self.config.trained_model_path, self.model)

    @staticmethod
    def save_model(path: Path, model: torch.nn.Module):
        torch.save(model, path)
