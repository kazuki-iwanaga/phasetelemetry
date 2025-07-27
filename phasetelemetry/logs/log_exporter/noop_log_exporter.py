from typing import List

from phasetelemetry.logs.log_exporter.interface import LogExporterInterface
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class NoOpLogExporter(LogExporterInterface):

    def export(self, _):  # type: (List[LogRecordInterface]) -> bool
        return True

    def shutdown(self):  # type: () -> None
        pass
