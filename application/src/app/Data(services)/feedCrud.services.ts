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
export class Feed {

    my_events: {"attending_events": JSON, "hosted_events": JSON};
}
@Injectable({
  providedIn: 'root'
})

export class FeedCrudService {

  endpoint = 'http://localhost:8000/user/';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private httpClient: HttpClient) { }

  getFeedEvents(): Observable<Feed[]> {
    return this.httpClient.get<Feed[]>(this.endpoint + '2' + '/feed')
      .pipe(
        tap(Events => console.log('Events retrieved!')),
        catchError(this.handleError<Feed[]>('Get Feed', []))
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