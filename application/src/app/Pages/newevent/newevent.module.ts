import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { NeweventPageRoutingModule } from './newevent-routing.module';

import { NeweventPage } from './newevent.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    NeweventPageRoutingModule,
    ReactiveFormsModule
  ],
  declarations: [NeweventPage]
})
export class NeweventPageModule {}
