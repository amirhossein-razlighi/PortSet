"""tensorflow_portSet dataset."""

import tensorflow_datasets as tfds
import tensorflow as tf


class Builder(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for tensorflow_portSet dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release of PortSet.",
    }

    MANUAL_DOWNLOAD_INSTRUCTIONS = """\
    Manual download instructions are included in https://github.com/amirhossein-razlighi/PortSet.
    Please read the instructions carefully to download the dataset.
    """

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        return self.dataset_info_from_configs(
            features=tfds.features.FeaturesDict(
                {
                    "input_image": tfds.features.Image(shape=(None, None, 3)),
                    "blurred_image": tfds.features.Image(shape=(None, None, 3)),
                }
            ),
            supervised_keys=(
                "input_image",
                "blurred_image",
            ),
            homepage="https://github.com/amirhossein-razlighi/PortSet",
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        path = dl_manager.manual_dir
        return {
            "real_world": self._generate_examples(
                inp_path=path / "RealWorld" / "Input_Images",
                gt_path=path / "RealWorld" / "GT_Images",
            ),
            "synthesized": self._generate_examples(
                inp_path=path / "Synthesized" / "Input_Images",
                gt_path=path / "Synthesized" / "GT_Images",
            ),
        }

    def _generate_examples(self, inp_path, gt_path):
        """Yields examples."""
        for f in inp_path.glob("*.jpg"):
            inp_img = tf.io.read_file(str(f)).numpy()
            gt_img = tf.io.read_file(str(gt_path / f.name)).numpy()

            yield f.name, {
                "input_image": inp_img,
                "blurred_image": gt_img,
            }
