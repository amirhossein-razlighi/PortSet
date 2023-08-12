import torch.utils.data as data
import os
from PIL import Image


class PortsetDataset(data.Dataset):
    def __init__(self, root, transform=None, target_transform=None):
        self.root = root
        self.transform = transform
        self.target_transform = target_transform
        self.data, self.targets = self.prepare_data(root)

    def __getitem__(self, index):
        img, target = self.data[index], self.targets[index]
        if self.transform is not None:
            img = self.transform(img)
        if self.target_transform is not None:
            target = self.target_transform(target)
        return img, target

    def __len__(self):
        return len(self.data)

    def _check_exists(self):
        return os.path.exists(self.root)

    def prepare_data(self, root):
        if not self._check_exists():
            raise RuntimeError("Dataset not found.")

        original_path = os.path.join(root, "Input_images")
        blurred_path = os.path.join(root, "GT_Images")
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
