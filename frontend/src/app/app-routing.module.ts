import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NosotrosComponent } from './pages/nosotros/nosotros.component';
import { ContactanosComponent } from './pages/contactanos/contactanos.component';
import { PerfilComponent } from './auth/perfil/perfil.component';
import { CartaComponent } from './pages/carta/carta.component';
import { HomeComponent } from './pages/home/home.component';

const routes: Routes = [
  {path: '', redirectTo:'/home', pathMatch:'full'},
  {path: 'home', component:HomeComponent},
  {path: 'nosotros', component:NosotrosComponent},
  {path: 'contactanos', component:ContactanosComponent},
  {path: 'perfil', component:PerfilComponent},
  {path: 'carta', component:CartaComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
