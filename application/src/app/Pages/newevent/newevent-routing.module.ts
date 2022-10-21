import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { NeweventPage } from './newevent.page';

const routes: Routes = [
  {
    path: '',
    component: NeweventPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class NeweventPageRoutingModule {}
