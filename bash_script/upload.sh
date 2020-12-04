# write data to excel and to github
dir="/Users/eason/Desktop/statistics/final-project"
echo "**************************************************" >> ${dir}/log/upload.log
now=$(date +"%x %X")
echo "current time: ${now}" >> ${dir}/log/upload.log
echo "writing data to excel..." >> ${dir}/log/upload.log
/opt/anaconda3/bin/python ${dir}/toExcel.py >> ${dir}/log/upload.log
echo "uploading data to github..." >> ${dir}/log/upload.log
git add .
git commit -m "upload data"
git push
echo "upload complete!!"
echo "**************************************************" >> ${dir}/log/upload.log
echo ""