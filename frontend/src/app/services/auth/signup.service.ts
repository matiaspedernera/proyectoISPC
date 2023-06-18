import { Injectable } from '@angular/core';
import { SignupRequest } from './signupRequest';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SignupService {
  private url: string = 'http://127.0.0.1:8000/api/auth/signup/';
  constructor(private http: HttpClient) {}

  signup(credentials: SignupRequest): Observable<any> {
    return this.http.post(this.url, credentials);
  }
}
