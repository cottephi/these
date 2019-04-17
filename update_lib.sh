if [ -e bibli.bib ] ; then
  rm bibli.bib
  echo "Removed previous link to bibli.bib"
fi
ln ~/Documents/JabRef/bibli.bib bibli.bib
echo "Created new link to bibli.bib"
