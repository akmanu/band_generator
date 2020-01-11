# Build the images and push them to the local docker registry
cp /home/jenkins/.env /var/lib/jenkins/workspace/staging/.env
docker-compose build
docker-compose push