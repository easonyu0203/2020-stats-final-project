dir="/Users/eason/Desktop/statistics/final-project"
now=$(date +"%x %X")
# run web crawling python script!!!!!
echo "===================================================================" >> ${dir}/result.txt
echo "web crawling program running..." >> ${dir}/result.txt
echo "current time: ${now}" >> ${dir}/result.txt
/opt/anaconda3/bin/python ${dir}/web_crawler.py >> ${dir}/result.txt
echo "===================================================================" >> ${dir}/result.txt
echo "" >> ${dir}/result.txt
