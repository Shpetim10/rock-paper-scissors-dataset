from PIL import Image, ImageEnhance, ImageOps
import os
import random

# Where the original dataset is located
INPUT_DIR = "rock-paper-scissors-dataset-main/datasets"

# Where the new augmented dataset will be saved
OUTPUT_DIR = "augmented_dataset"

# Your three classes
CLASSES = ["rock", "paper", "scissors"]


def augment_image(image):
    """Create one random augmented version of an image."""

    # Horizontal flip with 50% probability
    if random.random() < 0.5:
        image = ImageOps.mirror(image)

    # Small rotation
    angle = random.uniform(-15, 15)
    image = image.rotate(angle, resample=Image.Resampling.BICUBIC)

    # Slight brightness change
    brightness = random.uniform(0.85, 1.15)
    image = ImageEnhance.Brightness(image).enhance(brightness)

    # Slight contrast change
    contrast = random.uniform(0.85, 1.15)
    image = ImageEnhance.Contrast(image).enhance(contrast)

    # Small random crop and resize
    width, height = image.size

    crop_ratio = random.uniform(0.90, 1.0)

    crop_width = int(width * crop_ratio)
    crop_height = int(height * crop_ratio)

    left = random.randint(0, width - crop_width)
    top = random.randint(0, height - crop_height)

    image = image.crop((
        left,
        top,
        left + crop_width,
        top + crop_height
    ))

    image = image.resize((width, height), Image.Resampling.LANCZOS)

    return image


# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

total_original = 0
total_augmented = 0

for class_name in CLASSES:

    input_class_dir = os.path.join(INPUT_DIR, class_name)
    output_class_dir = os.path.join(OUTPUT_DIR, class_name)

    os.makedirs(output_class_dir, exist_ok=True)

    if not os.path.exists(input_class_dir):
        print(f"WARNING: Could not find {input_class_dir}")
        continue

    for filename in os.listdir(input_class_dir):

        input_path = os.path.join(input_class_dir, filename)

        # Only process image files
        if not filename.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp", ".webp")
        ):
            continue

        try:
            image = Image.open(input_path).convert("RGB")

            # Save original image
            original_name = os.path.splitext(filename)[0]

            original_path = os.path.join(
                output_class_dir,
                original_name + "_original.jpg"
            )

            image.save(original_path, quality=95)

            total_original += 1

            # Create and save augmented version
            augmented_image = augment_image(image)

            augmented_path = os.path.join(
                output_class_dir,
                original_name + "_augmented.jpg"
            )

            augmented_image.save(augmented_path, quality=95)

            total_augmented += 1

        except Exception as e:
            print(f"Error processing {input_path}: {e}")


print()
print("===================================")
print("AUGMENTATION COMPLETE")
print("===================================")
print(f"Original images copied: {total_original}")
print(f"Augmented images created: {total_augmented}")
print(f"Total images: {total_original + total_augmented}")
print()
print(f"Dataset saved to:")
print(os.path.abspath(OUTPUT_DIR))
