import { Component } from '@angular/core';

@Component({
  selector: 'perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent {
  viewSignIn:boolean=false;

  cambiarVista() {
    this.viewSignIn = !this.viewSignIn;
  }
}
