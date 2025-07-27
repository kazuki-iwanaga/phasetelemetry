from abc import ABCMeta, abstractmethod
from typing import List

from phasetelemetry.logs.log_record.interface import LogRecordInterface


class LogExporterInterface(object):
    """Interface for log exporters that send log records to external systems."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def export(self, records):  # type: (List[LogRecordInterface]) -> bool
        """Export a list of log records to an external system.

        Args:
            records (List[LogRecordInterface]): The log records to export.
        Returns:
            bool: True if export was successful, False otherwise.
        """
        pass

    @abstractmethod
    def shutdown(self):  # type: () -> None
        """Shutdown the log exporter.
        Clean up all resources such as network connections or file handles.
        """
        pass
