# test stats generator (service 3)
pip3 install -r 3_stats_generator/requirements.txt
python3 -m pytest --cov=application . --cov-report html:cov_html
ssh jenkins@bg-manager-node "mkdir -p /home/jenkins/test-reports/stats_generator/"
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/stats_generator/coverage.html
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/stats_generator/$BULID_ID.html
rm -r cov_html