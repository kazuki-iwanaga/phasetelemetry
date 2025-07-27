from phasetelemetry.logs.log_record.simple_log_record import SimpleLogRecord


class TestSimpleLogRecord:

    def test_to_json(self):
        # Arrange
        message = "Test log message"
        log_record = SimpleLogRecord(message)

        # Act
        result = log_record.to_json()

        # Assert
        assert result == '{"message": "Test log message"}'
