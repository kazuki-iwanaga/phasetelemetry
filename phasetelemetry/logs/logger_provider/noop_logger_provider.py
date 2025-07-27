from phasetelemetry.logs.log_processor.interface import LogProcessorInterface
from phasetelemetry.logs.logger.interface import LoggerInterface
from phasetelemetry.logs.logger.noop_logger import NoOpLogger
from phasetelemetry.logs.logger_provider.interface import LoggerProviderInterface


class NoOpLoggerProvider(LoggerProviderInterface):

    def get_logger(self, _):  # type: (str) -> LoggerInterface
        return NoOpLogger()

    def add_processor(self, _):  # type: (LogProcessorInterface) -> None
        pass

    def force_flush(self):  # type: () -> None
        pass

    def shutdown(self):  # type: () -> None
        pass
