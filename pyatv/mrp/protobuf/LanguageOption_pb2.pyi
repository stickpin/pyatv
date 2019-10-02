# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class LanguageOption(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type = ... # type: int
    languageTag = ... # type: typing___Text
    characteristics = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    displayName = ... # type: typing___Text
    identifier = ... # type: typing___Text

    def __init__(self,
        *,
        type : typing___Optional[int] = None,
        languageTag : typing___Optional[typing___Text] = None,
        characteristics : typing___Optional[typing___Iterable[typing___Text]] = None,
        displayName : typing___Optional[typing___Text] = None,
        identifier : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LanguageOption: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"displayName",u"identifier",u"languageTag",u"type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"characteristics",u"displayName",u"identifier",u"languageTag",u"type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"displayName",b"displayName",u"identifier",b"identifier",u"languageTag",b"languageTag",u"type",b"type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"characteristics",b"characteristics",u"displayName",b"displayName",u"identifier",b"identifier",u"languageTag",b"languageTag",u"type",b"type"]) -> None: ...