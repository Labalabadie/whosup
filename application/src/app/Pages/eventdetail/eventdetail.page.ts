import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from "@angular/router";
import { User, UserCrudService } from 'src/app/Data(services)/userCrud.services';
import { Event, EventCrudService } from 'src/app/Data(services)/eventCrud.services';
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
	event: Event;
	currentUser: User;
	currentUserId: number = 2; // <---- HARDCODEADO
	eventCreator: User;
	joined: boolean = false;
	contentReady: Promise<boolean>;
	date: string = "";
	time: string = "";

	constructor(private eventCrudService: EventCrudService,
		private activatedRoute: ActivatedRoute,
		private router: Router,
		private userCrudService: UserCrudService,
	) {
		this.id = parseInt(this.activatedRoute.snapshot.paramMap.get('id'));
	}

	ngOnInit() {
		this.eventCrudService.getEvent(this.id)
			.subscribe(data => {
				this.event = data; // Here comes the data 
				this.date = data.event_datetime.split('T')[0];
				this.time = data.event_datetime.split('T')[1].split(":").slice(0, 2).join(":");

				this.userCrudService.getUser(this.event.event_host_id)
				.subscribe(eventCreatorData => {
					this.eventCreator = eventCreatorData; 

					this.userCrudService.getUser(this.currentUserId) // <---- HARDCODEADO
					.subscribe(currentUserData => {
						this.currentUser = currentUserData;
						if (this.event.participants
							.find(x => x.id == this.currentUser.id) != null) {this.joined = true} // check if already joined
						this.contentReady = Promise.resolve(true); // Now you can load the page :)
					})
				})
			})
	}

	joinChange() {
    	var button = document.getElementById("joinbtn");
    	var currentClass = button.className;
    	if (currentClass == "join-button") { // Check the current class name
        	button.className = "unjoin-button";   // Set other class name
			document.getElementById("joinbtn").innerHTML = "Joined";
			this.eventCrudService.joinEvent(this.id, 2) // <---- HARDCODEADO
			.subscribe(() => {window.location.reload()})
    	} else {
        	button.className = "join-button";  // Otherwise, continue using the default class
			document.getElementById("joinbtn").innerHTML = "Join";
			this.eventCrudService.unjoinEvent(this.id, 2)   // <---- HARDCODEADO
			.subscribe(() => {window.location.reload()})
    	}
	}

	removeEvent(id = this.event.id) {
		if (window.confirm('Are you sure')) {
		  	this.eventCrudService.deleteEvent(id)
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
