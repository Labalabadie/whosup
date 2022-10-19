import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { EventdetailPageRoutingModule } from './eventdetail-routing.module';

import { EventdetailPage } from './eventdetail.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    EventdetailPageRoutingModule
  ],
  declarations: [EventdetailPage]
})
export class EventdetailPageModule {}
