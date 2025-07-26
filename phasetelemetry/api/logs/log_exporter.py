from abc import ABCMeta, abstractmethod
from typing import List

from phasetelemetry.api.logs import LogRecord


class LogExporter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def export(self, records):  # type: (List[LogRecord]) -> bool
        pass

    @abstractmethod
    def shutdown(self):  # type: () -> None
        pass
