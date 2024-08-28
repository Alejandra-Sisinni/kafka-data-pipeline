# kafka-data-pipeline
Steps Google Cloud Console (https://console.cloud.google.com/)
1. Activate APIs --> Go to Menu --> APIs and Services --> APIs and Services enabled --> Enable the Compute Engine API and Dataflow API
2. Create Service Account --> Menu --> IAM and Admin --> Service Account --> Add name, ID, description --> Create and Continue --> Rol "Product Owner"
3. Create a key for the account --> Manage keys --> Add Key --> Create new Key
4. Activate Cloud Shell to develop data transformation apps

Setting Up Kafka
1. Install Docker - https://www.docker.com/products/docker-desktop
2. Powershell - cd Kafka-Project 
3. docker-compose -f kafka-single-node.yml up -d
4. docker ps
5. To shut down and remove setup: docker-compose -f kafka-single-node.yml down