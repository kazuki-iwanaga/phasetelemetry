from phasetelemetry.logs.log_record.interface import LogRecordInterface
from phasetelemetry.logs.logger.interface import LoggerInterface


class NoOpLogger(LoggerInterface):

    def emit(self, _):  # type: (LogRecordInterface) -> None
        pass
