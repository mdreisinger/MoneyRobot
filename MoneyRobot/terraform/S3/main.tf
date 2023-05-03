# aws_s3_bucket.moneyrobot:
resource "aws_s3_bucket" "moneyrobot" {
    bucket                      = "moneyrobot"
    object_lock_enabled         = false
    request_payer               = "BucketOwner"
    tags                        = {}
    tags_all                    = {}

    grant {
        id          = "262f7623cd8d1394e6e25e76b68524620a25d8b08183bfde78c6dc86e600d0bf"
        permissions = [
            "FULL_CONTROL",
        ]
        type        = "CanonicalUser"
    }

    server_side_encryption_configuration {
        rule {
            bucket_key_enabled = false

            apply_server_side_encryption_by_default {
                sse_algorithm = "AES256"
            }
        }
    }

    versioning {
        enabled    = false
        mfa_delete = false
    }
}