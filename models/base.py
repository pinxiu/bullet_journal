import uuid

UUID_LENGTH = 36


def create_uuid_string() -> str:
    return uuid.uuid4().hex
