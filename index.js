"use strict";
var http = require('http');
var express = require('express');
var app = express();
var fs = require('fs');
var path = require('path');
//var privKey = fs.createWriteStream();
//var pubKey = fs.createWriteStream();


//var crypto = require('crypto-js');
var AES = require("crypto-js/aes");
var SHA256 = require("crypto-js/sha256");
//var NodeRSA = require('node-rsa');
var crypto = require('crypto');

//var sign = crypto.createSign('RSA-SHA256');

var NodeRSA = require('node-rsa');

//var key = new NodeRSA({b: 512});

//var keyPair = key.generateKeyPair(512);
//console.log(keyPair);
//var privKey = key.getPrivatePEM();
//var pubKey = key.getPublicPEM();
//console.log('Private key is ' + privKey + ' and public key is ' + pubKey);
//console.log('Private key is');
//console.log(privKey);
//console.log('Public key is');
//console.log(pubKey);


//var pubData = pubKey;
//var privData = privKey;

//key.importKey(pubData, 'pkcs8');
//var publicDer = key.exportKey('pkcs8-public-der');

//var publicDer = new NodeRSA(pubKey).exportKey('pkcs8-public-der');
//var publicDer = pubKey.exportKey('pkcs8-public-der');
//var privateDer = new NodeRSA(privKey).exportKey('pkcs1-der');
//console.log("Public Der: " + publicDer);
//console.log("Private Der: " + privateDer);


var message = "Booyakasha!";


var dotenv = require('dotenv');
dotenv.load();
//var _ = require('lodash');
//var express = require('express');
var bodyParser = require('body-parser');
var session = require('cookie-session');
var request = require('request');
var async = require('async');
var moment = require('moment');
// var sendgrid = require("sendgrid")(process.env.SENDGRID_USERNAME, process.env.SENDGRID_PASSWORD);
//var token_broker = "https://oauth.oit.duke.edu/oauth/token.php";
//var duke_card_host = "https://dukecard-proxy.oit.duke.edu";
//var auth_url = process.env.ROOT_URL + "/home/auth";
//var db = require('monk')(process.env.MONGOHQ_URL || "mongodb://localhost/foodpoints");
var db = require('monk')('104.131.255.24/HackDuke');
var users = db.get('users');
var keys = db.get('keys');

//var users = db.get("users");
//var balances = db.get("balances");
//var budgets = db.get("budgets");
//var passport = require('passport');
//var favicon = require('serve-favicon'); //serve favicon for site
//var munge = require('munge'); //obfuscate email

var twilio = require('twilio')('ACd566c2614fae1998ae89a275952b4ccc', 'dfeacbb442ea9601ae93a0c3ff505d54');

var numVisits = 0;

app.use('/users/new', bodyParser.json());
app.use('/deposits', bodyParser.json());
app.use('/twilio', bodyParser.urlencoded({extended:false}));
app.listen(process.env.PORT || 3000, function() {
  console.log("Node app is running");
});

app.get('/', function(req, res) {
  numVisits++;
  res.set('text/plain');
  //res.send("Hi Brandon!!! You're visiting for the " + numVisits + " time!");
  res.send("Result of hashing " + message + " is " + SHA256(message));
  res.end();
  console.log("GET Request received");

  console.log("Result of hashing " + message + " is " + SHA256(message));

  console.log("All users: ");
  console.log();
  users.find({}, function(err, res) {
    console.log(res);
  });
});

// Transaction requests sent by SMS
app.post('/deposits', function(req, res) {
  var body = req.body;
  //	console.log("Received deposit string " + JSON.stringify(req.body));
  //	res.send();
  //res.set('text/plain').send('Your encrypted message is ' + SHA256(body)).end();

});


// Registration of new user

app.post('/users/new', function(req, res){

    var start = "-----BEGIN PUBLIC KEY-----\n";
    var end = "\n-----END PUBLIC KEY-----";
    var newUser = req.body;
    var keyId;
    var key;
    console.log("Received JSON object for new user:");
    console.log(newUser);
    newUser['balance'] = 0;
    users.insert(newUser, function(err, reply) {
        console.log("Added new user to database");
        keyId = reply['_id'];
        console.log("Key id is " + keyId);

        key = new NodeRSA({b: 512});
//    key.generateKeyPair((Math.floor((Math.random() * 10)* + 1))*8);
    key.generateKeyPair();
    var privKey = key.getPrivatePEM();
    var pubKey = key.getPublicPEM();
    //var info = "Your public key is:\n" + pubKey;
    var info = {'Key' : pubKey.substring(pubKey.indexOf(start) + start.length, pubKey.indexOf(end)), 'ID' : keyId};
    console.log('Sending JSON object with ' + Object.keys(info).length + ' keys');
    console.log(info);
    res.set('app/json').send(info);
    res.end();
    var keyInfo = {'id' : keyId, 'Private Key' : privKey};
    keys.insert(keyInfo, function(err, rep) {
        console.log('Saved new private key into database');
        console.log(rep);
    });
    /***
    key = new NodeRSA({b: 512});
//    key.generateKeyPair((Math.floor((Math.random() * 10)* + 1))*8);
    key.generateKeyPair();
    var privKey = key.getPrivatePEM();
    var pubKey = key.getPublicPEM();
    //var info = "Your public key is:\n" + pubKey;
    var info = {'Key' : pubKey, 'ID' : keyId};
    console.log('Sending JSON object with ' + Object.keys(info).length + ' keys');
    console.log(info);
    res.set('app/json').send(info);
    res.end();
    var keyInfo = {'id' : keyId, 'Private Key' : privKey};
    keys.insert(keyInfo, function(err, rep) {
        console.log('Saved new private key into database');
        console.log(rep);
        ***/
    });
    });
app.post('/users/new', function(req, res) {

  var newUser = req.body;
  var keyId;
  var key;
  console.log("Received JSON object for new user:");
  console.log(newUser);
  newUser['balance'] = 0;
  users.insert(newUser, function(err, reply) {
    console.log("Added new user to database");
    keyId = reply['_id'];
    console.log("Key id is " + keyId);
  });
  key = new NodeRSA({
    b: 512
  });
  //    key.generateKeyPair((Math.floor((Math.random() * 10)* + 1))*8);
  key.generateKeyPair();
  var privKey = key.getPrivatePEM();
  var pubKey = key.getPublicPEM();
  //var info = "Your public key is:\n" + pubKey;
  var info = {
    'Key': pubKey,
    'ID': keyId
  };
  res.set('app/json').send(info);
  res.end();
  var keyInfo = {
    'id': keyId,
    'Private Key': privKey
  };
  keys.insert(keyInfo, function(err, rep) {
    console.log('Saved new private key into database');
    console.log(rep);
  });
});

app.post('/twilio', function(req, res) {
  if (twilio.validateExpressRequest(req, 'dfeacbb442ea9601ae93a0c3ff505d54')) {
    var resp = new twilio.TwimlResponse();
    console.log("twilio req is", req);
    resp.say('express sez - hello twilio!');

    res.type('text/xml');
    res.send(resp.toString());
  } else {
    res.send('you are not twilio.  Buzz off.');
  }
});
