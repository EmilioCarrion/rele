from unittest.mock import patch, ANY

import pytest
from django.conf import settings
from django.core.management import call_command

from rele import Worker


class TestRunReleCommand:
    @pytest.fixture(autouse=True)
    def worker_wait_forever(self):
        with patch.object(Worker, "_wait_forever", return_value=None) as p:
            yield p

    @pytest.fixture
    def mock_worker(self):
        with patch("rele.management.commands.runrele.Worker", autospec=True) as p:
            yield p

    def test_calls_worker_start_and_setup_when_runrele(self, mock_worker):
        call_command("runrele")

        config = mock_worker.mock_calls[0][1][1]
        assert (
            config.gc_project_id == "SOME-PROJECT-ID"
            and config.credentials == ANY
            and config.ack_deadline == 60
        )
        mock_worker.assert_called_with([], "SOME-PROJECT-ID", ANY, 60)
        mock_worker.return_value.run_forever.assert_called_once_with()

    def test_prints_warning_when_conn_max_age_not_set_to_zero(
        self, mock_worker, capsys
    ):
        settings.DATABASES = {"default": {"CONN_MAX_AGE": 1}}
        call_command("runrele")

        out, err = capsys.readouterr()
        assert (
            "WARNING: settings.CONN_MAX_AGE is not set to 0. "
            "This may result in slots for database connections to "
            "be exhausted." in err
        )

        config = mock_worker.mock_calls[0][1][1]
        assert (
            config.gc_project_id == "SOME-PROJECT-ID"
            and config.credentials == ANY
            and config.ack_deadline == 60
        )
        mock_worker.assert_called_with([], "SOME-PROJECT-ID", ANY, 60)
        mock_worker.return_value.run_forever.assert_called_once_with()
