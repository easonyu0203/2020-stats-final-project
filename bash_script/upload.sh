# write data to excel and to github
dir="/Users/eason/Desktop/statistics/final-project"
echo "**************************************************"
now=$(date +"%x %X")
echo "current time: ${now}"
echo "writing data to excel..."
/opt/anaconda3/bin/python ${dir}/toExcel.py
echo "uploading data to github..."
git add .
git commit -m "upload data"
git push
echo "**************************************************"
