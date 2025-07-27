from phasetelemetry.logs.log_processor.interface import LogProcessorInterface
from phasetelemetry.logs.log_processor_manager.interface import LogProcessorManagerInterface
from phasetelemetry.logs.log_processor_manager.simple_log_processor_manager import SimpleLogProcessorManager
from phasetelemetry.logs.logger.interface import LoggerInterface
from phasetelemetry.logs.logger_provider.logger_provider import LoggerProvider


class TestLoggerProvider:

    def test_get_logger_no_cache(self, mocker):
        """Should create a new logger when no cache exists."""
        # Arrange
        manager = mocker.Mock(spec=LogProcessorManagerInterface)
        provider = LoggerProvider(manager)

        # Act
        logger_name = "test_logger"
        logger = provider.get_logger(logger_name)

        # Assert
        assert isinstance(logger, LoggerInterface)
        assert logger._manager == manager

    def test_get_logger_with_cache(self, mocker):
        """Should return the same logger instance when called with the same name."""
        # Arrange
        manager = mocker.Mock(spec=LogProcessorManagerInterface)
        provider = LoggerProvider(manager)

        # Act
        logger_name = "test_logger"
        logger1 = provider.get_logger(logger_name)
        logger2 = provider.get_logger(logger_name)

        # Assert
        assert isinstance(logger1, LoggerInterface)
        assert isinstance(logger2, LoggerInterface)
        assert logger1 is logger2

    def test_default_log_processor_manager(self):
        """Should use SimpleLogProcessorManager when no manager is provided."""
        # Arrange
        provider = LoggerProvider(None)

        # Act
        logger = provider.get_logger("default_logger")

        # Assert
        assert isinstance(logger._manager, SimpleLogProcessorManager)

    def test_add_processor(self, mocker):
        """Should call LogProcessorManager's add_processor."""
        # Arrange
        manager = mocker.Mock(spec=LogProcessorManagerInterface)
        provider = LoggerProvider(manager)

        # Act
        processor = mocker.Mock(spec=LogProcessorInterface)
        provider.add_processor(processor)

        # Assert
        manager.add_processor.assert_called_once_with(processor)

    def test_force_flush(self, mocker):
        """Should call LogProcessorManager's force_flush."""
        # Arrange
        manager = mocker.Mock(spec=LogProcessorManagerInterface)
        provider = LoggerProvider(manager)

        # Act
        provider.force_flush()

        # Assert
        manager.force_flush.assert_called_once()

    def test_shutdown(self, mocker):
        """Should call LogProcessorManager's shutdown."""
        # Arrange
        manager = mocker.Mock(spec=LogProcessorManagerInterface)
        provider = LoggerProvider(manager)

        # Act
        provider.shutdown()

        # Assert
        manager.shutdown.assert_called_once()
