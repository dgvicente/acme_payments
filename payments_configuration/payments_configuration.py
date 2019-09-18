from .payments_configuration_entry import PaymentsConfigurationEntry


class PaymentsConfiguration:

    def __init__(self, weekdays, weekends):
        self.weekdays_config = [PaymentsConfigurationEntry(item) for item in weekdays.split('\n') if item] if weekdays else []
        self.weekend_config = [PaymentsConfigurationEntry(item) for item in weekends.split('\n') if item] if weekends else []
