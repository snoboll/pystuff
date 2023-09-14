from PIL import Image


def crop_and_resize(input_path, output_path, target_size=512):
    img = Image.open(input_path)
    width, height = img.size

    # Calculate dimensions to crop to target aspect ratio
    new_dim = min(width, height)

    left = (width - new_dim) / 2
    upper = (height - new_dim) / 2
    right = left + new_dim
    lower = upper + new_dim

    img_cropped = img.crop((left, upper, right, lower))

    # Resize to 512x512
    img_resized = img_cropped.resize((target_size, target_size), Image.LANCZOS)

    # Save the image as PNG
    img_resized.save(output_path, "PNG")


# Example usage
crop_and_resize("input_image.png", "output_image.png")
