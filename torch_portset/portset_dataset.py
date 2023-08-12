import torch.utils.data as data
import os
from PIL import Image


class PortsetDataset(data.Dataset):
    def __init__(self, root, transform=None, target_transform=None):
        self.root = root
        self.transform = transform
        self.target_transform = target_transform
        self.realworld_data, self.realworld_targets = None, None
        self.synthesized_data, self.synthesized_targets = None, None

    def __getitem__(self, index):
        if not type(index) == str:
            raise Exception(
                "You should choose between synthesized and real_world splits!"
            )
        if index == "synthesized":
            if self.synthesized_data is None:
                self.synthesized_data, self.synthesized_targets = self.prepare_synth(
                    self.root
                )
            return self.synthesized_data, self.synthesized_targets
        elif index == "real_world":
            if self.realworld_data is None:
                self.realworld_data, self.realworld_targets = self.prepare_data(
                    self.root
                )
            return self.realworld_data, self.realworld_targets
        else:
            raise Exception(
                "You should choose between synthesized and real_world splits!"
            )

    def __len__(self):
        return len(self.realworld_data) + len(self.synthesized_data)

    def _check_exists(self):
        return os.path.exists(self.root)

    def prepare_data(self, root):
        if not self._check_exists():
            raise RuntimeError("Dataset not found.")

        original_path = os.path.join(root, "Real_World", "Input_images")
        blurred_path = os.path.join(root, "Real_World", "GT_Images")
        original_images = os.listdir(original_path)
        blurred_images = os.listdir(blurred_path)

        data = []
        targets = []
        for i in range(len(original_images)):
            original_image = Image.open(os.path.join(original_path, original_images[i]))
            blurred_image = Image.open(os.path.join(blurred_path, blurred_images[i]))
            data.append(original_image)
            targets.append(blurred_image)
        return data, targets

    def prepare_synth(self, root):
        if not self._check_exists():
            raise RuntimeError("Dataset not found.")

        original_path = os.path.join(root, "Synthesized", "Input_images")
        blurred_path = os.path.join(root, "Synthesized", "GT_Images")
        original_images = os.listdir(original_path)
        blurred_images = os.listdir(blurred_path)

        data = []
        targets = []
        for i in range(len(original_images)):
            original_image = Image.open(os.path.join(original_path, original_images[i]))
            blurred_image = Image.open(os.path.join(blurred_path, blurred_images[i]))
            data.append(original_image)
            targets.append(blurred_image)
        return data, targets
