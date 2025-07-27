from phasetelemetry.logs.log_exporter.in_memory_log_exporter import InMemoryLogExporter
from phasetelemetry.logs.log_record.noop_log_record import NoOpLogRecord


class TestInMemoryLogExporter:

    def test_export(self):
        """Exported records should be stored in memory list."""

        # Arrange
        exporter = InMemoryLogExporter()
        # NOTE: Set already exported records to test extending list.
        exporter._exported = [NoOpLogRecord for _ in range(2)]

        # Act
        records = [NoOpLogRecord for _ in range(3)]
        result = exporter.export(records)

        # Assert
        assert result is True
        assert len(exporter._exported) == 5
        assert exporter._exported[-3:] == records

    def test_shutdown(self):
        """After shutdown is called, no records should be exported."""

        # Arrange
        exporter = InMemoryLogExporter()

        # Act
        exporter.shutdown()

        records = [NoOpLogRecord for _ in range(3)]
        result = exporter.export(records)

        # Assert
        assert result is False
        assert exporter._exported == []
