import argparse
import wgenpatex
import os

parser = argparse.ArgumentParser()
parser.add_argument('target_image_dir', help='path of target texture directory')

args = parser.parse_args()

dir = args.target_image_dir 
out_dir = "./out"

for path in os.listdir(dir):
    texture_path = os.path.join(dir,path)
    os.system(f"python run_optim_synthesis.py {texture_path} {out_dir}")