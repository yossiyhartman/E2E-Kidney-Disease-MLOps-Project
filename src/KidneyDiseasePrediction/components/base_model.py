import torch

from pathlib import Path
from torchvision.models import vgg16
from KidneyDiseasePrediction import logger
from KidneyDiseasePrediction.entity.config_entity import BaseModelConfig


class BaseModel:
    def __init__(self, config: BaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = vgg16(weights=self.config.params_weights)
        self.save_model(self.config.base_model_path, self.model)

    def modify_base_model(self):
        layers = list(self.model.features.children())
        total_layers = len(layers)
        freeze_until = int(total_layers * self.config.params_freeze_ratio)

        for i, layer in enumerate(layers):
            if i < freeze_until:
                for param in layer.parameters():
                    param.requires_grad = False

        self.model.classifier[6] = torch.nn.Linear(in_features=4096, out_features=self.config.params_classes)

        self.save_model(self.config.modified_base_model_path, self.model)

    @staticmethod
    def save_model(path: Path, model: torch.nn.Module):
        torch.save(model, path)
