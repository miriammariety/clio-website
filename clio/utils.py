import uuid

from django.db import IntegrityError


def generate_slug(model):
    generated_slug = uuid.uuid4().bytes.encode('base64')
    generated_slug = generated_slug.rstrip('=\n')
    generated_slug = generated_slug.replace('+', '-').replace('/', '_')
    # in the VERY unlikely event that the generated slug already exists
    try:
        model.objects.get(slug=generated_slug)
    except (model.DoesNotExist, IntegrityError):
        return generated_slug[:11]
    return generate_slug()
