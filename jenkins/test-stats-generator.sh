# test stats generator (service 3)
python -m pytest --cov=application . --cov-report html:cov_html
ssh jenkins@bg-manager-node "mkdir -p /home/jenkins/test-reports/stats_generator/"
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/stats_generator/coverage.html
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/stats_generator/$BULID_ID.html
rm -r cov_html