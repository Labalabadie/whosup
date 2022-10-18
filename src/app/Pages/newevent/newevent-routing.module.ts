import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NeweventPage } from './newevent.page';

const routes: Routes = [
  {
    path: '',
    component: NeweventPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes), FormsModule],
  exports: [RouterModule],
})
export class NeweventPageRoutingModule {}
