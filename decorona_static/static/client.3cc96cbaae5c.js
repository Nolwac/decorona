// import React from 'react.min';
// import ReactDOM from 'react-dom.min';
// the above statements only work with the webpackaging plugins for the main time and does not work with browsers for now.
/**
 * @jsx React.DOM
 */
// class Layout extends React.Component{
// 	render(){
// 		return (
// 			<h1> It works like mad</h1>
// 			);
// 	}
// }
// app=document.getElementById('testapp');
// ReactDOM.render(<Layout/>, app);
var message = require('./testpack')
alert(message);