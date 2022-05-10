#Download the original text (result stored in ./original-text/lxxmorph
./bin/downloadRawText.sh
#Convert this to imp (result stored in ./imp)
./bin/convertToImp.sh
#Convert in xml (stored in ./xml 
./bin/convertToXml.sh
#Fix some xml issues and re order books (stored in ./clean)
./bin/fixXml.sh
#Generate html files
rm -rf html
mkdir html
for i in `ls clean` ; do
  echo $i;
  ./bin/create-html.py clean/$i html
done

./bin/create-toc.py clean/* html

cp templates/Foreword.html html/02-Foreword.html
