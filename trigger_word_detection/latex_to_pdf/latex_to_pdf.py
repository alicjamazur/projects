from PIL import Image
from glob import glob
import os
import re

def convert_images_to_ps():

	pngfiles = glob('*.png')

	for file in pngfiles:
		filename, ext = os.path.splitext(file)
		im = Image.open(file)
		im = im.convert('RGB')
		im.save(filename + '.eps')
		print('%s converted to %s' % (file, filename + '.eps'))

convert_images_to_ps()

print('\n Next steps: \n\n 1. Edit .tex file. Substitute \\adjustimage{*}} with \\includegraphics and delete file extension.')
print('\n 2. Run latex file.tex')
print('\n 3. Run dvipdfm file.dvi \n')