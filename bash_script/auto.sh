# run web crawling python script!!!!!
dir="/Users/eason/Desktop/statistics/final-project"
echo "auto web crawling..." >> ${dir}/result.txt
now=$(date +"%x %X")
echo "current time: ${now}" >> ${dir}/result.txt
/opt/anaconda3/bin/python ${dir}/web_crawler.py
echo "" >> ${dir}/result.txt

