"""
    ulid/hints
    ~~~~~~~~~~

    Contains type hint definitions across modules in the package.
"""
import datetime
import typing
import uuid

#: Type hint that defines multiple types that implement the buffer protocol
#: that can encoded into a Base32 string.
Buffer = typing.Union[bytes, bytearray, memoryview]  # pylint: disable=invalid-name


#: Type hint that is an alias for the built-in :class:`~bytes` type.
Bytes = bytes  # pylint: disable=invalid-name


#: Type hint that is an alias for the built-in :class:`~int` type.
Int = int  # pylint: disable=invalid-name


#: Type hint that is an alias for the built-in :class:`~float` type.
Float = float  # pylint: disable=invalid-name


#: Type hint that is an alias for the built-in :class:`~str` type.
Str = str  # pylint: disable=invalid-name


#: Type hint that is an alias for the built-in :class:`~datetime.datetime` type.
Datetime = datetime.datetime  # pylint: disable=invalid-name

#: Type hint that is an alias for the built-in :class:`~datetime.datetime` type.
UUID = uuid.UUID  # pylint: disable=invalid-name
