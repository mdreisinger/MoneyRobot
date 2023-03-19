# aws_iam_role.ec2_access_s3:
resource "aws_iam_role" "ec2_access_s3" {
    assume_role_policy    = jsonencode(
        {
            Statement = [
                {
                    Action    = "sts:AssumeRole"
                    Effect    = "Allow"
                    Principal = {
                        Service = "ec2.amazonaws.com"
                    }
                },
            ]
            Version   = "2012-10-17"
        }
    )
    description           = "Allows EC2 instances to call AWS services on your behalf."
    force_detach_policies = false
    managed_policy_arns   = [
        "arn:aws:iam::aws:policy/AmazonS3FullAccess",
    ]
    max_session_duration  = 3600
    name                  = "ec2_access_s3"
    path                  = "/"
    tags                  = {}
    tags_all              = {}
}