from phasetelemetry.logs.log_processor.interface import LogProcessorInterface
from phasetelemetry.logs.log_processor_manager.interface import LogProcessorManagerInterface
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class NoOpLogProcessorManager(LogProcessorManagerInterface):

    def add_processor(self, _):  # type: (LogProcessorInterface) -> None
        pass

    def on_emit(self, _):  # type: (LogRecordInterface) -> None
        pass

    def force_flush(self):  # type: () -> None
        pass

    def shutdown(self):  # type: () -> None
        pass
