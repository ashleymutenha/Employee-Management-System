import { Injectable } from '@angular/core';
import {HttpClient,HttpHeaders} from '@angular/common/http'
import {throwError as observableThrowError, Observable} from 'rxjs'
import {catchError} from 'rxjs/operators'
import {Message} from './users'

const headers = new HttpHeaders({'Content-Type':'application/json'})

@Injectable({
  providedIn: 'root'
})
export class PeopleService {

  public add_url = "http://127.0.0.1:5000/addUsers"
  public add_url2 ="http://127.0.0.1:5000/getMessage"

  constructor(private http:HttpClient) { }

  addUsers(data:any):Observable<any>{
    return this.http.post<any>(this.add_url,JSON.stringify(data),{'headers':headers})
  }

  getMessage():Observable<Message[]>{
    return this.http.get<Message[]>(this.add_url2)
  }
}
