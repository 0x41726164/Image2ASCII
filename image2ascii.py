import argparse
from PIL import Image

# HANDLING ARGUMENT SWITCHES
parser = argparse.ArgumentParser(description="Turn Images Into Ascii Art")
parser.add_argument(
    "--img",
    type=str,
    default="image.png",
    help="Path To Image File")
parser.add_argument(
    "--dim",
    default=20,
    type=int,
    help="dimnesion is divided by this value; e.g. 100x100 --dim 2 -> 50x50")
parser.add_argument(
    "--dob",
    type=int,
    choices=[0,1],
    default=0,
    help="0 If Image is Dark, 1 If Image is Bright")
parser.add_argument(
    "--lod",
    type=int,
    choices=[0,1,2],
    default=1,
    help="0 for Minimalism, 2 for Maximalism")
args = parser.parse_args()

# ACCESSING IMAGE INFO
image = Image.open(args.img)
width, height = image.size

# RESIZING THE IMAGE
newsize = (width//args.dim,height//args.dim)
image = image.resize(newsize)

# CONVERT TO GRAYSCALE (FOR BRIGHTNESS VALUES)
grayscale_image = image.convert("L")
width, height = grayscale_image.size

# LEVEL OF DETAIL / DENSITY (DENSITY IS A SET OF CHARACTERS IN ORDER OF BRIGHTEST TO DARKEST)
if args.lod == 0:
    density = 'N@#$;:+=-.     '
elif args.lod == 1:
    density = 'N@#W$;:+=-,._  '
elif args.lod == 2:
    density = 'N@#W$987654321?!abc;:+=-,._ '

# DARK OR BRIGHT SELECTION
if args.dob == 1:
    density = density[::-1]

# MAP BRIGHTNESS VALUES TO DENSITY CHARACTERS
def get_ascii_char(brightness):
    # index = int(brightness / (255 / len(density)))
    index = int(brightness/(255/(len(density)-1)))
    return density[index]

# MAIN LOOP
for y in range(height):
    for x in range(width):
        brt = grayscale_image.getpixel((x,y))
        print(get_ascii_char(brt),end=' ')
    print(end="\n")
