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
    return this.http.get(this.productUrl+"?format=json")
  }

  editProduct(product: any): Observable<any> {
    const url = `${this.productUrl}/${product.id}`;
    return this.http.put<any>(url, product);
  }

  
  createProduct(productData: any): Observable<any> {
    return this.http.post(this.productUrl, productData);
  }
  deleteProduct(productId: number): Observable<any> {
    const url = `${this.productUrl}/${productId}?format=json`;
    return this.http.delete<any>(url);
  }


  
}
  