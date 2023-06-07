import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  registerForm = this.formBuilder.group({
    nombreApellido:['',Validators.required],
    identificacion:['',Validators.maxLength(8)],
    email: ['', [Validators.required, Validators.email]],
    password: ['', Validators.required],
  });

  constructor(
    private formBuilder: FormBuilder,
    private router: Router
  ) {}

  get nombreApellido() {
    return this.registerForm.controls.nombreApellido;
  }
  get identificacion() {
    return this.registerForm.controls.identificacion;
  }
  get email() {
    return this.registerForm.controls.email;
  }
  get password() {
    return this.registerForm.controls.password;
  }

  register() {
    if (this.registerForm.valid) {
      
    } else {
      this.registerForm.markAllAsTouched();
      alert('No se permiten campos vacios.');
    }
  }

}
