import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './guard/auth.guard';
import { HomePage } from './home/home.page';
import { NotFoundPage } from './Pages/not-found/not-found.page';
import { SignupPage } from './Pages/signup/signup.page';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {
    path: 'home',
    canActivate: [AuthGuard],
    component: HomePage,
    loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)
  },
  {
    path: 'login',
    loadChildren: () => import('./Pages/login/login.module').then( m => m.LoginPageModule)
  },
  {
    path: 'signup',
    component: SignupPage,
    loadChildren: () => import('./Pages/signup/signup.module').then( m => m.SignupPageModule)
  },
  {
    path: '404',
    component: NotFoundPage
  },
  {
    path: '**',
    redirectTo: '404'
  },
  {
    path: 'start',
    loadChildren: () => import('./Pages/start/start.module').then( m => m.StartPageModule)
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
