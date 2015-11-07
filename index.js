var http = require('http');
var express = require('express');
var app = express();



var dotenv = require('dotenv');
dotenv.load();
var _ = require('lodash');
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
var db = require('monk')(process.env.MONGOHQ_URL || "mongodb://localhost/foodpoints");
//var users = db.get("users");
//var balances = db.get("balances");
//var budgets = db.get("budgets");
//var passport = require('passport');
//var favicon = require('serve-favicon'); //serve favicon for site
//var munge = require('munge'); //obfuscate email



var numVisits = 0;

app.listen(process.env.PORT || 3000, function() {
    console.log("Node app is running");
});

app.get('/', function(req, res){
    numVisits ++;
    res.set('text/plain');
    res.send("Hi Brandon!!! You're visiting for the " + numVisits + " time!");
    res.end();
    console.log("GET Request received");
});