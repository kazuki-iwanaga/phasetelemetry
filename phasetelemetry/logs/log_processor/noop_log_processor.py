from phasetelemetry.logs.log_processor.interface import LogProcessorInterface
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class NoOpLogProcessor(LogProcessorInterface):

    def on_emit(self, record):  # type: (LogRecordInterface) -> None
        pass

    def force_flush(self):  # type: () -> None
        pass

    def shutdown(self):  # type: () -> None
        pass
