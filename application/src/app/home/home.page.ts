import { Component, OnInit } from '@angular/core';
import { EventCrudService } from '../Data(services)/eventCrud.services';
import { FeedCrudService } from '../Data(services)/feedCrud.services';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {

  events = [];
  //Dynamic calendar icon
  Months = ['U curious?','JAN','FEB','MAR','APR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DEC'];


  constructor(private feedcrudService: FeedCrudService, private router: Router) {}

  ngOnInit() {
  	this.feedcrudService.getFeedEvents()
  		.subscribe(data => {
	  		this.events = data;
  		})

	}
  
/*
  removeEvent(events,) {
    if (window.confirm('Are you sure')) {
      this.eventcrudService.deleteEvent(events.id)
      .subscribe(() => {
          console.log('Event deleted!')
        }
      )
    }
  }
*/
 // eventDetail(events) {
 //     this.eventcrudService.getEvent(events.id)
 //   this.router.navigate(['/eventdetail']);
 // }


}


