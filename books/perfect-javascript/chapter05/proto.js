function Animal() {
  this.call = function(){ print('??'); };
}
var animal = new Animal();
animal.call(); // => ??

function Dog() {
}
print(Dog.prototype.constructor);
// =>
// function Dog() {
// }

Dog.prototype = new Animal();
print(Dog.prototype.constructor);
// =>
// function Animal() {
//     this.call = function () {print("??");};
// }

Dog.prototype.call = function(){ print('わんわん'); };
var dog = new Dog();
dog.call();// => わんわん
