yourfilenames=`ls -v ./Task*.py`
i=1
for file in $yourfilenames
do
    new_file=./$i.py
    mv $file $new_file

    echo $file
    echo $new_file
    i=$((i+1))
done
read -p "Enter some characters" string