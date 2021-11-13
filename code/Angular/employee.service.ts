import { Injectable } from '@angular/core';
import {throwError as observableThrowError, Observable} from 'rxjs'
import {catchError} from 'rxjs/operators'
import {HttpClient,HttpErrorResponse,HttpHeaders} from '@angular/common/http'
import {Login,Details}from './employees'

const headers= new HttpHeaders({'Content-Type':'application/json'})
@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

 public detail:string ="http://127.0.0.1:5000/getDetails"
 public add_users:string ="http://127.0.0.1:5000/addUsers"
 public login:string="http://127.0.0.1:5000/login"
 public delete:string="http://127.0.0.1:5000/delete_user"
  constructor(private http:HttpClient) { }

  getDetails():Observable<Details[]>{
    return this.http.get<Details[]>(this.detail).pipe(
      catchError(this.errorHandler))
  }

  _login(data:any):Observable<any>{
    return this.http.post<any>(this.login,JSON.stringify(data),{'headers':headers}).pipe(
      catchError(this.errorHandler))
  }

   _delete(data:any):Observable<any>{
    return this.http.post<any>(this.delete,JSON.stringify(data),{'headers':headers}).pipe(
      catchError(this.errorHandler))
  }

 
  errorHandler(error:HttpErrorResponse){

    return observableThrowError(error.message ||"Server Down")

  }
  }


