#!/usr/bin/env python

import logging, webapp2

from google.appengine.api import taskqueue

class CronCheckAndSend( webapp2.RequestHandler ):
    def get(self):
        return
"""
class QueueWeeklyAnalytics( webapp.RequestHandler ):
    def post(self):
        return self.get( )

    def get(self):
        store = ShopifyStore.get_by_uuid( self.request.get('uuid') )
        
        logging.info("Starting weekly")
        if store.pinterest_enabled:
            # Grab total # clicks
            pinterest_total_clicks = 0

            # Grab top urls and counts
            pinterest_urls, pinterest_counts = Analytics_ThisWeek.get_weekly_count( store, 'pinterest' )

            # Store this week's data
            Analytics_PastWeek.create( store, 'pinterest', pinterest_total_clicks, pinterest_urls[:3])
        
        if store.pinterest_enabled:
            # Grab total # clicks
            pinterest_total_clicks = 0

            # Grab top urls and counts
            pinterest_urls, pinterest_counts = Analytics_ThisWeek.get_weekly_count( store, 'pinterest' )

            # Store this week's data
            Analytics_PastWeek.create( store, 'pinterest', pinterest_total_clicks, pinterest_urls[:3])

        # Send out email
        Email.weeklyAnalytics( store.email, 
                               store.full_name, 
                               pinterest_total_clicks,
                               pinterest_urls,
                               pinterest_counts )

class CronWeeklyAnalytics( webapp.RequestHandler ):
    def post(self):
        return self.get( )

    def get(self):
        stores = ShopifyStore.all()
        for s in stores:
            taskqueue.add( queue_name = 'analytics', 
                           url        = '/analytics/queue/weekly',
                           params     = {'uuid' : s.uuid} )

        
"""
