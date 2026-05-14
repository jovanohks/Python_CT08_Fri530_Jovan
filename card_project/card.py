# =========================
# IMPORT LIBRARIES
# =========================
#
# These libraries give Python extra abilities.
#
# PIL:
# Used to create images, draw shapes,
# draw text, and load fonts/images.
#
# imageio:
# Used to turn all frames into a video.
#
# numpy:
# Used to convert images into video frames.
#
# math:
# Used for animation effects like
# spinning, pulsing, and wave movement.

from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio
import numpy as np
import math


# =========================
# CANVAS SETTINGS
# =========================
#
# WIDTH:
# Width of the video canvas.
#
# HEIGHT:
# Height of the video canvas.
#
# Bigger WIDTH or HEIGHT creates
# a bigger video.

WIDTH = 608
HEIGHT = 512


# =========================
# VIDEO SETTINGS
# =========================
#
# FRAMES:
# Total number of frames/images created.
#
# FPS:
# Frames shown per second.
#
# Video length = FRAMES / FPS
#
# Example:
# 150 / 30 = 5 seconds.

FRAMES = 150
FPS = 30


# =========================
# STUDENT SETTINGS
# =========================
#
# These values are used to create
# the output video file name.

CLASS = "CT08"
DAY = "THU"
TIME = "1915"
STUDENT_NAME = "Jovan"


# =========================
# PROJECT FOLDER
# =========================
#
# This is the main project folder.
#
# Expected structure:
#
# card_project/
# ├── asset/
# │   ├── image/
# │   └── font/
# └── main.py

FOLDER_NAME = "card_project"


# =========================
# MESSAGE IMAGE SETTINGS
# =========================
#
# These images appear beside the sliding message.
#
# FRONT image:
# Appears before the message.
#
# BACK image:
# Appears after the message.
#
# Use "" if you do not want an image.

MESSAGE_ASSET_FRONT_FILE = "heart.png"
MESSAGE_ASSET_BACK_FILE = "heart.png"


# =========================
# FLOATING IMAGE SETTINGS
# =========================
#
# This image is used for the
# floating background animation.

FLOATING_ASSET_FILE = "ballon_three.png"


# =========================
# FONT FILE SETTINGS
# =========================
#
# These are the font files used
# for the text.
#
# Make sure they are inside:
# card_project/asset/font

MESSAGE_FONT_FILE = "Roboto-Regular.ttf"
SUBMESSAGE_FONT_FILE = "Roboto-Regular.ttf"


# =========================
# FONT SIZE SETTINGS
# =========================
#
# MESSAGE_FONT_SIZE:
# Bigger = larger main message.
#
# SUBMESSAGE_FONT_SIZE:
# Bigger = larger subtitle message.

MESSAGE_FONT_SIZE = 50
SUBMESSAGE_FONT_SIZE = 25


# =========================
# TEXT SETTINGS
# =========================
#
# message:
# Main sliding message.
#
# sub_message:
# Smaller message shown below.
#
# You can change the words inside
# the quotation marks.

message = "Happy Mother's Day"

sub_message = "Thank you for always supporting me \nand believing in me every single day!"

# =========================
# FILE PATHS
# =========================

image_dir = f"{FOLDER_NAME}/asset/image"

floating_asset_fullpath = f"{image_dir}/{FLOATING_ASSET_FILE}"

image_file_name = (
    f"{FOLDER_NAME}/"
    f"{CLASS}_{DAY}_{TIME}_{STUDENT_NAME}_mothers_day_animation.mp4"
)

frames = []

# =========================
# LOAD FONTS
# =========================
font_dir = f"{FOLDER_NAME}/asset/font"
font_big_file = f"{font_dir}/{MESSAGE_FONT_FILE}"
font_small_file = f"{font_dir}/{SUBMESSAGE_FONT_FILE}"

font_big = ImageFont.truetype(
    font_big_file,
    MESSAGE_FONT_SIZE
)

font_small = ImageFont.truetype(
    font_small_file,
    SUBMESSAGE_FONT_SIZE
)

# =========================
# LOAD FLOATING ASSET
# =========================

floating_asset_img = Image.open(
    floating_asset_fullpath
).convert("RGBA")

# Change (40, 40) to resize floating image.
# Example:
# (20, 20) = smaller
# (80, 80) = bigger
floating_asset_img = floating_asset_img.resize((40, 40))

# =========================
# LOAD MESSAGE ASSETS
# =========================

message_asset_front_img = ""
message_asset_back_img = ""

# FRONT image appears before the message.
if MESSAGE_ASSET_FRONT_FILE != "":

    message_asset_front_fullpath = (
        f"{image_dir}/{MESSAGE_ASSET_FRONT_FILE}"
    )

    message_asset_front_img = Image.open(
        message_asset_front_fullpath
    ).convert("RGBA")

    message_asset_front_img = (
        message_asset_front_img.resize((MESSAGE_FONT_SIZE, MESSAGE_FONT_SIZE))
    )

# BACK image appears after the message.
if MESSAGE_ASSET_BACK_FILE != "":

    message_asset_back_fullpath = (
        f"{image_dir}/{MESSAGE_ASSET_BACK_FILE}"
    )

    message_asset_back_img = Image.open(
        message_asset_back_fullpath
    ).convert("RGBA")

    message_asset_back_img = (
        message_asset_front_img.resize((MESSAGE_FONT_SIZE, MESSAGE_FONT_SIZE))
    )

# BACK image appears after the message.
if MESSAGE_ASSET_BACK_FILE != "":

    message_asset_back_fullpath = (
        f"{image_dir}/{MESSAGE_ASSET_BACK_FILE}"
    )

    message_asset_back_img = Image.open(
        message_asset_back_fullpath
    ).convert("RGBA")

    message_asset_back_img = (
        message_asset_front_img.resize((MESSAGE_FONT_SIZE, MESSAGE_FONT_SIZE))
    )


def draw_floating_assets(
    img,
    frame,
    diagonal_lines=1
):

    number_of_assets = 12
    spacing = 45
    speed = 4

    # This is the full vertical looping distance.
    # The extra 200 gives space before the image reappears.
    loop_height = HEIGHT + 200

    # This makes every diagonal line equally spaced,
    # including when it disappears at the top
    # and reappears from the bottom.
    line_gap = loop_height // diagonal_lines

    for line in range(diagonal_lines):

        for i in range(number_of_assets):

            x = 50 + i * spacing

            y = HEIGHT - (
                (
                    frame * speed
                    + i * 25
                    + line * line_gap
                )
                % loop_height
            )

            img.paste(
                floating_asset_img,
                (x, y),
                floating_asset_img
            )


def draw_waterfall(draw, frame):

    # =========================
    # WATERFALL EFFECT
    # =========================
    #
    # This function draws falling blue lines.
    #
    # SAFE THINGS TO CHANGE:
    #
    # range(40):
    # More = more water streams
    # Less = fewer water streams
    #
    # i * 17:
    # Controls horizontal spacing
    #
    # frame * 8:
    # Larger = faster falling water
    # Smaller = slower falling water
    #
    # width=3:
    # Larger = thicker water
    # Smaller = thinner water

    for i in range(40):

        x = (i * 17) % WIDTH
        y = (frame * 8 + i * 30) % HEIGHT

        draw.line(
            (x, y, x, y + 35),
            fill="#7dd3fc",
            width=3
        )

        draw.ellipse(
            (x - 3, y + 35, x + 3, y + 41),
            fill="#bae6fd"
        )


def draw_sparkles(draw, frame):

    # =========================
    # SPARKLE EFFECT
    # =========================
    #
    # This function draws blinking sparkles.
    #
    # SAFE THINGS TO CHANGE:
    #
    # range(20):
    # More = more sparkles
    # Less = fewer sparkles
    #
    # frame * 0.3:
    # Larger = faster blinking
    # Smaller = slower blinking
    #
    # "*":
    # Try "+", "x"

    for i in range(20):

        x = (i * 73) % WIDTH
        y = (i * 41) % HEIGHT

        brightness = int(
            150 + 100 * math.sin(frame * 0.3 + i)
        )

        color = (255, brightness, brightness)

        draw.text(
            (x, y),
            "*",
            fill=color,
            font=font_small
        )




def draw_sliding_message(img, draw, frame):

    # =========================
    # SLIDING MESSAGE
    # =========================
    #
    # This function makes the main message
    # slide from right to left.
    #
    # SAFE THINGS TO CHANGE:
    #
    # gap:
    # Space between message and image
    #
    # text_y:
    # Larger = message moves lower
    # Smaller = message moves higher
    #
    # start_x:
    # Larger = starts further outside right
    #
    # end_x:
    # Smaller = moves further outside left

    gap = 10
    text_y = 100

    text_bbox = draw.textbbox(
        (0, 0),
        message,
        font=font_big
    )

    text_width = text_bbox[2] - text_bbox[0]

    total_width = text_width

    if message_asset_front_img != "":
        total_width += message_asset_front_img.width + gap

    if message_asset_back_img != "":
        total_width += message_asset_back_img.width + gap

    progress = frame / FRAMES

    start_x = WIDTH + 100
    end_x = -total_width - 100

    text_x = int(
        start_x + progress * (end_x - start_x)
    )

    draw.text(
        (text_x, text_y),
        message,
        fill="#7a1f44",
        font=font_big
    )

    asset_y = text_y + 8

    # FRONT image appears before the message.
    if message_asset_front_img != "":

        front_x = (
            text_x
            - message_asset_front_img.width
            - gap
        )

        img.paste(
            message_asset_front_img,
            (front_x, asset_y),
            message_asset_front_img
        )

    # BACK image appears after the message.
    if message_asset_back_img != "":

        back_x = (
            text_x
            + text_width
            + gap
        )

        img.paste(
            message_asset_back_img,
            (back_x, asset_y),
            message_asset_back_img
        )


def draw_rotating_pulsing_flower(
    draw,
    frame,
    center_x,
    center_y,
    flower_size,
    center_size
):

    # =========================
    # ROTATING PULSING FLOWER
    # =========================
    #
    # This function draws one flower.
    #
    # PARAMETERS STUDENTS CAN CHANGE:
    #
    # center_x:
    # Horizontal position of flower
    #
    # center_y:
    # Vertical position of flower
    #
    # flower_size:
    # Size of each petal
    #
    # center_size:
    # Size of the middle circle
    #
    # SAFE THINGS TO CHANGE:
    #
    # frame * 0.2:
    # Larger = faster pulsing
    # Smaller = slower pulsing
    #
    # frame * 5:
    # Larger = faster spinning
    # Smaller = slower spinning
    #
    # range(0, 360, 45):
    # 45 = 8 petals
    # 30 = 12 petals
    # 60 = 6 petals

    base_distance = flower_size * 2

    size = base_distance + int(
        flower_size * 0.6
        * math.sin(frame * 0.2)
    )

    rotation = frame * 5

    for angle in range(0, 360, 45):

        rad = math.radians(
            angle + rotation
        )

        x = center_x + int(
            math.cos(rad) * size
        )

        y = center_y + int(
            math.sin(rad) * size
        )

        draw.ellipse(
            (
                x - flower_size,
                y - flower_size,
                x + flower_size,
                y + flower_size
            ),
            fill="#ff8fab"
        )

    draw.ellipse(
        (
            center_x - center_size,
            center_y - center_size,
            center_x + center_size,
            center_y + center_size
        ),
        fill="#ffd166"
    )


def draw_subtitle(draw, frame):

    if frame > 45:

        max_width = WIDTH - 80
        start_y = 300
        line_spacing = 32

        lines = []

        # Check if student added "\n"
        if "\n" in sub_message:

            manual_lines = sub_message.split("\n")

        else:

            manual_lines = [sub_message]

        # Process every manual line
        for manual_line in manual_lines:

            words = manual_line.split()

            current_line = ""

            for word in words:

                test_line = current_line + word + " "

                test_bbox = draw.textbbox(
                    (0, 0),
                    test_line,
                    font=font_small
                )

                test_width = (
                    test_bbox[2] - test_bbox[0]
                )

                if test_width <= max_width:

                    current_line = test_line

                else:

                    lines.append(
                        current_line.strip()
                    )

                    current_line = word + " "

            # VERY IMPORTANT
            # Append final remaining line
            lines.append(
                current_line.strip()
            )

        # Draw all lines
        for i in range(len(lines)):

            line = lines[i]

            line_bbox = draw.textbbox(
                (0, 0),
                line,
                font=font_small
            )

            line_width = (
                line_bbox[2] - line_bbox[0]
            )

            line_x = (
                WIDTH // 2
                - line_width // 2
            )

            line_y = (
                start_y
                + i * line_spacing
            )

            draw.text(
                (line_x, line_y),
                line,
                fill="#5c2a3d",
                font=font_small
            )


# =========================
# CREATE EACH FRAME
# =========================
#
# This loop creates one image at a time.
# Each image becomes one frame of the video.
#
# The order matters:
# Things drawn earlier appear behind.
# Things drawn later appear in front.

for frame in range(FRAMES):

    img = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "#ffd6e8"
    )

    draw = ImageDraw.Draw(img)

    draw_waterfall(draw, frame)
    draw_floating_assets(img, frame)
    draw_sparkles(draw, frame)

    draw_sliding_message(img, draw, frame)

    draw_rotating_pulsing_flower(
        draw,
        frame,
        WIDTH // 2,
        230,
        18,
        12
    )

    draw_subtitle(draw, frame)

    frames.append(np.array(img))


# =========================
# SAVE VIDEO
# =========================

writer = imageio.get_writer(
    image_file_name,
    fps=FPS
)

for frame in frames:
    writer.append_data(frame)

writer.close()

print(f"MP4 created: {image_file_name}")