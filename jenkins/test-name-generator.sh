# test name generator (service 2)
ssh jenkins@bg-manager-node "mkdir -p /home/jenkins/test-reports/name_generator/"
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/name_generator/coverage.html
scp cov_html/index.html jenkins@bg-manager-node:/home/jenkins/test-reports/name_generator/${BUILD_ID}.html
rm -r cov_html