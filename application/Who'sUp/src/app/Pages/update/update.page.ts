import { Component, OnInit } from '@angular/core';

import { Router, ActivatedRoute } from "@angular/router";
import { FormGroup, FormBuilder } from "@angular/forms";
import { EventCrudService } from 'src/app/Data(services)/eventCrud.services';


@Component({
  selector: 'app-update',
  templateUrl: './update.page.html',
  styleUrls: ['./update.page.scss'],
})

export class UpdatePage implements OnInit {

  updateEventFg: FormGroup;
  id: any;

  constructor(
    private eventcrudService: EventCrudService,
    private activatedRoute: ActivatedRoute,
    public formBuilder: FormBuilder,
    private router: Router
  ) {
    this.id = this.activatedRoute.snapshot.paramMap.get('id');
  }
  

  ngOnInit() {                                 
    this.fetchEvent(this.id);
    this.updateEventFg = this.formBuilder.group({
        event_name: [''],
        event_datetime: [''],
        location: [''],
        participants: [],
        description: ['']
    })
  }

  fetchEvent(id) {
    this.eventcrudService.getEvent(id).subscribe((data) => {
      this.updateEventFg.setValue({
        event_name: data['event_name'],
        event_datetime: data['event_datetime'],
        location: data['location'],
        participants: data['participants'],
        description: data['description'],
        
      });
    });
  }

  onSubmit() {
    if (!this.updateEventFg.valid) {
      return false;
    } else {
      this.eventcrudService.updateEvent(this.id, this.updateEventFg.value)
        .subscribe(() => {
          this.updateEventFg.reset();
          this.router.navigate(['/home']);
        })
    }
  }

}