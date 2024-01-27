class LenPasswordError(Exception):
    pass


class AlphaPasswordError(Exception):
    pass


class SmallAlphaPasswordError(Exception):
    pass


class BigAlphaPasswordError(Exception):
    pass


class DigitPasswordError(Exception):
    pass


class SymbolPasswordError(Exception):
    pass


class SymbolLoginError(Exception):
    pass


class ExistLoginError(Exception):
    pass


class NotFoundLoginError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class NoTestsForDate(Exception):
    pass


class AuthorizationError(Exception):
    pass
