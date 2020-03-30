How to convert jupyter notebook to PDF file

1. Install LaTeX https://www.latex-project.org/get/

2. Export notebook to filename.tex 

3. If you have images to display: 

   Convert images to .ps (e.g. using online converters) and include them in the working directory

4. If you have images to display: 

   Edit filename.tex : find lines with names of the images and substitute them with the following line:
 	\includegraphics{filename} 

 	DO NOT include file extension!

5. Compile .tex to .dvi on command line:
latex filename.tex 

6. Convert .dvi to .pdf on command line:
dvipdfm file.dvi 
