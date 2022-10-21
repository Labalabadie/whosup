import { Component, OnInit } from '@angular/core';
import { AlertController, NavController } from '@ionic/angular';
import { Storage } from '@capacitor/storage'
import { Signup } from 'src/app/Models/signup.model';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.page.html',
  styleUrls: ['./signup.page.scss'],
})
export class SignupPage implements OnInit {

  signupUser: Signup = new Signup();

  constructor(public alertController: AlertController,
    public navCtrl: NavController,) { }

  ngOnInit() {
  }

  async Name(){
	  if(this.signupUser.name == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
  async Mail(){
	  if(this.signupUser.mail == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
  async Phone(){
	  if(this.signupUser.phone == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
  async Password(){
	  if(this.signupUser.password == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
  async checkPassword(){
	  if(this.signupUser.checkpassword == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
    async save(signupForm: NgForm){

      console.log(signupForm);
        if(signupForm.invalid){
          const alert = await this.alertController.create({
            header: 'Datos incompletos',
            message: 'Tienes que llenar todos los datos',
            buttons: ['Aceptar']
          });
    
          await alert.present();
          return;
        }
    
        const user = {
        name: signupForm.value.name,
        mail: signupForm.value.mail,
        phone: signupForm.value.movil,
        password: signupForm.value.password,
        checkpassword: signupForm.value.checkpassword
        };
    
      const key = 'user';
        Storage.set({ key, value: JSON.stringify(user) });
    
      const key2 = 'ingresado';
      const value = 'true';
      Storage.set({ key: key2, value });
        this.navCtrl.navigateRoot('home');
      }
    }
