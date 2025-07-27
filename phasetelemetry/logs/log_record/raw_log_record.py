from phasetelemetry.logs.log_record.interface import LogRecordInterface


class RawLogRecord(LogRecordInterface):
    """Simple implementation of LogRecord."""

    def __init__(self, message):  # type: (str) -> None
        """Initialize an instance.

        Args:
            message (str): Body message.
        
        Returns:
            None
        """
        self._message = message
