import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GetProductsService {
  url:String= "http://localhost:3000/";
  constructor(private http:HttpClient) { }


  getProducts(): Observable <any> {
    return this.http.get(this.url+"products")
  }
}
