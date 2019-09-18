from unittest import TestCase

from configuration_factory.configuration_factory import ConfigurationFactory


class TestConfigurationFactory(TestCase):

    def test_should_build_configuration_using_default_file(self):
        payments_configuration = ConfigurationFactory.build()
        self.assertEquals(len(payments_configuration.weekend_config), 3)
