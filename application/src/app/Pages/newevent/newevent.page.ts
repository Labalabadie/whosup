import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Event } from 'src/app/Models/event.model';
import { EventsService } from 'src/app/Data(services)/events.service';
import { Storage } from '@capacitor/storage';

@Component({
  selector: 'app-newevent',
  templateUrl: './newevent.page.html',
  styleUrls: ['./newevent.page.scss'],
})
export class NeweventPage implements OnInit {

  event: Event = {};

  constructor(private eventsService: EventsService,
    private router: Router) { }

  ngOnInit() {
    
  }

//  savenewEvent(){
	  //this.pedidoService.agrPedido(fecha.value, nombre.value, barrio.value, direccion.value, telefono.value, productos.value, comentarios.value);
	  //if(this.eventsService.events == null){
	//	  this.eventsService.events = []
//	  }
	//  this.eventsService.events.push(this.event);
//	const key = 'events';
//	  Storage.set({key, value:JSON.stringify(this.eventsService.events)});
 //   this.eventsService.sendPostRequest();
//	  this.router.navigate(["/home"]);

}
