dir="/Users/eason/Desktop/statistics/final-project"
now=$(date +"%x %X")
# run web crawling python script!!!!!
echo "===================================================================" >> ${dir}/log/crawling.log
echo "web crawling program running..." >> ${dir}/log/crawling.log
echo "current time: ${now}" >> ${dir}/log/crawling.log
/opt/anaconda3/bin/python ${dir}/web_crawler.py >> ${dir}/log/crawling.log
echo "===================================================================" >> ${dir}/log/crawling.log
echo "" >> ${dir}/log/crawling.log
