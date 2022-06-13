from django.core.exceptions import ValidationError


class ObjectDoesNotExistError(ValidationError):
    def __init__(self, classname, id: str, code=None, params=None):
        message = f"{classname._meta.verbose_name} object with id={id} does not exist."
        super().__init__(message=message, code=code, params=params)


class ObjectCannotBeDeletedError(ValidationError):
    def __init__(self, classname, id: str, code=None, params=None):
        message = f"{classname._meta.verbose_name} object with id={id} cannot be deleted."
        super().__init__(message=message, code=code, params=params)


class ObjectMustBeLinkedError(ValidationError):
    def __init__(self, classname, link_to: list, code=None, params=None):
        link_to_verbose_names = [
            link_to_classname._meta.verbose_name for link_to_classname in link_to
        ]
        message = f"{classname._meta.verbose_name} object must be linked to: {', '.join(link_to_verbose_names)}."
        super().__init__(message=message, code=code, params=params)
