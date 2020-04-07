import 'package:flutter/material.dart';
import 'package:corvid/authUI/validators/validator.dart';

class SignIn extends StatefulWidget{
  @override 
  _SignIn createState() => _SignIn();

}

class _SignIn extends State<SignIn>{

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  final TextEditingController _email = new TextEditingController();
  final TextEditingController _password = new TextEditingController();

  @override 
  Widget build(BuildContext context) {

    final emailField = TextFormField(
      style: TextStyle(fontSize: 20.0),
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      controller: _email,
      validator: Validator.validateEmail,
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
      style: TextStyle(fontSize: 20.0),
      autofocus: false,
      obscureText: true,
      controller: _password,
      validator: Validator.validatePassword,
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

    final loginButton = Material(
      elevation: 5.0,
      borderRadius: BorderRadius.circular(30.0),
      color: Color(0xFF66BB6A),
      child: MaterialButton(
        minWidth: MediaQuery.of(context).size.width,
        padding: EdgeInsets.symmetric(horizontal:15.0, vertical:20.0),
        onPressed: () {},
        child: Text('Sign in',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 20.0,
                color: Colors.white,
                fontWeight: FontWeight.bold
              ),),),
    );


      final signupButton = FlatButton(
        child: Text('Sign Up'),
        onPressed:() => Navigator.pushNamed(context, '/signup')
    );



    return Scaffold(
      body: Center(
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
                SizedBox(height: 100.0,
                child: Image.asset('assets/image/logo.jpg',
                fit: BoxFit.contain,),
                ),

                SizedBox(height: 48.0),
                emailField,
                SizedBox(height: 24.0),
                passwordField,
                SizedBox(
                  height: 36.0,
                ),

                loginButton,
                SizedBox(height: 16.0),
                signupButton,
              ],
            ),),

        )
      ))
    );
  }
}