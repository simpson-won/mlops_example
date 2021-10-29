# mlops_example

### Description
This is an example source for a simple mlops flow implementation.
It includes the following features:
- Upload data
- Data preprocessing
- Detire modeling and testing and distribution
- New data prediction

You can do a simple test through the Makefile in the root folder.

### To Run:

make run-data       : data implements
make run-preprocess : data process
make run-train      : data trainning
make run-api        : data prediction, run flask app to predict through web apps.


### Execution Flow :

1) run-data
2) run-preprocess
3) run-train
4) run-api


### pre-request
1) install file-api-server
  used "mayth/simple-upload-server"  
2) install ftp server
  used vsftpd
3) install jenkins
  https://www.jenkins.io/doc/book/installing/
4) install docker 
  for docker-registry : https://docs.docker.com/registry/
  for docker-client : https://docs.docker.com/get-docker/
5) install kubernetes
  refer any site
6) install mlflow-server in kubernetes
  run docker/server
