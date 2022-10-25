import { Component, OnInit } from '@angular/core';
import { EventCrudService } from 'src/app/Data(services)/eventCrud.services';
import { Router, ActivatedRoute } from "@angular/router";

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
				this.event = data; // Here comes the data 
				this.date = data.event_datetime.split('T')[0];
				this.time = data.event_datetime.split('T')[1].split(":").slice(0, 2).join(":");
				this.contentReady = Promise.resolve(true); // Now you can load the page :)
			})
	}

	joinChange(){
    var button = document.getElementById("joinbtn");
    var currentClass = button.className;
    if (currentClass == "join-button") { // Check the current class name
        button.className = "unjoin-button";   // Set other class name
				document.getElementById("joinbtn").innerHTML = "+1";
    } else {
        button.className = "join-button";  // Otherwise, continue using the default class
				document.getElementById("joinbtn").innerHTML = "Join";
    }
}  

}
