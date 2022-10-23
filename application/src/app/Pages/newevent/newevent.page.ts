import { Component, OnInit, NgZone } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, FormControl } from "@angular/forms";
import { EventCrudService } from '../../Data(services)/eventCrud.services';

@Component({
  selector: 'app-create',
  templateUrl: './newevent.page.html',
  styleUrls: ['./newevent.page.scss'],
})


export class NeweventPage implements OnInit {

  eventForm: FormGroup;

  constructor(
    private router: Router,
    public formBuilder: FormBuilder,
    private zone: NgZone,
    private userCrudService: EventCrudService    
  ) {
    this.eventForm = this.formBuilder.group({
			id: 0,
      name: [''],
      event_datetime: [''],
      location: [''],
			max_people: [''],
			participants: [],
      image_URL: '',
			event_host_id: 1,
      description: [''],
			group_id: [],
			channel_id: [],
			config: {}
    })
  }


  
  ngOnInit() {
    let x = document.getElementById("event-image-button");
    x.addEventListener("focusout", this.refreshImg);
  }

  onSubmit() {
    if (!this.eventForm.valid) {
      return false;
    } else {
      this.userCrudService.createEvent(this.eventForm.value)
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


  refreshImg(value) {
    let x = document.getElementById("event-image-button") as HTMLImageElement;
    x.src = this.eventForm.value.image_URL;
    console.log(x.src);
  }
}

