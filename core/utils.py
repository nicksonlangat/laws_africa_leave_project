import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def get_workdays(start_date: datetime, end_date: datetime):
    # if the start date is on a weekend, forward the date to next Monday
    if start_date.weekday() > 4:
        start_date = start_date + datetime.timedelta(days=7 - start_date.weekday())
    # if the end date is on a weekend, rewind the date to the previous Friday
    if end_date.weekday() > 4:
        end_date = end_date - datetime.timedelta(days=end_date.weekday() - 4)
    if start_date > end_date:
        return 0
    # that makes the difference
    diff_days = (end_date - start_date).days + 1
    weeks = int(diff_days / 7)
    return weeks * 5 + (end_date.weekday() - start_date.weekday()) + 1

def validate_dates(start_date: datetime, end_date: datetime):
    if start_date > end_date:
        raise ValidationError(
            _('%(start_date)s cannot be after %(end_date)s'),
            params={'start_date': start_date, 'end_date':end_date},
        )
