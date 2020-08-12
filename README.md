# EnhanceIt
A containerized API service that will **enhance** an image for you with the help of image super-resolution(SR). 

**🚧 Unfortunately, this project has become a failed attempt due to memory limits on serverless solutions and the memory intensive nature of neural networks. However, you can still run the containerized application in a server with more than 4GB of memory at the cost of losing all the benefits of serverless technology. 🚧**

## Highlights
* Highly cost-effective. Image super-resolution is a very time-intensive and resource-intensive task. The API can run on Kubernetes so that running a powerful yet expensive server is not required. Furthermore, the API taps into serverless technologies so that zero cost will be incurred when idling.

* Very responsive. Kubernetes automatically launch new containers so that one user will not steal resources from another user.

## Challenges
* Up until this moment (Aug 2020), no cloud computing service offers containerized serverless solutions with the support of GPU or TPU. And there is a very low limit set on how much CPU resource can be consumed by each container. Therefore, you can expect processing to be fairly slow for very large images.

## Prerequisites
* A Google Cloud Platform account

## Architecture
1. Users send requests providing an image url

2. Cloud run starts the built container

3. Requests are handled by a python server

4. Python downloads the image with the provided url

5. Image super-resolution algorithm is started to generate the enhanced image

6. The enhanced image is stored temporarily in a Cloud Storage bucket (image will be automatically deleted after some time as configured)

7. The url of the stored image is returned to the user

## Super-resolution algorithms

* [waifu2x-chainer](https://github.com/tsurumeso/waifu2x-chainer)


## Setup

1. Create a new Cloud Storage bucket, this will behave like a tmp folder for the API
   - Specify `Uniform` in `Access control`
   - Add a Lifecycle rule to delete objects after some time so that enhanced images will not be kept forever (I'm using 1 day)
   - Assign `Storage Object Viewer` role to `allUsers` so that users can download enhanced images
   
2. Create a new service account in IAM & Admin
   - Assign it `Storage Admin` role
   - Create a json key and store the key securely

3. Configure
   - Copy the service account json key to this repository
   - Rename `config_template.yaml` to `config.yaml` and make changes to it based on your environment
   
4. Build and deploy the container to Cloud Run
   - Use maximum CPU, RAM and timeout setting
   - Set maximum requests per container to 1
