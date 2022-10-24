import { Component, OnInit } from '@angular/core';
import { EventCrudService } from '../Data(services)/eventCrud.services';
import { FeedCrudService } from '../Data(services)/feedCrud.services';
import { Router } from '@angular/router';
import { promise } from 'protractor';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {

  events = [];
  feed = [];
  hosted_events = [];
  attending_events = [];
  contentReady: Promise<boolean>;

  //Dynamic calendar icon
  Months = ['U curious?','JAN','FEB','MAR','APR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DEC'];



  constructor(private feedcrudService: FeedCrudService, private eventcrudService: EventCrudService, private router: Router) {}

  ngOnInit() {
  	//this.feedcrudService.getFeedEvents()
    this.eventcrudService.getEvents()
  		.subscribe(data => {
	  		this.events = data;
  		})
    this.feedcrudService.getFeedEvents()
      .subscribe(data => {
        this.feed = data.events_feed;
        this.hosted_events = data.hosted_events;
        this.attending_events = data.attending_events;
      })
    this.contentReady = Promise.resolve(true);
	}

  removeEvent(events,) {
    if (window.confirm('Are you sure')) {
      this.eventcrudService.deleteEvent(events.id)
      .subscribe(() => {
          console.log('Event deleted!')
        }
      )
    }
  }

  eventDetail(events) {
      this.eventcrudService.getEvent(events.id)
    this.router.navigate(['/eventdetail/events.id']);
  }

}


