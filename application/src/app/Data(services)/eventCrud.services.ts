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
	participants: any;
	group_id: number;
	channel_id: number;
	config: JSON;
	status: boolean;
}

export class EventJoin {
  event_id: '';
  user_id: '';
}

@Injectable({
  providedIn: 'root'
})

export class EventCrudService {

  endpoint = 'http://34.229.7.213:8000/event';

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

  getEvent(id): Observable<Event> {
    return this.httpClient.get<Event>(this.endpoint + '/' + id)
      .pipe(
        tap(_ => console.log(`Event fetched: ${id}`)),
        catchError(this.handleError<Event>(`Get Event id=${id}`))
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

  deleteEvent(id): Observable<Event> {
    return this.httpClient.delete<Event>(this.endpoint + '/' + id, this.httpOptions)
      .pipe(
        tap(_ => console.log(`Event deleted: ${id}`)),
        catchError(this.handleError<Event>('Delete Event'))
      );
  }

  joinEvent(event_id, user_id): Observable<any> {
    console.log('TEST')
    return this.httpClient.post<EventJoin>(this.endpoint + '/' + event_id + '/join' + '?user_id=' + user_id, this.httpOptions)
    .pipe(
      catchError(this.handleError<Event>('Error occured'))
    );
  }

  unjoinEvent(event_id, user_id): Observable<any> {
    console.log('UNTEST')
    return this.httpClient.delete<EventJoin>(this.endpoint + '/' + event_id + '/join' + '?user_id=' + user_id, this.httpOptions)
    .pipe(
      catchError(this.handleError<Event>('Error occured'))
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