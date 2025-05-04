import aws_cdk as core
import aws_cdk.assertions as assertions

from sqs_fan_out_template.sqs_fan_out_template_stack import SqsFanOutTemplateStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sqs_fan_out_template/sqs_fan_out_template_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SqsFanOutTemplateStack(app, "sqs-fan-out-template")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
