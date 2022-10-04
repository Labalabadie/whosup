import { Component, OnInit } from '@angular/core';
import { EventsService } from '../Data(services)/events.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {

  events = [];

  constructor(private eventService: EventsService) {}

  ngOnInit() {
  	this.eventService.getEvents()
  		.subscribe(data => {
	  		this.events = data;
  		})
	}
}
