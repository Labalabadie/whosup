import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Event } from '../Models/event.model';


@Injectable({
  providedIn: 'root'
})
export class GetEventsService {
  detail: Event = {};
  events: Event[] = [];
  

  constructor(private http: HttpClient,) { }

  getEvents() {
	  return this.http.get<any>('http://localhost:8000/events')

  }

}