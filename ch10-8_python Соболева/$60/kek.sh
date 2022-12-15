yourfilenames=`ls ./*.py`
for eachfile in $yourfilenames
do
    iconv -f CP1251 -t UTF-8 $eachfile > $eachfile

    echo $eachfile
done
read -p "Enter some characters" string