# Use XeLaTeX
$pdf_mode = 5;

# Set the XeLaTeX command with necessary flags
$xelatex = 'xelatex -file-line-error -halt-on-error -interaction=nonstopmode -synctex=1 -shell-escape -8bit %O %S';

# Set the output directory
$out_dir = './build';

# Required for minted v3 to find the build directory
$ENV{'TEXMF_OUTPUT_DIRECTORY'} = './build';