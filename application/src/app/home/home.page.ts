import { Component, OnInit } from '@angular/core';
import { EventCrudService } from '../Data(services)/eventCrud.services';
import { Router } from '@angular/router';
import { AuthService } from '../Data(services)/auth.services';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {

  message = '';
  isLoadingResults = false;

  events = [];
  //Dynamic calendar icon
  Months = ['U curious?','JAN','FEB','MAR','APR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DEC'];



  constructor(private eventcrudService: EventCrudService, private router: Router, private authService: AuthService) {}

  ngOnInit(): void {
    this.isLoadingResults = true;
    this.authService.secured()
      .subscribe((data: any) => {
        this.message = data;
        console.log(data);
        this.isLoadingResults = false;
      });

  	this.eventcrudService.getEvents()
  		.subscribe(data => {
	  		this.events = data;
  		})
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

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']).then(_ => console.log('Logout'));
  }

}


