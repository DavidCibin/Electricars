from django import forms
from bootstrap_daterangepicker import widgets, fields


class DateRangePicker(forms.Form):
    # Date Picker Fields
    date_single_normal = fields.DateField()
    date_single_with_format = fields.DateField(
        input_formats=['%d/%m/%Y'],
        widget=widgets.DatePickerWidget(
            format='%d/%m/%Y'
        )
    )
    date_single_clearable = fields.DateField(required=False)

    # Date Range Fields
    date_range_normal = fields.DateRangeField()
    date_range_with_format = fields.DateRangeField(
        input_formats=['%d/%m/%Y'],
        widget=widgets.DateRangeWidget(
            format='%d/%m/%Y'
        )
    )
    date_range_clearable = fields.DateRangeField(required=False)

    # DateTime Range Fields
    datetime_range_normal = fields.DateTimeRangeField()
    datetime_range_with_format = fields.DateTimeRangeField(
        input_formats=['%d/%m/%Y (%I:%M:%S)'],
        widget=widgets.DateTimeRangeWidget(
            format='%d/%m/%Y (%I:%M:%S)'
        )
    )
    datetime_range_clearable = fields.DateTimeRangeField(required=False)