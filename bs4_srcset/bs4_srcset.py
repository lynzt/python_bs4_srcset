def get_img_url_from_srcset(img_element, size_wanted):
    if img_element == '':
        return None
    min_size_wanted = _get_min_size_wanted(size_wanted)
    max_size_wanted = _get_max_size_wanted(size_wanted)

    srcsets = img_element.split(',')
    # for size_wanted in size_wanted_arr: # will return first one found in sizewanted_arr
    for srcset in srcsets:
        img_url, img_size = srcset.strip().split(' ', 2)
        img_size = _convert_size_to_float(img_size)
        if img_size >= min_size_wanted and img_size <= max_size_wanted:
            return img_url

def _convert_size_to_float(size_str):
    size = size_str[:-1] # remove x|w at end
    return float(size)

def _get_min_size_wanted(size_wanted):
    if 'min' in size_wanted:
        return size_wanted['min']
    else:
        return 0

def _get_max_size_wanted(size_wanted):
    if 'max' in size_wanted:
        return size_wanted['max']
    else:
        return 2000