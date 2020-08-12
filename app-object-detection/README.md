
Serverless application that uses a deep learning model YOLOv2 to detect objects on uploaded images. The inference code was written by me during the Deep Learning Specialization course, created by deeplearning.ai. When creating this demo I was inspired by an open-source project Serverless Stack by Anomaly Innovations. The API and website are both hosted on AWS. The front-end is a single page app build on top of Create React App project, developed by Facebook.

The back-end is built on top of Serverless Node.js Starter, a part of Serverless Stack, an open-source project developed by Anomaly Innovations. They created a step-by-step guide to help you build a full-stack serverless application hosted on AWS. The front-end is a single page app build on top of Create React App project developed by Facebook.

<h2>Prerequisites</h2>
AWS account
AWS CLI set up (learn more <a href='https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html'>here</a>)

<h2>Launch the stack with CloudFormation</h2> 
on the AWS console:
<img src="cloudformation-launch-stack.png" href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=object-detection-app&templateURL=https://raw.githubusercontent.com/molly-moon/app-object-detection/master/object-detection-app-stack.yml"/>

or via AWS CLI:
download CloudFormation template:
https://raw.githubusercontent.com/molly-moon/projects/master/app-object-detection/web-app/object-detection-app-stack.yml
run the command:
aws cloudformation create-stack --stack-name object-detection-app --template-body file://PATH-TO-TEMPLATE/object-detection-app-stack.yml

Creation time: about 30 min 

<h2>Under the hood: what resources are being provisioned</h2>
<ul>
	<li>Basic environment: VPC, public subnet, private subnet, Internet Gateway, NAT Gateway and all necessary attachments and associations</li>
	<li>S3 bucket for website hosting and for Lambda handler code storage</li>
	<li>Elastic File System for increased Lambda storage space</li>
	<li>Lambda function to execute machine learning inference code</li>
	<li>REST API with API Gateway to serve as a front-door to the application</li>
	<li>EC2 instance to perform automated configuration tasks:
    - Download Lambda handler code
    - Download static files to host the website
    - Download inference model weights
    - Mount Elastic File System and install Lambda dependencies 
       The instance will self-terminate right after the setup is completed.

<h2>Clean up</h2>
aws cloudformation delete-stack --stack-name object-detection-app

