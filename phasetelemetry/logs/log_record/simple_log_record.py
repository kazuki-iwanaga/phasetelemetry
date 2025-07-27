import json
from typing import Union

import six
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class SimpleLogRecord(LogRecordInterface):
    """A simple implementation that records a string message."""

    def __init__(
            self,
            message):  # type: (Union[six.text_type, six.binary_type]) -> None
        """Initialize with a string message.

        Args:
            message (Union[six.text_type, six.binary_type]): The log message to record.
        
        Returns:
            None
        """
        self._message = six.ensure_text(message)

    def to_json(self):  # type: () -> six.text_type
        """Convert the log record to a JSON string.

        Returns:
            str: The JSON representation of the log record.
        """
        return six.ensure_text(
            json.dumps({"message": self._message}, ensure_ascii=False))
