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
	currentUserId = 2;
	eventJoined: boolean = false;

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
				this.eventJoined = this.event.value.participants.find(element => {
					if (element.id == this.currentUserId) {return true}
					return false;
				});
			})

		var button = document.getElementById("joinbtn");
		if (this.eventJoined == true) {
			button.className = "unjoin-button";
		} else { button.className = "join-button"}
	}

	joinChange(){
    	var button = document.getElementById("joinbtn");
    	var currentClass = button.className;
    	if (currentClass == "join-button") { // Check the current class name
        	button.className = "unjoin-button";   // Set other class name
			document.getElementById("joinbtn").innerHTML = "Joined";
			this.eventcrudService.joinEvent(this.id, 2)
			.subscribe(() => {window.location.reload()})
    	} else {
        	button.className = "join-button";  // Otherwise, continue using the default class
			document.getElementById("joinbtn").innerHTML = "Join";
			this.eventcrudService.unjoinEvent(this.id, 2)
			.subscribe(() => {window.location.reload()})
    	}
	}  

	removeEvent(id = this.event.id) {
		if (window.confirm('Are you sure')) {
		  	this.eventcrudService.deleteEvent(id)
		  	.subscribe(() => {
			  	console.log('Event deleted!');
				this.router.navigateByUrl('/home')  
				.then(() => {
					window.location.reload();
				  });
				}
		  	)
		}
	}
}
