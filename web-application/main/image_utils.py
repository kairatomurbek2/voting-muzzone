import uuid


def poll_choices_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'poll/{0}/choices/{1}'.format(instance.poll.id, filename)