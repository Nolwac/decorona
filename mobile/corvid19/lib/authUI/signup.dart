import 'package:flutter/material.dart';
import 'package:corvid/authUI/validators/validator.dart';

class SignUp extends StatefulWidget{
  @override 
  _SignUp createState() => _SignUp();

}

class _SignUp extends State<SignUp>{

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  final TextEditingController _userName = new TextEditingController();
  final TextEditingController _email = new TextEditingController();
  final TextEditingController _password = new TextEditingController();



  @override 
  Widget build(BuildContext context) {

      final usernameField = TextFormField(
      autofocus: false,
      textCapitalization: TextCapitalization.words,
      controller: _userName,
      validator: Validator.validateName,
      style: TextStyle(fontSize: 20.0),
      decoration: InputDecoration(
        prefixIcon: Padding(
          padding: EdgeInsets.only(left: 5.0),
          child: Icon(
            Icons.person,
            color: Colors.grey,
          ), // icon is 48px widget.
        ),
        contentPadding: EdgeInsets.symmetric(horizontal: 15.0, vertical: 20.0),
        hintText: "Username",
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(32.0))
      ),
    );

    final emailField = TextFormField(
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      controller: _email,
      validator: Validator.validateEmail,
      style: TextStyle(fontSize: 20.0),
      decoration: InputDecoration(
        prefixIcon: Padding(
          padding: EdgeInsets.only(left: 5.0),
          child: Icon(
            Icons.email,
            color: Colors.grey,
          ), // icon is 48px widget.
        ),
        contentPadding: EdgeInsets.symmetric(horizontal: 15.0, vertical: 20.0),
        hintText: "Email",
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(32.0))
      ),
    );

    final passwordField = TextFormField(
      autofocus: false,
      obscureText: true,
      controller: _password,
      validator: Validator.validatePassword,
      style: TextStyle(fontSize: 20.0),
      decoration: InputDecoration(
        prefixIcon: Padding(
          padding: EdgeInsets.only(left: 5.0),
          child: Icon(
            Icons.lock,
            color: Colors.grey,
          ), // icon is 48px widget.
        ), 
        contentPadding: EdgeInsets.symmetric(horizontal:15.0, vertical:20.0),
        hintText: "Password",
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(32.0))
      ),
    );

    final conpasswordField = TextFormField(
      autofocus: false,
      obscureText: true,
      validator: Validator.validateConPassword,
      style: TextStyle(fontSize: 20.0),
      decoration: InputDecoration(
         prefixIcon: Padding(
          padding: EdgeInsets.only(left: 5.0),
          child: Icon(
            Icons.lock,
            color: Colors.grey,
          ), // icon is 48px widget.
        ),
        contentPadding: EdgeInsets.symmetric(horizontal:15.0, vertical:20.0),
        hintText: "Confirm Password",
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(32.0))
      ),
    );

    final signupButton = Material(
      elevation: 5.0,
      borderRadius: BorderRadius.circular(30.0),
      color: Color(0xFF66BB6A),
      child: MaterialButton(
        minWidth: MediaQuery.of(context).size.width,
        padding: EdgeInsets.symmetric(horizontal:15.0, vertical:20.0),
        onPressed: () {},
        child: Text('Sign up',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 20.0,
                color: Colors.white,
                fontWeight: FontWeight.bold
              ),),),
    );


      final loginButton = FlatButton(
        child: Text('Sign In'),
        onPressed:() => Navigator.pushNamed(context, '/signin')
    );


    
    return Scaffold(body: Center( 
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(8.0),
          child: Container( 
          height: MediaQuery
                    .of(context)
                    .size.height/1.2,
          child: Padding(
            padding: const EdgeInsets.all(36.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                SizedBox(height: 0.0,),
                usernameField,
                SizedBox(height: 10.0),
                emailField,
                SizedBox(height: 10.0),
                passwordField,
                SizedBox(height: 10.0),
                conpasswordField,
                SizedBox(height: 20.0),
                signupButton,
                SizedBox(height: 10.0),
                loginButton
              ],
            ),),

        )
      ))
    );
  }
}