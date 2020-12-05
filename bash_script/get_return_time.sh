dir="/Users/eason/Desktop/statistics/final-project"
now=$(date +"%x %X")
cd ${dir}

echo "===================================================================" >> ${dir}/log/get_return_time.log
echo "web crawling program running..." >> ${dir}/log/get_return_time.log
echo "current time: ${now}" >> ${dir}/log/get_return_time.log
/opt/anaconda3/bin/python ${dir}/get_return_time.py >> ${dir}/log/get_return_time.log
echo "===================================================================" >> ${dir}/log/get_return_time.log
echo "" >> ${dir}/log/get_return_time.log
