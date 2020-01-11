# test members generator (service 1)
pytest --cov=flask_app . --cov-report html:cov_html
ssh jenkins@bg-manager-node "mkdir -p /home/jenkins/test-reports/members_generator/"
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/members_generator/coverage.html
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/members_generator/$BULID_ID.html
rm -r cov_html