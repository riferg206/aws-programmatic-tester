import pytest
import config.ConfigService as ConfigService


@pytest.fixture
def mock_file_read(monkeypatch):
    def mock_read(*args, **kwargs):
        return {
            'service': 'yes please',
            'operation': 'whatever',
            'params':
                "{'TopicArn': 'crap', 'Message': '{any}'}"
        }

    monkeypatch.setattr(ConfigService, "read_config", mock_read)


def test_single_valid_config_yml_parse_config(mock_file_read):
    assert ConfigService.parse_config.__wrapped__("some_config_file") == ['yes please',
                                                                          'whatever',
                                                                          "{'TopicArn': 'crap', 'Message': '{any}'}"]
