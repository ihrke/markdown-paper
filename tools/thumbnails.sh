# create thumbnails from PDFs in pdf/ and store them in pics/
#
mkdir -p pics
for f in `ls pdf/`
do
    BASE="$(basename $f .pdf)"
    convert pdf/$f\[0\] -resize x400 -background white -flatten -shave 1x1 -bordercolor black -border 1 pics/$BASE.png
    echo "![$BASE](pics/$BASE.png)"
done;
