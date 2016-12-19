def get_img_url_from_srcset(img_element, size_wanted):
    srcsets = img_element.split(',')
    for srcset in srcsets:
        img_url, size = srcset.strip().split(' ', 2)
        if size == size_wanted:
            return img_url
