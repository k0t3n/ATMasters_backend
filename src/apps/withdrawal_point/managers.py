from datetime import datetime

from django.db import models


class WithdrawalPointsManager(models.Manager):
    def working_now(self, *args, **kwargs):
        time_now = datetime.now()
        entering_the_range = self.filter(
            schedule__start_day__lte=time_now.weekday(),
            schedule__end_day__gte=time_now.weekday(),
        )

        round_the_clock = entering_the_range.filter(schedule__is_round_the_clock=True)
        working_now = entering_the_range.filter(schedule__is_closed=False)
        queryset = (round_the_clock | working_now).distinct()

        return queryset
