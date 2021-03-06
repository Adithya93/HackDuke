var NodeRSA = require("node-rsa");

var key = new NodeRSA(
          '-----BEGIN RSA PRIVATE KEY-----\n'+
          'MIIBOQIBAAJAVY6quuzCwyOWzymJ7C4zXjeV/232wt2ZgJZ1kHzjI73wnhQ3WQcL\n'+
          'DFCSoi2lPUW8/zspk0qWvPdtp6Jg5Lu7hwIDAQABAkBEws9mQahZ6r1mq2zEm3D/\n'+
          'VM9BpV//xtd6p/G+eRCYBT2qshGx42ucdgZCYJptFoW+HEx/jtzWe74yK6jGIkWJ\n'+
          'AiEAoNAMsPqwWwTyjDZCo9iKvfIQvd3MWnmtFmjiHoPtjx0CIQCIMypAEEkZuQUi\n'+
          'pMoreJrOlLJWdc0bfhzNAJjxsTv/8wIgQG0ZqI3GubBxu9rBOAM5EoA4VNjXVigJ\n'+
          'QEEk1jTkp8ECIQCHhsoq90mWM/p9L5cQzLDWkTYoPI49Ji+Iemi2T5MRqwIgQl07\n'+
          'Es+KCn25OKXR/FJ5fu6A6A+MptABL3r8SEjlpLc=\n'+
          '-----END RSA PRIVATE KEY-----');

var test = new NodeRSA({
      b: 512
    });

    test.generateKeyPair();

    var privKey = test.getPrivatePEM();
    var pubKey = test.getPublicPEM();
    
    console.log('Successfully generated keys');


    


var text = 'Hello RSA!';
//var encrypted = key.encrypt(text, 'base64');
//console.log('encrypted: ', encrypted); 

    var newPubKey = new NodeRSA(pubKey);
//    var otherEncrypted = newPubKey.encrypt(text, 'base64');
	var otherEncrypted = newPubKey.encrypt(text, 'base64');


/***
var otherKey = new NodeRSA(
          '-----BEGIN RSA PRIVATE KEY-----\n'+
          'MIIBOQIBAAJAVY6quuzCwyOWzymJ7C4zXjeV/232wt2ZgJZ1kHzjI73wnhQ3WQcL\n'+
          'DFCSoi2lPUW8/zspk0qWvPdtp6Jg5Lu7hwIDAQABAkBEws9mQahZ6r1mq2zEm3D/\n'+
          'VM9BpV//xtd6p/G+eRCYBT2qshGx42ucdgZCYJptFoW+HEx/jtzWe74yK6jGIkWJ\n'+
          'AiEAoNAMsPqwWwTyjDZCo9iKvfIQvd3MWnmtFmjiHoPtjx0CIQCIMypAEEkZuQUi\n'+
          'pMoreJrOlLJWdc0bfhzNAJjxsTv/8wIgQG0ZqI3GubBxu9rBOAM5EoA4VNjXVigJ\n'+
          'QEEk1jTkp8ECIQCHhsoq90mWM/p9L5cQzLDWkTYoPI49Ji+Iemi2T5MRqwIgQl07\n'+
          'Es+KCn25OKXR/FJ5fu6A6A+MptABL3r8SEjlpLc=\n'+
          '-----END RSA PRIVATE KEY-----');
          ***/
//var decrypted = key.decrypt(encrypted, 'utf8');
//var otherDecrypted = otherKey.decrypt(encrypted, 'utf8');
var newPrivKey = new NodeRSA(privKey);
//var otherDecrypted = newPrivKey.decrypt(otherEncrypted, 'base64');
var otherDecrypted = newPrivKey.decrypt(otherEncrypted, 'utf8');

//console.log('decrypted: ', decrypted);
console.log('Other decrypted:', otherDecrypted);

