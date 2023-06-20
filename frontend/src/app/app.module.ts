import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NgxPayPalModule } from 'ngx-paypal';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NosotrosComponent } from './pages/nosotros/nosotros.component';
import { FooterComponent } from './shared/footer/footer.component';
import { ContactanosComponent } from './pages/contactanos/contactanos.component';
import { CartaComponent } from './pages/carta/carta.component';
import { HeaderComponent } from './shared/header/header.component';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './auth/login/login.component';
import { SignupComponent } from './auth/signup/signup.component';
import { ProductosComponent } from './pages/productos/productos.component';
<<<<<<< HEAD
import { FormsModule } from '@angular/forms';
=======
import { PagoComponent } from './pages/pago/pago.component';
import { PedidosComponent } from './pages/pedidos/pedidos.component';

>>>>>>> e5bc4c1211f0b5c6516e687c77371ff0fa8256bb
@NgModule({
  declarations: [
    AppComponent,
    CartaComponent,
    NosotrosComponent,
    FooterComponent,
    ContactanosComponent,
    HeaderComponent,
    HomeComponent,
    LoginComponent,
    SignupComponent,
    ProductosComponent,
    PagoComponent,
    PedidosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
<<<<<<< HEAD
    FormsModule
=======
    FormsModule,
<<<<<<< HEAD
>>>>>>> f22d2dd3ec8d0aa82fb2c3e8ed994a56104b1444
=======
    NgxPayPalModule
>>>>>>> e5bc4c1211f0b5c6516e687c77371ff0fa8256bb
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }
