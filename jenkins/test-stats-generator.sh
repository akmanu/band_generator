# test stats generator (service 3)
export $(xargs <.env)
pip3 install -r 3_stats_generator/requirements.txt
python3 -m pytest --cov=application 3_stats_generator/ --cov-report html:cov_html
ssh jenkins@bg-manager-node "mkdir -p /home/jenkins/test-reports/stats_generator/"
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/stats_generator/coverage.html
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/stats_generator/$BUILD_ID.html
rm -r cov_html