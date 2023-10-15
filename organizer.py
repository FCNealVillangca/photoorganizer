import os
from checkfilename import *
from PIL import Image


source = os.path.abspath(os.path.join(os.getcwd(), "source"))
destination = os.path.abspath(os.path.join(os.getcwd(), "destination"))
directory_files = os.listdir(source)
firstfile = os.listdir(source)[0]


def organize_file(src, name, dest):
    try:
        img = Image.open(os.path.join(src, name))
        if bool(check_format_a(name)):
            print(bool(check_format_a(name)))
            name_array = check_format_a(name)
            file_transfer_process(name, name_array, img, dest)

        elif check_format_b(img):
            name_array = check_format_b(img)
            file_transfer_process(name, name_array, img, dest)
        else:
            file_transfer(name, img, dest)
    except Exception as exc:
        print(exc)


def file_transfer_process(name, name_array, img, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

    new_dir_name = dest + f"\{name_array[0]:02}-{name_array[1]:02}-{name_array[2]:02}"
    if not os.path.exists(new_dir_name):
        os.makedirs(new_dir_name)

    new_image = resize_img(img)
    new_image.save(os.path.join(new_dir_name, name), exif=new_image.getexif())


def file_transfer(name, img, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    if not os.path.exists(dest + "\_unsorted"):
        os.makedirs(dest + "\_unsorted")

    new_image = resize_img(img)
    new_image.save(dest + "\_unsorted" + f"\{name}", exif=new_image.getexif())


def resize_img(img):
    width, height = img.size
    if width > 2048 or height > 2048:
        img.thumbnail((2048, 2048))
    return img


def main(src, name, dest):
    image_format = ["png", "PNG", "jpg", "jpeg", "JPG"]
    ext = name.split(".")[-1]
    if ext in image_format:
        organize_file(src, name, dest)


def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


progress_bar(0, len(directory_files))
for i, name in enumerate(directory_files):
    main(source, name, destination)
    progress_bar(i + 1, len(directory_files))
