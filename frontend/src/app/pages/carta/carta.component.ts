import { Component, OnInit } from '@angular/core';
import { GetProductsService } from 'src/app/services/get-products.service';

@Component({
  selector: 'app-carta',
  templateUrl: './carta.component.html',
  styleUrls: ['./carta.component.css']
})
export class CartaComponent implements OnInit{
  products: any;

  constructor(private product: GetProductsService) {
    this.product.getProducts().subscribe({
      next: (productsData) => {
        this.products=productsData
        console.log(productsData)
      },
      error: (errorData) => {
        console.error(errorData);
      }
    })
  }

  ngOnInit(): void {
    // TODO document why this method 'ngOnInit' is empty
  
    
  }
}
