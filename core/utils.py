import random
import string
from django.utils.text import slugify
from django.db.models import Model

def random_string_generator(size:int=4, chars:str=string.ascii_lowercase+string.digits):
    '''
    Generate random string for making unique slugs.
    It generates 4 random chars by default.
    accepts 2 optional parameters
    @param size
    @param chars
    '''
    return ''.join([random.choice(chars) for _ in range(size)])

def unique_slug_generator(instance):
    '''
    It acceps 1 positional argument (instance).
    It assumes your model has a slug and name fields
    '''
    slug = slugify(instance.name)
    model = instance.__class__

    if model.objects.filter(slug=slug).exists():
        new_slug = f'{slug}-{random_string_generator()}'
        return new_slug

    return slug