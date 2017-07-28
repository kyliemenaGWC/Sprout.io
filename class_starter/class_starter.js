class Person {
	constructor(first_name, last_name, address) {
		this.first_name = first_name;
		this.last_name = last_name;
		this.address = address;
	}

	getFulName(){
		return this.first_name + " " + this.last_name
	}
	getAddress(){
		return this.address
	}
}

var TomCruise = new Person("Tom", "Cruise", "123 Seasame Street")
document.getElementById("myName").innerText = TomCruise.getFulName();
document.getElementById("myAddress").innerText = TomCruise.getAddress();