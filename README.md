# Rock-Paper-Scissors Dataset

## Dataset

This repository contains an image dataset for **Rock-Paper-Scissors hand gesture classification**.

The dataset contains three classes:

* **Rock**
* **Paper**
* **Scissors**

The original images are stored in the `datasets/` directory.

### Original Dataset

The original dataset contains **247 images**:

| Class     | Number of Images |
| --------- | ---------------: |
| Rock      |               80 |
| Paper     |               80 |
| Scissors  |               87 |
| **Total** |          **247** |

## Dataset Diversity

When preparing the dataset, we considered variation in the visual appearance and recording conditions of the images. The dataset includes differences such as:

* **Different skin tones and hand appearances**, helping the model learn the gestures across a range of people rather than relying on one specific appearance.
* **Accessories**, such as rings, bracelets, watches, or other items that may appear on or near the hand.
* **Different backgrounds**, including variation in the environment surrounding the hand.
* **Different lighting and image conditions**, resulting in differences in brightness, shadows, and contrast.
* **Different hand positions and orientations**, providing variation in how the gestures are presented to the camera.

These variations are important because, in real-world use, the same Rock, Paper, or Scissors gesture may be presented by different people and under different environmental conditions.

## Data Augmentation

Data augmentation was applied to increase the variability of the dataset while keeping the original images unchanged.

The augmentation was implemented using **Python and the Pillow (PIL) library**. For each original image, one augmented version was generated.

The following transformations were randomly applied:

* **Horizontal flipping:** 50% probability of mirroring the image horizontally.
* **Rotation:** a random rotation between **-15° and +15°**.
* **Brightness adjustment:** brightness randomly varied between **85% and 115%** of the original.
* **Contrast adjustment:** contrast randomly varied between **85% and 115%** of the original.
* **Random cropping/zooming:** a random crop between **90% and 100%** of the original image area.
* **Resizing:** after cropping, the image was resized back to its original dimensions.

These transformations introduce additional variation in orientation, lighting, contrast, and image framing while keeping the Rock, Paper, and Scissors gestures recognizable.

## Augmented Dataset

The augmented dataset is stored in the `augmented_dataset/` directory.

Each original image was preserved, and one augmented version was created for each original image.

| Class     | Original Images | Augmented Images |   Total |
| --------- | --------------: | ---------------: | ------: |
| Rock      |              80 |               80 |     160 |
| Paper     |              80 |               80 |     160 |
| Scissors  |              87 |               87 |     174 |
| **Total** |         **247** |          **247** | **494** |

The augmented dataset therefore contains **494 images in total**.

### File Naming

The augmented dataset contains two versions of each image:

* `*_original.jpg` — the original image
* `*_augmented.jpg` — the transformed version of the original image

The original dataset was not modified during augmentation.


