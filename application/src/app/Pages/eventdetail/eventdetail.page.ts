import { Component, OnInit } from '@angular/core';
import { EventCrudService } from 'src/app/Data(services)/eventCrud.services';

@Component({
  selector: 'app-eventdetail',
  templateUrl: './eventdetail.page.html',
  styleUrls: ['./eventdetail.page.scss'],
})
export class EventdetailPage implements OnInit {

  //Dynamic calendar icon
	Months = ['U curious?','JAN','FEB','MAR','APR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DEC'];

  events = [];

  constructor(private eventcrudService: EventCrudService) { }

  ngOnInit() {
	
  this.eventcrudService.getEvent
}
}
