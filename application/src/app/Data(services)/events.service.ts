import { Injectable } from '@angular/core';
import { HttpClient,HttpRequest, } from '@angular/common/http';
import { Event } from '../Models/event.model';


@Injectable({
  providedIn: 'root'
})
export class EventsService {
  detail: Event = {};
  events: Event[] = [];
  

  constructor(private http: HttpClient) { }

  getEvents() {
	  return this.http.get<any>('http://localhost:8000/events')

  }

  //postEvents() {
    //return this.http.post("http://localhost/events", postData, requestOptions)
    
  //}
}