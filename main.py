import matplotlib.image as mpl
import os
import sys
from colorthief import ColorThief



## Code from tux21b's awnser on https://stackoverflow.com/questions/2453344/find-the-colour-name-from-a-hexadecimal-colour-code/65074672#65074672 ##
import re
re_color = re.compile('#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})')
from math import sqrt

def color_to_rgb(color):
    return tuple(int(x, 16) / 255.0 for x in re_color.match(color).groups())

def similarity(color1, color2):
    """Computes the pearson correlation coefficient for two colors. The result
    will be between 1.0 (very similar) and -1.0 (no similarity)."""
    c1 = color_to_rgb(color1)
    c2 = color_to_rgb(color2)

    s1 = sum(c1)
    s2 = sum(c2)
    sp1 = sum(map(lambda c: pow(c, 2), c1))
    sp2 = sum(map(lambda c: pow(c, 2), c2))
    sp = sum(map(lambda x: x[0] * x[1], zip(c1, c2)))

    try:
        computed = (sp - (s1 * s2 / 3.0)) / sqrt((sp1 - pow(s1, 2) / 3.0) * (sp2 - pow(s2, 2) / 3.0))
    except:
        computed = 0
    
    return computed

color_names = {
    '#ff0000': 'red',
    '#00ff00': 'green',
    '#0000ff': 'blue',
    '#ffa500': 'orange',
    '#6a0dad': 'purple',
    '#ffff00': 'yellow'   
}

def find_name(color):
    sim = [(similarity(color, c), name) for c, name in color_names.items()]
    return max(sim, key=lambda x: x[0])[1]


## citation end ##

color_thief = ColorThief(sys.argv[1])
palette = color_thief.get_palette(color_count=4)


for item in palette:
    if not item[0]-item[1]/2-item[2]/2 in range (-10,10):
        color = item
        break
        
hex_color = '#{}{}{}'.format(
    hex(color[0]).split('x')[-1],
    hex(color[1]).split('x')[-1],
    hex(color[2]).split('x')[-1]
    )

if (find_name(hex_color)) == 'red':
    os.system("gsettings set org.gnome.desktop.interface cursor-theme 'LyraS-cursors'")
    os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Matcha-dark-aliz'")

elif (find_name(hex_color)) == 'green':
    os.system("gsettings set org.gnome.desktop.interface cursor-theme 'LyraX-cursors'")
    os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Matcha-dark-sea'")

elif (find_name(hex_color)) == 'blue':
    os.system("gsettings set org.gnome.desktop.interface cursor-theme 'LyraP-cursors'")
    os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Matcha-dark-azul'")

elif (find_name(hex_color)) == 'orange':
    os.system("gsettings set org.gnome.desktop.interface cursor-theme 'LyraG-cursors'")
    os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Matcha-dark-azul'")

elif (find_name(hex_color)) == 'purple':
    os.system("gsettings set org.gnome.desktop.interface cursor-theme 'LyraR-cursors'")
    os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Matcha-dark-azul'")

elif (find_name(hex_color)) == 'yellow':
    os.system("gsettings set org.gnome.desktop.interface cursor-theme 'LyraY-cursors'")
    os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Matcha-dark-azul'")

os.system("wal -i {}".format(sys.argv[1]))

