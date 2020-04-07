import 'package:firebase_auth/firebase_auth.dart';
import 'package:google_sign_in/google_sign_in.dart';

class Auths{
  FirebaseAuth _auth = FirebaseAuth.instance;
  GoogleSignIn _gAuth = GoogleSignIn();
// SignUp user Function with FirebaseAuth
  Future signUp(String email, String password) async{
    try{
      AuthResult result = await _auth.createUserWithEmailAndPassword(email: email, password: password);
      FirebaseUser user = result.user;
      return user != null;
    }
    catch(e){
      print(e.toString());
      return null;
    } 
  }
//  SignIn User Function with FirebaseAuth

  Future signIn(String email, String password) async{
    try{
      AuthResult result = await _auth.signInWithEmailAndPassword(email: email, password: password);
      FirebaseUser user = result.user;
      return user != null;
    }
    catch(e){
      print(e.toString());
      return null;
    }
  }

  // Google SignIn 

  Future googleSignIn() async{
    try{
      GoogleSignInAccount google = await _gAuth.signIn();
      GoogleSignInAuthentication authenticate = await google.authentication;
      AuthCredential creden = GoogleAuthProvider
        .getCredential(
          idToken: authenticate.idToken, 
        accessToken: authenticate.accessToken);
      return creden != null;
    }
    catch(e){
      print(e.toString());
      return null;
    }
  }
  // Everything Sign-Out
  Future signOut() async{
    try{
      _auth.signOut();
    }
    catch(e){
      print(e.toString());
      return null;
    }
  }

  
  Future googleSignOut() async{
    try{
      _gAuth.signOut();
    }
    catch(e){
      print(e.toString());
      return null;
    }
  }
}