import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from "@angular/router";
import { FormGroup, FormBuilder } from "@angular/forms";
import { Event, EventCrudService } from 'src/app/Data(services)/eventCrud.services';
import { UserCrudService } from 'src/app/Data(services)/userCrud.services';
import { max } from 'rxjs/operators';

@Component({
  selector: 'app-update',
  templateUrl: './eventupdate.page.html',
  styleUrls: ['./eventupdate.page.scss'],
})

export class EventUpdatePage implements OnInit {

  updateEventForm: FormGroup;
  id: any;
  contentReady: Promise<boolean>;
  imgChanged: boolean = false;
  event: Event;
  

  constructor(
    private userCrudService: UserCrudService,
    private eventCrudService: EventCrudService,
    private activatedRoute: ActivatedRoute,
    public formBuilder: FormBuilder,
    private router: Router
  ) {
    this.id = this.activatedRoute.snapshot.paramMap.get('id');
    this.updateEventForm = this.formBuilder.group({
      id: this.id,
      event_host_id: 2, // HARDCODEADO <----
      name: '',
      event_datetime: [''],
      location: [''],
      image_URL: '',
      description: [''],
      max_people: '',
      people_count: ''
  })
  }
  

  ngOnInit() {                                 
    this.eventCrudService.getEvent(this.id).subscribe((data) => {
      this.updateEventForm.setValue({
        id: this.id,
        event_host_id: 2, // HARDCODEADO <----
        name: data['name'],
        event_datetime: data['event_datetime'],
        location: data['location'],
        image_URL: data['image_URL'],
        max_people: data['max_people'],
        people_count: data['people_count'],
        description: data['description'],
      });
      this.event = data;
    });
    this.contentReady = Promise.resolve(true);
    console.log(this.event)
  }

  fetchEvent(id) {
    this.eventCrudService.getEvent(id).subscribe((data) => {
      this.updateEventForm.setValue({
        name: data['event_name'],
        event_datetime: data['event_datetime'],
        location: data['location'],
        image_URL: data['image_URL'],
        max_people: data['max_people'],
        people_count: data['people_count'],
        description: data['description'],
      });
    });
  }

  onSubmit() {
    if (!this.updateEventForm.valid) {
      return false;
    } else {
      this.eventCrudService.updateEvent(this.id, this.updateEventForm.value)
        .subscribe(() => {
          this.updateEventForm.reset();
          this.router.navigate(['/home']);
        })
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
    x.src = this.updateEventForm.value.image_URL;
  }
}