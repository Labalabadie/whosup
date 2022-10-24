import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

export class User {
  id: number;
	name: string;
	email: string;
	phone: number;
	image_URL: string;
	password: string;
	checkpassword: string;
	created_at: string;
	updated_at: string;
	status: boolean;
}

@Injectable({
  providedIn: 'root'
})

export class UserCrudService {

  endpoint = 'http://34.229.7.213:8000/user';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private httpClient: HttpClient) { }

  createUser(User: User): Observable<any> {
    return this.httpClient.post<User>(this.endpoint, JSON.stringify(User), this.httpOptions)
      .pipe(
        catchError(this.handleError<User>('Error occured'))
      );
  }

	getUser(id): Observable<User> {
    return this.httpClient.get<User>(this.endpoint + '/' + id)
      .pipe(
        tap(_ => console.log(`User fetched: ${id}`)),
        catchError(this.handleError<User>(`Get User id=${id}`))
      );
  }

  getUsers(): Observable<User[]> {
    return this.httpClient.get<User[]>(this.endpoint)
      .pipe(
        tap(Users => console.log('Users retrieved!')),
        catchError(this.handleError<User[]>('Get User', []))
      );
  }

  updateUser(id, User: User): Observable<any> {
    return this.httpClient.put(this.endpoint + '/' + id, JSON.stringify(User), this.httpOptions)
      .pipe(
        tap(_ => console.log(`User updated: ${id}`)),
        catchError(this.handleError<User[]>('Update User'))
      );
  }

  deleteUser(id): Observable<User[]> {
    return this.httpClient.delete<User[]>(this.endpoint + '/' + id, this.httpOptions)
      .pipe(
        tap(_ => console.log(`User deleted: ${id}`)),
        catchError(this.handleError<User[]>('Delete User'))
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