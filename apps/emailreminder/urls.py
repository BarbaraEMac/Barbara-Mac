#!/usr/bin/env python

from apps.emailreminder.views     import *
from apps.emailreminder.processes import *

urlpatterns = [
    (r'/email',                   ShowEmailIndex),
    (r'/email/create',            DoCreateEmailReminder),
    
    (r'/email/cron/checkAndSend', CronCheckAndSend),
]
