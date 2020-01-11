# Build the images and push them to the local docker registry
cp /home/jenkins/.env /var/lib/jenkins/workspace/deploy-services/.env
docker-compose build
docker-compose push