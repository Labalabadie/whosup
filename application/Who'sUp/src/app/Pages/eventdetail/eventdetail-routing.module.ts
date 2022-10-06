import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { EventdetailPage } from './eventdetail.page';

const routes: Routes = [
  {
    path: '',
    component: EventdetailPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class EventdetailPageRoutingModule {}
