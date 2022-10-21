import { Component, OnInit } from '@angular/core';
import { EventCrudService } from 'src/app/Data(services)/eventCrud.services';

@Component({
  selector: 'app-eventdetail',
  templateUrl: './eventdetail.page.html',
  styleUrls: ['./eventdetail.page.scss'],
})
export class EventdetailPage implements OnInit {

 

  events = [];

  constructor(private eventcrudService: EventCrudService) { }

  ngOnInit() {
   
      this.eventcrudService.getEvent
    
    


}

}
