from django.core.exceptions import ValidationError
from io import BytesIO
from PIL import Image
from django.core.files import File


def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File ölçüsü çox böyükdür. 2MiB-dən çox ola bilməz.')

def compress(image):
    if image != None:
        img = Image.open(image)
        format = img.format
        img_io = BytesIO()
        # img = img.convert('RGB')
        if format == 'JPEG':
            # Convert RGBA to RGB for JPEG
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            img.save(img_io, format="JPEG", quality=50)
        elif format == 'PNG':
            img.save(img_io, format="PNG", optimize=True)
        else:
            # For other formats, save as-is
            img.save(img_io, format=format)
        # img.save(img_io, "JPEG", quality=70)
        new_image = File(img_io, name=image.name)
        return new_image