import argparse
import wgenpatex
import os 

parser = argparse.ArgumentParser()
parser.add_argument('target_image_path', help='paths of target texture image')
parser.add_argument('out_dir', help='directory to save the generated texture image')
parser.add_argument('-s', '--size', default=None, help="size of synthetized texture [nrow, ncol] (default: target texture size)")
parser.add_argument('-w', '--patch_size', type=int,default=4, help="patch size (default: 4)")
parser.add_argument('-nmax', '--n_iter_max', type=int, default=500, help="max iterations of the algorithm(default: 500)")
parser.add_argument('-npsi', '--n_iter_psi', type=int, default=10, help="max iterations for psi (default: 10)")
parser.add_argument('-nin', '--n_patches_in', type=int, default=-1, help="number of patches of the synthetized texture used at each iteration, -1 corresponds to all patches (default: -1)")
parser.add_argument('-nout', '--n_patches_out', type=int, default=2000, help="number maximum of patches of the target texture used, -1 corresponds to all patches (default: 2000)")
parser.add_argument('-sc', '--scales', type=int, default=4, help="number of scales used (default: 4)")
parser.add_argument('--visu',  action='store_true', help='show intermediate results')
parser.add_argument('--save',  action='store_true', help='save temp results in /tmp folder')
parser.add_argument('--keops', action='store_true', help='use keops package')
args = parser.parse_args()

synth_img = wgenpatex.optim_synthesis(args)

save_file = f'synth_{args.target_image_path}'

# plot and save the synthesized texture 
# wgenpatex.imshow(synth_img)

filename = os.path.basename(args.target_image_path)
filename_no_ext = os.path.splitext(filename)[0]

wgenpatex.imsave(os.path.join(args.out_dir,f'{filename_no_ext}.png'), synth_img)
