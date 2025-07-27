from phasetelemetry.logs.logger.logger import Logger


class TestLogger:

    def test_emit(self, mocker):
        # Arrange
        manager = mocker.Mock()
        logger = Logger(manager)
        record = mocker.Mock()

        # Act
        logger.emit(record)

        # Assert
        manager.on_emit.assert_called_once_with(record)
