import torch.utils.data as data
import os
from PIL import Image


class PortsetDataset(data.Dataset):
    def __init__(self, root, transform=None, target_transform=None, split="real_world"):
        self.root = root
        self.transform = transform
        self.target_transform = target_transform
        self.realworld_data, self.realworld_targets = None, None
        self.synthesized_data, self.synthesized_targets = None, None
        self.split = split

    def __getitem__(self, index):
        # We have 2 splits "real_world" and "synthesized". Each of these contain 2 folders "Input_images" and "GT_Images"
        # We will return the image from "Input_images" as data and the image from "GT_Images" as target
        if self.split == "real_world":
            if self.realworld_data is None:
                self.realworld_data, self.realworld_targets = self.prepare_data(
                    self.root
                )
            data, target = self.realworld_data[index], self.realworld_targets[index]
        elif self.split == "synthesized":
            if self.synthesized_data is None:
                self.synthesized_data, self.synthesized_targets = self.prepare_synth(
                    self.root
                )
            data, target = (
                self.synthesized_data[index],
                self.synthesized_targets[index],
            )
        else:
            raise ValueError("Invalid split name.")

        if self.transform is not None:
            data = self.transform(data)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return data, target

    def __len__(self):
        if self.split == "real_world":
            if self.realworld_data is None:
                self.realworld_data, self.realworld_targets = self.prepare_data(
                    self.root
                )
            return len(self.realworld_data)
        elif self.split == "synthesized":
            if self.synthesized_data is None:
                self.synthesized_data, self.synthesized_targets = self.prepare_synth(
                    self.root
                )
            return len(self.synthesized_data)
        else:
            raise ValueError("Invalid split name.")

    def _check_exists(self):
        return os.path.exists(self.root)

    def prepare_data(self, root):
        if not self._check_exists():
            raise RuntimeError("Dataset not found.")

        original_path = os.path.join(root, "RealWorld", "Input_images")
        blurred_path = os.path.join(root, "RealWorld", "GT_Images")
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
