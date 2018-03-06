echo "running uniform experient"
stdbuf -oL python run-jmeter.py rest_api_get_uniform.jmx 30 hnode07 8081 mongo uniform > exp_mongo_uniform.log

echo "running gaussian experient"
stdbuf -oL python run-jmeter.py rest_api_get_gaussian.jmx 30 hnode07 8081 mongo gaussian > exp_mongo_gaussian.log
