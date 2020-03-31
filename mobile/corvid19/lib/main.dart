import 'package:corvid/authUI/signin.dart';
import 'package:flutter/material.dart';

import 'authUI/signin.dart';
import 'authUI/signup.dart';
import 'authUI/home.dart';
import 'package:flutter/services.dart';

void main() {
    SystemChrome.setEnabledSystemUIOverlays([]);
    runApp(MyApp());
} 

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations([
      DeviceOrientation.portraitUp,
      DeviceOrientation.portraitDown,
    ]);

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      routes: {
        '/': (BuildContext context) => HomePage(),
        '/signin': (BuildContext context) => SignIn(),
        '/signup': (BuildContext context) => SignUp(),
      },
    );
  }
}

