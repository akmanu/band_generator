# test name generator (service 2)
export $(xargs <.env)
pip3 install -r 2_name_generator/requirements.txt
python3 -m pytest --cov=application 2_name_generator/ --cov-report html:cov_html
ssh jenkins@bg-manager-node "mkdir -p /home/jenkins/test-reports/name_generator/"
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/name_generator/coverage.html
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/name_generator/${BUILD_ID}.html
rm -r cov_html