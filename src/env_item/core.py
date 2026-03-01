import os
from typing import Any, Self

from pydantic import Secret

from .exceptions import EnvironmentVariableCastError, EnvironmentVariableMissingError


class EnvItem:
    def __init__(self, key: str) -> None:
        self.key = key
        self.value = os.getenv(self.key)

    def default(self, value: Any) -> Self:
        if self.value is None:
            self.value = value

        return self

    def required(self) -> Self:
        if self.value is None:
            raise EnvironmentVariableMissingError(self.key)

        return self

    def secret(self) -> Self:
        if self.value is not None:
            self.value = Secret(self.value)

        return self

    def get_str(self) -> str:
        try:
            self.value = str(self.value)
        except Exception:  # noqa: BLE001
            raise EnvironmentVariableCastError(self.key, str)  # noqa: B904

        return self.value

    def get_int(self) -> int:
        try:
            self.value = int(self.value)
        except Exception:  # noqa: BLE001
            raise EnvironmentVariableCastError(self.key, int)  # noqa: B904

        return self.value

    def get_bool(self) -> bool:
        if self.value in {"True", "true"}:
            return True
        if self.value in {"False", "false"}:
            return False
        raise EnvironmentVariableCastError(self.key, bool)
