#!/usr/bin/env python

from apps.email-reminder.views     import *
from apps.email-reminder.processes import *

urlpatterns = [
    # Views
    (r'/email',                    ShowEmailIndex),

    # Processes
    (r'/email/cron/checkAndSend',  CronCheckAndSend),

]

