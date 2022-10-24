import { Component, OnInit, NgZone } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, FormControl, Validators } from "@angular/forms";
import { EventCrudService } from '../../Data(services)/eventCrud.services';
import { User, UserCrudService } from 'src/app/Data(services)/userCrud.services';

@Component({
  selector: 'app-create',
  templateUrl: './newevent.page.html',
  styleUrls: ['./newevent.page.scss'],
})


export class NeweventPage implements OnInit {

  eventForm: FormGroup;
  currentUser: User;
  contentReady: Promise<boolean>;
  imgChanged: boolean = false;

  constructor(
    private router: Router,
    public formBuilder: FormBuilder,
    private zone: NgZone,
    private eventCrudService: EventCrudService,  
    private userCrudService: UserCrudService,  
     
  ) {
    this.eventForm = this.formBuilder.group({
			id: 0,
      name: [''],
      event_datetime: [''],
      location: [''],
			max_people: [''],
			image_URL: "",
			participants: [],
			event_host_id: 1, // HARDCODEADO <--
      description: [''],
			group_id: [],
			channel_id: [],
			config: {}
    })
  }

  ngOnInit() {
    this.userCrudService.getUser(2) // HARDCODEADO <-
      .subscribe(data => {
        this.currentUser = data;
        this.eventForm.value.image_URL = data.image_URL;
        this.contentReady = Promise.resolve(true);
      })
  }

  onSubmit() {
    if (this.imgChanged == false) {
      this.eventForm.value.image_URL = this.currentUser.image_URL;
    }
    console.log(this.eventForm.value.image_URL);
    if (!this.eventForm.valid) {
      return false;
    } else {
			this.eventForm.value.event_datetime = this.date + 'T' + this.time;
      this.eventCrudService.createEvent(this.eventForm.value)
        .subscribe((response) => {
          this.zone.run(() => {
            this.eventForm.reset();
            this.router.navigate(['/home']);
          })
        });
    }
  }

	btn1: boolean=true;
	btn2: boolean=false;

  togglebutton(){
    this.btn1 = !this.btn1;
		this.btn2 = !this.btn2;
  }

	showfield = {
    place : true,
    online : false
  }

	date = 'Select a date';
	time = 'Select time';

	dateChanged(value){
		this.date = value.split("T", 1)[0];
		console.log(this.date);
	}
	timeChanged(value){
		const pattern = new RegExp('[+-]');
		this.time = value.split("T", 2)[1].split(pattern, 2)[0];
		console.log(this.time);
	}

  refreshImg() {
    this.imgChanged = true;
    let x = document.getElementById("event-image-button") as HTMLImageElement;
    x.src = this.eventForm.value.image_URL;
  }
}
