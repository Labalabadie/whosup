import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

export class Event {
  id: number;
	name: string;
	event_host_id: number;
	event_datetime: string;
	location: string;
	description: string;
	icon: string;
	max_people: number;
	participants: JSON;
	group_id: number;
	channel_id: number;
	config: JSON;
	status: boolean;
}

@Injectable({
  providedIn: 'root'
})

export class EventCrudService {

  endpoint = 'http://54.221.93.106:8000/event';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private httpClient: HttpClient) { }

  createEvent(Event: Event): Observable<any> {
    return this.httpClient.post<Event>(this.endpoint, JSON.stringify(Event), this.httpOptions)
      .pipe(
        catchError(this.handleError<Event>('Error occured'))
      );
  }

  getEvent(id): Observable<Event[]> {
    return this.httpClient.get<Event[]>(this.endpoint + '/' + id)
      .pipe(
        tap(_ => console.log(`Event fetched: ${id}`)),
        catchError(this.handleError<Event[]>(`Get Event id=${id}`))
      );
  }

  getEvents(): Observable<Event[]> {
    return this.httpClient.get<Event[]>(this.endpoint)
      .pipe(
        tap(Events => console.log('Events retrieved!')),
        catchError(this.handleError<Event[]>('Get Event', []))
      );
  }

  updateEvent(id, Event: Event): Observable<any> {
    return this.httpClient.put(this.endpoint + '/' + id, JSON.stringify(Event), this.httpOptions)
      .pipe(
        tap(_ => console.log(`Event updated: ${id}`)),
        catchError(this.handleError<Event[]>('Update Event'))
      );
  }

  deleteEvent(id): Observable<Event[]> {
    return this.httpClient.delete<Event[]>(this.endpoint + '/' + id, this.httpOptions)
      .pipe(
        tap(_ => console.log(`Event deleted: ${id}`)),
        catchError(this.handleError<Event[]>('Delete Event'))
      );
  }


  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      console.log(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }  
  
}