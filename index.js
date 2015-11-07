var http = require('http');
var express = require('express');
var app = express();


var numVisits = 0;

app.get('/', function(req, res){
    numVisits ++;
    res.set('text/plain');
    res.send("Hi Brandon!!! You're visiting for the " + numVisits + " time!");
    res.end();
    console.log("GET Request received");
}).listen(3000);