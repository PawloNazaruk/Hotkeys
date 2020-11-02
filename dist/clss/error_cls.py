
class BaseValidationError(ValueError):
    """ Class for marking errors
    """
    pass


class SomethingIsNotYes(BaseValidationError):
    msg = "Something is not yes."


class NameAlreadyUsed(BaseValidationError):
    msg = "Given name is already used, use another one."


class FillName(BaseValidationError):
    msg = "Name entry cannot be empty."


class FillText(BaseValidationError):
    msg = "Text entry cannot empty."


class FillBothEntries(BaseValidationError):
    msg = "None entry cannot be empty."
