import { Component, OnInit, NgZone } from '@angular/core';

import { Router } from '@angular/router';
import { FormGroup, FormBuilder } from "@angular/forms";
import { EventCrudService } from 'src/app/Data(services)/eventCrud.services';

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
      event_name: [''],
      event_datetime: [''],
      location: [''],
      description: [''],
      participants: [''],
      event_status: [''],
      nonolist: ['']
    })
  }

  ngOnInit() { }

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

}