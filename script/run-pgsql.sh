echo "running uniform experient"
stdbuf -oL python run-jmeter.py rest_api_get_uniform.jmx 30 hnode07 8081 pgsql uniform > exp_pgsql_uniform.log

echo "running gaussian experient"
stdbuf -oL python run-jmeter.py rest_api_get_gaussian.jmx 30 hnode07 8081 pgsql gaussian > exp_pgsql_gaussian.log
