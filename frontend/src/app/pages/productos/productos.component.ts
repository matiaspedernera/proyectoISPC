import { Component } from '@angular/core';
import { Form, FormBuilder, Validators } from '@angular/forms';
import { GetProductsService } from 'src/app/services/get-products.service';

@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css']
})
export class ProductosComponent {
  productForm = this.formBuilder.group({
    nombre: ['', Validators.required],
    descripcion: ['', Validators.required],
    precio: ['', Validators.required],
    stock: ['', Validators.required],
    imagen: ['', Validators.required],
    activo: ['', Validators.required],
    categoria: ['', Validators.required],
  })

  constructor(
    private formBuilder: FormBuilder,
    private productService : GetProductsService,
  ) {}

  get nombre() {
    return this.productForm.controls.nombre;
  }
  get descripcion() {
    return this.productForm.controls.descripcion;
  }
  get precio() {
    return this.productForm.controls.precio;
  }
  get stock() {
    return this.productForm.controls.stock;
  }
  get imagen() {
    return this.productForm.controls.imagen;
  }
  get activo() {
    return this.productForm.controls.activo;
  }
  get categoria() {
    return this.productForm.controls.categoria;
  }

  crearProducto() {
    if (this.productForm.valid) {
      this.productService.createProduct(this.productForm.value).subscribe({
        error: (errorData) => {
          console.error(errorData);
        },
        complete: () => {
          console.log("Producto creado");
        }
      })
    }else {
      this.productForm.markAllAsTouched();
      alert('No se permiten campos vacios.');
    }
  }

}
