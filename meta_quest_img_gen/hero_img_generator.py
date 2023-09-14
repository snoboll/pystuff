from PIL import Image


def crop_to_aspect_single(
    input_path, output_path, target_width=3000, target_height=900
):
    img = Image.open(input_path)
    img_width, img_height = img.size
    img_aspect = img_width / img_height
    target_aspect = target_width / target_height

    crop_left = 0
    crop_upper = 0
    crop_right = img_width
    crop_lower = img_height

    if img_aspect > target_aspect:
        # Crop width
        new_width = int(img_height * target_aspect)
        offset = (img_width - new_width) // 2
        crop_left += offset
        crop_right -= offset
    elif img_aspect < target_aspect:
        # Crop height
        new_height = int(img_width / target_aspect)
        offset = (img_height - new_height) // 2
        crop_upper += offset
        crop_lower -= offset

    img_cropped = img.crop((crop_left, crop_upper, crop_right, crop_lower))
    img_resized = img_cropped.resize((target_width, target_height), Image.LANCZOS)
    img_resized.save(output_path, "PNG")


# Example usage
crop_to_aspect_single("hero_input.jpg", "hero_output.png")
