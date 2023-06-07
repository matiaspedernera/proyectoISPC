import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GetProductsService {
  url:string= "http://127.0.0.1:8000/";
  productUrl:string = "http://127.0.0.1:8000/producto"
  constructor(private http:HttpClient) { }


  getProducts(): Observable <any> {
    return this.http.get(this.url+"producto?format=json")
  }

  createProduct(productData: any): Observable<any> {
    return this.http.post(this.productUrl, productData);
  }
}
