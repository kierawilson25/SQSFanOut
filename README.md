# SQSFanOut
AWS CDK project to demonstrate understanding of SQS fan-out pattern using: S3, SNS, SQS, Lambda

## Steps
1. An image is uploaded to an S3 bucket
2. A notification is send to the SNS topic which pushes the s3 event to its subscribers
3. The SQS queue subsriber has a lambda trigger which generates a thumbnail of the image
4. The image is then uploaded to a secondary 'resized' S3 bucket
