var http = require('http');
var express = require('express');
var app = express();


//var crypto = require('crypto-js');
var AES = require("crypto-js/aes");
var SHA256 = require("crypto-js/sha256");

var message = "Booyakasha!"


var dotenv = require('dotenv');
dotenv.load();
//var _ = require('lodash');
var express = require('express');
var bodyParser = require('body-parser');
var session = require('cookie-session');
//var app = express();
var request = require('request');
var async = require('async');
var moment = require('moment');
// var sendgrid = require("sendgrid")(process.env.SENDGRID_USERNAME, process.env.SENDGRID_PASSWORD);
//var token_broker = "https://oauth.oit.duke.edu/oauth/token.php";
//var duke_card_host = "https://dukecard-proxy.oit.duke.edu";
var auth_url = process.env.ROOT_URL + "/home/auth";
//var db = require('monk')(process.env.MONGOHQ_URL || "mongodb://localhost/foodpoints");
var db = require('monk')('104.131.255.24');
//var users = db.get("users");
//var balances = db.get("balances");
//var budgets = db.get("budgets");
//var passport = require('passport');
//var favicon = require('serve-favicon'); //serve favicon for site
//var munge = require('munge'); //obfuscate email



var numVisits = 0;

app.use(bodyParser.json());
//app.use('/deposits', bodyParser.urlencoded({extended : false}));

app.listen(process.env.PORT || 3000, function() {
    console.log("Node app is running");
});

app.get('/', function(req, res){
    numVisits ++;
    res.set('text/plain');
    //res.send("Hi Brandon!!! You're visiting for the " + numVisits + " time!");
    res.send("Result of hashing " + message + " is " + SHA256(message));
    res.end();
    console.log("GET Request received");

    console.log("Result of hashing " + message + " is " + SHA256(message));
});

app.post('/deposits', function(req, res) {
	var body = req.body;
//	console.log("Received deposit string " + JSON.stringify(req.body));
//	res.send();
	res.set('text/plain').send('Your encrypted message is ' + SHA256(body)).end();
});


