"""Exceptions for Ajax System."""
from typing import Optional


class AjaxSystemError(Exception):
    """Generic Ajax System exception."""

    def __init__(self, status: str, errno: Optional[int] = None):
        """Initialize."""
        super().__init__(status)
        self.status = status
        self.errno = errno


class AjaxSystemConnectionError(AjaxSystemError):
    """Ajax System connection exception."""


class AjaxSystemConnectionTimeoutError(AjaxSystemConnectionError, TimeoutError):
    """Ajax System connection Timeout exception."""


class ETIDomoUnmanagedDeviceError(AjaxSystemError):
    """ETI/Domo exception for unmanaged device."""

    def __init__(
        self, status: str = "This device is unmanageable", errno: Optional[int] = None
    ):
        """Initialize."""
        super().__init__(status, errno)
