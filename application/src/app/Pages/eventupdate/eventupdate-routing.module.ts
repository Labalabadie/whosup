import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EventUpdatePage } from './eventupdate.page';

const routes: Routes = [
  {
    path: '',
    component: EventUpdatePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})

export class EventUpdatePageRoutingModule {}
