resource "aws_instance" "bastion" {
    ami = "ami-0d2017e886fc2c0ab"
    instance_type = "t3.small"
    tags = {
        "Name" = "bastion"
    }
}