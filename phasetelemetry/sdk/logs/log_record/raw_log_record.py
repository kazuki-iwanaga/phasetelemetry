from phasetelemetry.api.logs import LogRecord


class RawLogRecord(LogRecord):
    """Simple implementation of LogRecord."""

    def __init__(self, message):  # type: (str) -> None
        """Initialize an instance.

        Args:
            message (str): Body message.
        
        Returns:
            None
        """
        self.message = message
