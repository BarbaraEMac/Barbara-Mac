#!/usr/bin/env python

from apps.emailreminder.views     import *
from apps.emailreminder.processes import *

urlpatterns = [
    (r'/email',                   ShowEmailIndex),
    
    (r'/email/cron/checkAndSend', CronCheckAndSend),
]
