# write data to excel and to github
dir="/Users/eason/Desktop/statistics/final-project"
dir="/Users/eason/Desktop/statistics/final-project"
echo "**************************************************" >> ${dir}/result.txt
now=$(date +"%x %X")
echo "current time: ${now}" >> ${dir}/result.txt
echo "writing data to excel..." >> ${dir}/result.txt
/opt/anaconda3/bin/python ${dir}/toExcel.py >> ${dir}/result.txt
echo "uploading data to github..." >> ${dir}/result.txt
git add .
git commit -m "upload data"
git push
echo "**************************************************" >> ${dir}/result.txt
echo ""