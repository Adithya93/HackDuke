var crypto = require('crypto');
var ciphers = crypto.getCiphers();
console.log(ciphers);
var rsaKeygen = require('rsa-keygen');
var keys = rsaKeygen.generate();
console.log(keys.public_key.toString('utf8'));
console.log(keys.private_key.toString('utf8'));
crypto.createCipheriv('RSA', keys.public_key, '1');

var result = crypto.publicEncrypt({
  key: keys.public_key
}, new Buffer('Hello world!'));
// <Crypted Buffer>
console.log(result.toString('utf8'));
var plaintext = crypto.privateDecrypt({
  key: keys.private_key
}, result);
// Hello world!
console.log(plaintext.toString('utf8'));
