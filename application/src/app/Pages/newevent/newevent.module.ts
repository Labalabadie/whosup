import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { NeweventPageRoutingModule } from './newevent-routing.module';

import { NeweventPage } from './newevent.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    NeweventPageRoutingModule
  ],
  declarations: [NeweventPage]
})
export class NeweventPageModule {}
