import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'start',
    loadChildren: () => import('./Pages/start/start.module').then( m => m.StartPageModule)
  },
  {
    path: 'login',
    loadChildren: () => import('./Pages/login/login.module').then( m => m.LoginPageModule)
  },
  {
    path: 'signup',
    loadChildren: () => import('./Pages/signup/signup.module').then( m => m.SignupPageModule)
  },
  {
    path: 'newevent',
    loadChildren: () => import('./Pages/newevent/newevent.module').then( m => m.NeweventPageModule)
  },
  {
    path: 'event/detail/:id',
    loadChildren: () => import('./Pages/eventdetail/eventdetail.module').then( m => m.EventdetailPageModule)
  },
  {
    path: 'event/update/:id',
    loadChildren: () => import('./Pages/eventupdate/eventupdate.module').then( m => m.EventUpdatePageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
