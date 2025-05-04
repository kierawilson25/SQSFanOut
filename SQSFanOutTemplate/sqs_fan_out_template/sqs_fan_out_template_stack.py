from aws_cdk import Stack
import aws_cdk as cdk
import aws_cdk.aws_iam as iam
import aws_cdk.aws_lambda as aws_lambda
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_sns as sns
import aws_cdk.aws_sqs as sqs
from constructs import Construct

class SqsFanOutTemplateStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

        # Define the props dictionary
    props = {
        'lambdaFunctionGeneratethumbnaillambdaCodeS3ObjectVersionVxzAo': cdk.CfnParameter(self, 'LambdaCodeS3ObjectVersion', type='String', default='latest'),
        'lambdaFunctionGeneratethumbnaillambdaCodeS3Bucket2k8Qn': cdk.CfnParameter(self, 'LambdaCodeS3Bucket', type='String', default='my-bucket-name'),
        'lambdaFunctionGeneratethumbnaillambdaCodeZipFiletKhrF': cdk.CfnParameter(self, 'LambdaCodeZipFile', type='String', default='my-zip-file.zip'),
        'lambdaFunctionGeneratethumbnaillambdaCodeImageUriuFwwA': cdk.CfnParameter(self, 'LambdaCodeImageUri', type='String', default='my-image-uri'),
        'lambdaFunctionGeneratethumbnaillambdaCodeS3KeyU7DtW': cdk.CfnParameter(self, 'LambdaCodeS3Key', type='String', default='my-s3-key'),
    }
    # Resources
    iamManagedPolicyPolicyserviceroleAwsLambdaBasicExecutionRole12a7b83263fb4700a64b79855bd0f6ad = iam.CfnManagedPolicy(self, 'IAMManagedPolicyPolicyserviceroleAWSLambdaBasicExecutionRole12a7b83263fb4700a64b79855bd0f6ad',
          managed_policy_name = 'AWSLambdaBasicExecutionRole-12a7b832-63fb-4700-a64b-79855bd0f6ad',
          path = '/service-role/',
          description = '',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': 'arn:aws:logs:us-east-1:361769557650:*',
                'Action': 'logs:CreateLogGroup',
                'Effect': 'Allow',
              },
              {
                'Resource': [
                  'arn:aws:logs:us-east-1:361769557650:log-group:/aws/lambda/sqs-message-logger:*',
                ],
                'Action': [
                  'logs:CreateLogStream',
                  'logs:PutLogEvents',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'lambda-sqs-access',
          ],
          users = [
          ],
        )
    iamManagedPolicyPolicyserviceroleAwsLambdaBasicExecutionRole12a7b83263fb4700a64b79855bd0f6ad.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    iamManagedPolicyPolicyserviceroleAwsLambdaBasicExecutionRolec9016dd897564ea1b28c411330a967d6 = iam.CfnManagedPolicy(self, 'IAMManagedPolicyPolicyserviceroleAWSLambdaBasicExecutionRolec9016dd897564ea1b28c411330a967d6',
          managed_policy_name = 'AWSLambdaBasicExecutionRole-c9016dd8-9756-4ea1-b28c-411330a967d6',
          path = '/service-role/',
          description = '',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': 'arn:aws:logs:us-east-1:361769557650:*',
                'Action': 'logs:CreateLogGroup',
                'Effect': 'Allow',
              },
              {
                'Resource': [
                  'arn:aws:logs:us-east-1:361769557650:log-group:/aws/lambda/generate-thumbnail-lambda:*',
                ],
                'Action': [
                  'logs:CreateLogStream',
                  'logs:PutLogEvents',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'generate-thumbnail-role',
          ],
          users = [
          ],
        )
    iamManagedPolicyPolicyserviceroleAwsLambdaBasicExecutionRolec9016dd897564ea1b28c411330a967d6.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    iamManagedPolicyPolicyserviceroleAwsLambdaS3ExecutionRoleb1d9459c168544d6a7697e835365c9a8 = iam.CfnManagedPolicy(self, 'IAMManagedPolicyPolicyserviceroleAWSLambdaS3ExecutionRoleb1d9459c168544d6a7697e835365c9a8',
          managed_policy_name = 'AWSLambdaS3ExecutionRole-b1d9459c-1685-44d6-a769-7e835365c9a8',
          path = '/service-role/',
          description = '',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': 'arn:aws:s3:::*',
                'Action': [
                  's3:GetObject',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'generate-thumbnail-role',
          ],
          users = [
          ],
        )
    iamManagedPolicyPolicyserviceroleAwsLambdaS3ExecutionRoleb1d9459c168544d6a7697e835365c9a8.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    iamManagedPolicyPolicyserviceroleAwsLambdaSqsPollerExecutionRole230286410fcc43d4a53411ff12cc32a3 = iam.CfnManagedPolicy(self, 'IAMManagedPolicyPolicyserviceroleAWSLambdaSQSPollerExecutionRole230286410fcc43d4a53411ff12cc32a3',
          managed_policy_name = 'AWSLambdaSQSPollerExecutionRole-23028641-0fcc-43d4-a534-11ff12cc32a3',
          path = '/service-role/',
          description = '',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': 'arn:aws:sqs:us-east-1:361769557650:*',
                'Action': [
                  'sqs:DeleteMessage',
                  'sqs:GetQueueAttributes',
                  'sqs:ReceiveMessage',
                ],
                'Effect': 'Allow',
                'Sid': 'AWSLambdaSQSPollerExecutionRole',
              },
            ],
          },
          roles = [
            'generate-thumbnail-role',
          ],
          users = [
          ],
        )
    iamManagedPolicyPolicyserviceroleAwsLambdaSqsPollerExecutionRole230286410fcc43d4a53411ff12cc32a3.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    iamManagedPolicyPolicyserviceroleAwsLambdaSqsPollerExecutionRole262bfa723639406fa3052f99a112e8a5 = iam.CfnManagedPolicy(self, 'IAMManagedPolicyPolicyserviceroleAWSLambdaSQSPollerExecutionRole262bfa723639406fa3052f99a112e8a5',
          managed_policy_name = 'AWSLambdaSQSPollerExecutionRole-262bfa72-3639-406f-a305-2f99a112e8a5',
          path = '/service-role/',
          description = '',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': 'arn:aws:sqs:us-east-1:361769557650:*',
                'Action': [
                  'sqs:DeleteMessage',
                  'sqs:GetQueueAttributes',
                  'sqs:ReceiveMessage',
                ],
                'Effect': 'Allow',
                'Sid': 'AWSLambdaSQSPollerExecutionRole',
              },
            ],
          },
          roles = [
            'lambda-sqs-access',
          ],
          users = [
          ],
        )
    iamManagedPolicyPolicyserviceroleAwsLambdaSqsPollerExecutionRole262bfa723639406fa3052f99a112e8a5.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    s3BucketImguploadiac2025resized = s3.CfnBucket(self, 'S3BucketImguploadiac2025resized',
          public_access_block_configuration = {
            'restrictPublicBuckets': True,
            'ignorePublicAcls': True,
            'blockPublicPolicy': True,
            'blockPublicAcls': True,
          },
          bucket_name = 'img-upload-iac2025-resized',
          ownership_controls = {
            'rules': [
              {
                'objectOwnership': 'BucketOwnerEnforced',
              },
            ],
          },
          bucket_encryption = {
            'serverSideEncryptionConfiguration': [
              {
                'bucketKeyEnabled': True,
                'serverSideEncryptionByDefault': {
                  'sseAlgorithm': 'AES256',
                },
              },
            ],
          },
        )
    s3BucketImguploadiac2025resized.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    sqsQueueNewimguploadqueue = sqs.CfnQueue(self, 'SQSQueueNewimguploadqueue',
          sqs_managed_sse_enabled = True,
          receive_message_wait_time_seconds = 0,
          delay_seconds = 0,
          message_retention_period = 345600,
          maximum_message_size = 262144,
          visibility_timeout = 30,
          queue_name = 'new-img-upload-queue',
        )
    sqsQueueNewimguploadqueue.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    iamRoleGeneratethumbnailrole = iam.CfnRole(self, 'IAMRoleGeneratethumbnailrole',
          path = '/service-role/',
          managed_policy_arns = [
            iamManagedPolicyPolicyserviceroleAwsLambdaSqsPollerExecutionRole230286410fcc43d4a53411ff12cc32a3.ref,
            'arn:aws:iam::aws:policy/AmazonS3FullAccess',
            iamManagedPolicyPolicyserviceroleAwsLambdaBasicExecutionRolec9016dd897564ea1b28c411330a967d6.ref,
            iamManagedPolicyPolicyserviceroleAwsLambdaS3ExecutionRoleb1d9459c168544d6a7697e835365c9a8.ref,
          ],
          max_session_duration = 3600,
          role_name = 'generate-thumbnail-role',
          policies = [
            {
              'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [
                  {
                    'Resource': 'arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p39-Pillow:1',
                    'Action': 'lambda:GetLayerVersion',
                    'Effect': 'Allow',
                  },
                ],
              },
              'policyName': 'lambdaGetLayerPermission',
            },
            {
              'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [
                  {
                    'Resource': '*',
                    'Action': 's3:*',
                    'Effect': 'Allow',
                  },
                ],
              },
              'policyName': 's3-full-access-lambda',
            },
          ],
          assume_role_policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Action': 'sts:AssumeRole',
                'Effect': 'Allow',
                'Principal': {
                  'Service': 'lambda.amazonaws.com',
                },
              },
            ],
          },
        )
    iamRoleGeneratethumbnailrole.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    iamRoleLambdasqsaccess = iam.CfnRole(self, 'IAMRoleLambdasqsaccess',
          path = '/service-role/',
          managed_policy_arns = [
            'arn:aws:iam::aws:policy/AmazonS3FullAccess',
            iamManagedPolicyPolicyserviceroleAwsLambdaSqsPollerExecutionRole262bfa723639406fa3052f99a112e8a5.ref,
            iamManagedPolicyPolicyserviceroleAwsLambdaBasicExecutionRole12a7b83263fb4700a64b79855bd0f6ad.ref,
          ],
          max_session_duration = 3600,
          role_name = 'lambda-sqs-access',
          assume_role_policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Action': 'sts:AssumeRole',
                'Effect': 'Allow',
                'Principal': {
                  'Service': 'lambda.amazonaws.com',
                },
              },
            ],
          },
        )
    iamRoleLambdasqsaccess.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    snsTopicImguploadspring2025124375 = sns.CfnTopic(self, 'SNSTopicImguploadspring2025124375',
          fifo_topic = False,
          subscription = [
            {
              'endpoint': sqsQueueNewimguploadqueue.attr_arn,
              'protocol': 'sqs',
            },
          ],
          tracing_config = 'PassThrough',
          archive_policy = {
          },
          topic_name = 'img-upload-spring-2025-124375',
        )
    snsTopicImguploadspring2025124375.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    lambdaFunctionGeneratethumbnaillambda = aws_lambda.CfnFunction(self, 'LambdaFunctionGeneratethumbnaillambda',
          memory_size = 128,
          description = 'An Amazon SQS trigger that logs messages in a queue.',
          tracing_config = {
            'mode': 'PassThrough',
          },
          timeout = 63,
          runtime_management_config = {
            'updateRuntimeOn': 'Auto',
          },
          handler = 'lambda_function.lambda_handler',
          code = {
            's3ObjectVersion': props['lambdaFunctionGeneratethumbnaillambdaCodeS3ObjectVersionVxzAo'].value_as_string,
            's3Bucket': props['lambdaFunctionGeneratethumbnaillambdaCodeS3Bucket2k8Qn'].value_as_string,
            'zipFile': props['lambdaFunctionGeneratethumbnaillambdaCodeZipFiletKhrF'].value_as_string,
            'imageUri': props['lambdaFunctionGeneratethumbnaillambdaCodeImageUriuFwwA'].value_as_string,
            's3Key': props['lambdaFunctionGeneratethumbnaillambdaCodeS3KeyU7DtW'].value_as_string,
          },
          role = iamRoleGeneratethumbnailrole.attr_arn,
          file_system_configs = [
          ],
          function_name = 'generate-thumbnail-lambda',
          runtime = 'python3.9',
          package_type = 'Zip',
          logging_config = {
            'logFormat': 'Text',
            'logGroup': '/aws/lambda/generate-thumbnail-lambda',
          },
          ephemeral_storage = {
            'size': 512,
          },
          layers = [
            'arn:aws:lambda:us-east-1:361769557650:layer:my-lambda-pillow-layer:2',
            'arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:11',
          ],
          tags = [
            {
              'value': 'sqs-poller',
              'key': 'lambda-console:blueprint',
            },
          ],
          architectures = [
            'x86_64',
          ],
        )
    lambdaFunctionGeneratethumbnaillambda.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE

    s3BucketImguploadiac2025 = s3.CfnBucket(self, 'S3BucketImguploadiac2025',
          notification_configuration = {
            'queueConfigurations': [
            ],
            'topicConfigurations': [
              {
                'topic': snsTopicImguploadspring2025124375.ref,
                'filter': {
                  's3Key': {
                    'rules': [
                      {
                        'value': '',
                        'name': 'Prefix',
                      },
                      {
                        'value': '',
                        'name': 'Suffix',
                      },
                    ],
                  },
                },
                'event': 's3:ObjectCreated:*',
              },
            ],
            'lambdaConfigurations': [
            ],
          },
          public_access_block_configuration = {
            'restrictPublicBuckets': True,
            'ignorePublicAcls': True,
            'blockPublicPolicy': True,
            'blockPublicAcls': True,
          },
          bucket_name = 'img-upload-iac2025',
          ownership_controls = {
            'rules': [
              {
                'objectOwnership': 'BucketOwnerEnforced',
              },
            ],
          },
          bucket_encryption = {
            'serverSideEncryptionConfiguration': [
              {
                'bucketKeyEnabled': True,
                'serverSideEncryptionByDefault': {
                  'sseAlgorithm': 'AES256',
                },
              },
            ],
          },
        )
    s3BucketImguploadiac2025.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.DELETE


