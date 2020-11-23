def find_screen_height(width, ratio): 
    ratio = ratio.split(":")
    height = int(width * (int(ratio[1])/int(ratio[0])))
    return (str(width)+"x"+str(height))


"""
Find height given width & aspect-ratio.
"""
