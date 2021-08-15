def hex_string_to_RGB(hex_string): 
    hex_string = hex_string.upper()
    hex = {'0': 0, '1': 1, '2': 2, '3': 3,
           '4': 4, '5':5, '6':6, '7':7,
           '8':8, '9':9, 'A': 10, 'B': 11,
           'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }
    # RED
    red = hex_string[1:3]
    r = hex[red[0]]*(16**1) + hex[red[1]]*(16**0)
    #
    green = hex_string[3:5]
    g = hex[green[0]]*(16**1) + hex[green[1]]*(16**0)
    #
    blue = hex_string[5:]
    b = hex[blue[0]]*(16**1) + hex[blue[1]]*(16**0)
    
    rgb = {
        'r':r,
        'g':g,
        'b':b,
    }
    return rgb
    
"""
HEX: 0 1 2 3 4 5 6 7 8 9 A B C D E F
    - base-16
    
"""

"""
When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:
  Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
  Returns a Map<String, int> with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
  Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")
    Example
      "#FF9933" --> {r: 255, g: 153, b: 51}
"""
