# test server (service 1)
pytest --cov=flask_app . --cov-report html:cov_html
ssh jenkins@bg-manager-node "mkdir -p /home/jenkins/test-reports/server/"
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/server/coverage.html
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/server/$BULID_ID.html
rm -r cov_html