import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NosotrosComponent } from './nosotros/nosotros.component';
import { ContactanosComponent } from './contactanos/contactanos.component';
import { PerfilComponent } from './perfil/perfil.component';

const routes: Routes = [
  {path: 'nosotros', component:NosotrosComponent},
  {path: 'contactanos', component:ContactanosComponent},
  {path: 'perfil', component:PerfilComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
