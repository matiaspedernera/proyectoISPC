import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GetProductsService {
<<<<<<< HEAD
  url:string= "http://127.0.0.1:8000/";
  productUrl:string = "http://127.0.0.1:8000/producto"
  constructor(private http:HttpClient) { }
 
=======
  products: any[] = [];
  url: string = "http://127.0.0.1:8000/";
  productUrl: string = "http://127.0.0.1:8000/producto"
  constructor(private http: HttpClient) { }
>>>>>>> f22d2dd3ec8d0aa82fb2c3e8ed994a56104b1444

  

<<<<<<< HEAD
  getProducts(): Observable <any> {
    return this.http.get(this.productUrl+"?format=json")
=======
  getProducts(): Observable<any> {
    return this.http.get(this.url + "producto?format=json")
  }

  getProduct() {
    return this.products;
>>>>>>> f22d2dd3ec8d0aa82fb2c3e8ed994a56104b1444
  }

  editProduct(product: any): Observable<any> {
    const url = `${this.productUrl}/${product.id}`;
    return this.http.put<any>(url, product);
  }

  
  createProduct(productData: any): Observable<any> {
    return this.http.post(this.productUrl, productData);
  }
<<<<<<< HEAD
  deleteProduct(productId: number): Observable<any> {
    const url = `${this.productUrl}/${productId}?format=json`;
    return this.http.delete<any>(url);
  }


  
=======

  saveProducts() {
    localStorage.setItem('productos_carrito', JSON.stringify(this.products));
  }

  addProductToCart(product: any) {
    this.products.push(product);
    this.saveProducts();
  }

  loadProductsInCart() {
    this.products = JSON.parse(localStorage.getItem('productos_carrito') as any) || [];
  }

  productInCart(product: any) {
    return this.products.findIndex((x: any) => x.id === product.id) > -1;
  }

  removeProduct(product: any) {
    const index = this.products.findIndex((x: any) => x.id === product.id)

    if (index > -1) {
      this.products.splice(index, 1);
      this.saveProducts();
    }
  }
<<<<<<< HEAD
>>>>>>> f22d2dd3ec8d0aa82fb2c3e8ed994a56104b1444
=======

  clearProducts() {
    this.products = [];
    localStorage.clear();
  }
>>>>>>> e5bc4c1211f0b5c6516e687c77371ff0fa8256bb
}
  