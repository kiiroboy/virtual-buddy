import glob
from PIL import Image, ImageOps
import os
dir = os.getcwd()
character_folder = "Xiao"
fp_in = dir + "/" + character_folder
fp_out = dir + "/GIF/" + character_folder.lower() + "_energy.gif"
walking_dir = fp_in + "/mask_energy/shime*.png"
img, *imgs = [ImageOps.mirror(Image.open(f)) for f in sorted(glob.glob(walking_dir))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)
print(fp_out)