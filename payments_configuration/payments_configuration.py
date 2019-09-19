from .payments_configuration_entry import PaymentsConfigurationEntry


class PaymentsConfiguration:

    def __init__(self, weekdays, weekends):
        self.weekdays_config = [PaymentsConfigurationEntry(item) for item in weekdays if item] if weekdays else []
        self.weekend_config = [PaymentsConfigurationEntry(item) for item in weekends if item] if weekends else []

    def get_hours_for(self, question_hour_item):
        entries_source = self.weekdays_config if question_hour_item.is_weekday() else self.weekend_config
        hours = []
        for entry in entries_source:
            hours_for_entry = entry.get_hours_contained(question_hour_item.initial_time, question_hour_item.end_time)
            if hours_for_entry:
                hours.append({'rate': entry.amount, 'hours': hours_for_entry})
        return hours
