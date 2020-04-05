#!/bin/bash

# Step 1: convert images .png to .eps
echo 'Converting images to .eps'
for i in *.png;
do
	convert "$i" "${i%.png}.eps";
done


# Step 2: delete .png extension from .tex file
echo 'Deleting .png extensions from tex file'
sed -i bak 's/.png//g' *.tex


# Step 3: replace adjustimage{.*}} with includegraphics
echo 'Editing tex file to include graphics'
sed -i bak 's/adjustimage{.*}}/includegraphics/g' *.tex

# # Step 4: convert .tex file to .dvi 
echo 'Converting .tex to .dvi '
latex *.tex

# # Step 5: convert .dvi to .pdf
echo 'Converting .dvi to .pdf'
dvipdfm *.dvi