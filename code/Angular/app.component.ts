import { Component} from '@angular/core';
import {User,User_Details} from "./user"
import {faPersonBooth,faHome,faBookmark,faBell,faSignInAlt,faPlus,faEye} from '@fortawesome/free-solid-svg-icons'
import {EmployeeService} from './employee.service'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Ashley Mutenha Cover Letter';
  public result =""
  public userDetails:boolean =false;
  public show:any =true
  public show1:any=false
  public login:any=true
  public warning:any =false
  public addPeople:any=false
  public model = new User("Ashley","nhetz")

  public user_details =new User_Details("")

  faHome =faHome
  faBookmark=faBookmark
  faBell =faBell
  faSignInAlt = faSignInAlt
  faPlus =faPlus
  faEye =faEye
  faPersonBooth =faPersonBooth
  public details:any
  
  constructor(private employee:EmployeeService) { }

  ngOnInit(): void {
  }

 

 signIn(){
 this.employee._login(this.model).subscribe()

}
delete(){
  this.employee._delete(this.user_details).subscribe()
}
  
toggle(){
this.show = !this.show
}
 
admin(){
  this.show1=true
  this.login=false
  this.userDetails=false
  this.addPeople=false}

home(){
  this.show1=false
  this.login=true
  this.userDetails=false
  this.addPeople=false
  }

showDetails(){
  this.login=false
  this.userDetails=true
  this.show1=false

  this.employee.getDetails().subscribe(data=>this.details=data)
}


addUsers(){
  this.addPeople =true
  this.login=false
  this.userDetails=false
  this.show1=false
}


}
