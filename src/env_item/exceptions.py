class EnvItemError(Exception):
    pass

class EnvironmentVariableMissingError(EnvItemError):
    def __init__(self, key: str) -> None:
        message: str = f"Environment variable {key} is missing. Check your .env file."
        super().__init__(message)


class EnvironmentVariableCastError(EnvItemError):
    def __init__(self, key: str, cast: type) -> None:
        message: str = f"Environment variable {key} cannot be cast to type {cast.__name__}"
        super().__init__(message)
