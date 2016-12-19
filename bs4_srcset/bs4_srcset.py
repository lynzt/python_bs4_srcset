def get_img_url_from_srcset(img_element, size_wanted_arr):
    if img_element == '':
        return None
    
    srcsets = img_element.split(',')
    for size_wanted in size_wanted_arr: # will return first one found in sizewanted_arr
        for srcset in srcsets:
            img_url, img_size = srcset.strip().split(' ', 2)
            if img_size == size_wanted:
                return img_url
