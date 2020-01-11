# test server (service 1)
export $(xargs <.env)
pip3 install -r 1_server/requirements.txt
python3 -m pytest --cov=application 1_server/ --cov-report html:cov_html
ssh jenkins@bg-manager-node "mkdir -p /home/jenkins/test-reports/server/"
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/server/coverage.html
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/server/${BUILD_ID}.html
rm -r cov_html