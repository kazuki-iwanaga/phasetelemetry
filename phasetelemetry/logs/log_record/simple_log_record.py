import json

from phasetelemetry.logs.log_record.interface import LogRecordInterface


class SimpleLogRecord(LogRecordInterface):
    """A simple implementation that records a string message."""

    def __init__(self, message):  # type: (str) -> None
        """Initialize with a string message.

        Args:
            message (str): The log message to record.
        
        Returns:
            None
        """
        self._message = message

    def to_json(self):  # type: () -> str
        """Convert the log record to a JSON string.

        Returns:
            str: The JSON representation of the log record.
        """
        return json.dumps({"message": self._message})
