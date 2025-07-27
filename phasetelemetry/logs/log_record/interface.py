from abc import ABCMeta, abstractmethod


class LogRecordInterface(object):
    """Interface for log records."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_json(self):  # type: () -> str
        """Convert the log record to a JSON string.

        Returns:
            str: The JSON representation of the log record.
        """
        pass
