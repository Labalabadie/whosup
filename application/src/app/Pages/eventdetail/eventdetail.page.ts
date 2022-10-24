import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from "@angular/router";
import { EventCrudService } from 'src/app/Data(services)/eventCrud.services';
import { FormGroup, FormBuilder } from "@angular/forms";

@Component({
  selector: 'app-eventdetail',
  templateUrl: './eventdetail.page.html',
  styleUrls: ['./eventdetail.page.scss'],
})
export class EventdetailPage implements OnInit {

  
  //Dynamic calendar icon
	Months = ['U curious?','JAN','FEB','MAR','APR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DEC'];
  id: number;
  event: any = null;
  contentReady: Promise<boolean>;
  date: string = "";
  time: string = "";

  constructor(private eventcrudService: EventCrudService,
              private activatedRoute: ActivatedRoute,
              private router: Router
  ) {
    this.id = parseInt(this.activatedRoute.snapshot.paramMap.get('id'));
  }

  ngOnInit() {
	console.log(this.id)
  this.eventcrudService.getEvent(this.id)
    .subscribe(data => {
      this.event = data;
      this.date = data.event_datetime.split('T')[0]
      this.time = data.event_datetime.split('T')[1].split(":").slice(0, 2).join(":")
      this.contentReady = Promise.resolve(true);
    })
}
}
