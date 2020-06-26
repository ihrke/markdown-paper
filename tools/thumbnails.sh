# create thumbnails from PDFs in pdf/ and store them in pics/
#
mkdir -p pics
for f in `ls pdf/`
do
    BASE="$(basename $f .pdf)"
    convert pdf/$f\[0\] -resize 75% pics/$BASE.png
    echo "![$BASE](pics/$BASE.png)"
done;
