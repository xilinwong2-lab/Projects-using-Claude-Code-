import uuid
import boto3
from app.config import settings


def upload_image(image_bytes: bytes, filename: str, user_id: int) -> str:
    """Upload image to S3 and return public URL. Falls back to a local placeholder in dev."""
    if not settings.aws_bucket_name:
        # Dev mode — skip real upload
        return f"/static/uploads/{user_id}/{uuid.uuid4()}_{filename}"

    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.aws_access_key_id,
        aws_secret_access_key=settings.aws_secret_access_key,
        region_name=settings.aws_region,
    )
    key = f"users/{user_id}/{uuid.uuid4()}_{filename}"
    s3.put_object(Bucket=settings.aws_bucket_name, Key=key, Body=image_bytes, ContentType="image/jpeg")
    return f"https://{settings.aws_bucket_name}.s3.{settings.aws_region}.amazonaws.com/{key}"
