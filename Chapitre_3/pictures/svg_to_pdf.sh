for afile in *.svg ; do
  afile_png=${afile/.svg/.png}
  afile_pdf=${afile/.svg/.pdf}
  if [ ! -e $afile_pdf ] ; then
    inkscape --file=$afile --export-area-drawing --without-gui --export-pdf=$afile_pdf
    echo "Created $afile_pdf"
    if [ -e $afile_png ] ; then
      rm $afile_png
      echo "Removed $afile_png"
    fi
  fi
done
