# check error in parsing a file name or a function

from datetime import datetime


def get_string_range(char, rangenumber):
    try:
        if int(char) in list(range(*rangenumber)):
            return int(char)
    except:
        return None


def check_format_a(name):
    date_name_list = []
    year = get_string_range(name[:4], (2000, 2023))
    month = get_string_range(name[4:6], (1, 12))
    day = get_string_range(name[6:8], (1, 31))
    if year:
        date_name_list.append(year)
    if month:
        date_name_list.append(month)
    if day:
        date_name_list.append(day)
    if not year or not month or not day:
        return False
    return date_name_list


def check_format_b(img):
    exif = img._getexif()

    if not exif:
        return False
    if not exif.get(36867):
        return False

    exif_time = datetime.strptime(exif[36867], "%Y:%m:%d %H:%M:%S").timetuple()
    return [exif_time[0], exif_time[1], exif_time[2]]
