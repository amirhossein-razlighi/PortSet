"""tensorflow_portSet dataset."""

import tensorflow_datasets as tfds
import tensorflow_portSet_dataset_builder


class TensorflowPortsetTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for tensorflow_portSet dataset."""
  # TODO(tensorflow_portSet):
  DATASET_CLASS = tensorflow_portSet_dataset_builder.Builder
  SPLITS = {
      'train': 1,  # Number of fake train example
      'test': 1,  # Number of fake test example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'name': 'DatasetV1.0.0.zip'}
  SKIP_CHECKSUMS = True


if __name__ == '__main__':
  tfds.testing.test_main()
