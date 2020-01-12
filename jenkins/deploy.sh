# Copy docker-compose.yaml to the manager node so that it can deploy
scp docker-compose.yaml jenkins@bg-manager-node:/home/jenkins/

# Deploy on the manager node
ssh bg-manager-node 'export BUILD_ID=$BUILD_ID'
ssh bg-manager-node 'docker stack deploy --compose-file docker-compose.yaml band_generator'
