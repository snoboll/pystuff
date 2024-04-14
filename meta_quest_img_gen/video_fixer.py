from moviepy.editor import VideoFileClip


def crop_video_to_aspect(input_video_path, output_video_path):
    clip = VideoFileClip(input_video_path)
    width, height = clip.size

    target_aspect_ratio = 16 / 9
    target_width = 1280
    target_height = 720

    video_aspect_ratio = width / height

    crop_left = 0
    crop_right = width
    crop_top = 0
    crop_bottom = height

    if video_aspect_ratio > target_aspect_ratio:
        # Crop width
        new_width = int(height * target_aspect_ratio)
        offset = (width - new_width) // 2
        crop_left += offset
        crop_right -= offset
    elif video_aspect_ratio < target_aspect_ratio:
        # Crop height
        new_height = int(width / target_aspect_ratio)
        offset = (height - new_height) // 2
        crop_top += offset
        crop_bottom -= offset

    cropped_clip = clip.crop(x1=crop_left, y1=crop_top, x2=crop_right, y2=crop_bottom)

    # Ensure minimum dimensions
    if cropped_clip.size[0] < target_width or cropped_clip.size[1] < target_height:
        cropped_clip = cropped_clip.resize(newsize=(target_width, target_height))

    cropped_clip.write_videofile(
        output_video_path,
        codec="libx264",
        audio_codec="aac",
        fps=24,
        threads=4,
        ffmpeg_params=["-strict", "experimental"],
    )


# Example usage
crop_video_to_aspect("input_video.mp4", "output_video.mp4")
