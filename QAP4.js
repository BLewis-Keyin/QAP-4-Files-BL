const customer = {
    name: 'John Doe',
    type: 'Motel',
    birthDate: new Date('1990-09-12'),
    gender: 'Male',
    roomPreference: ['2 Beds', ' Pool View ', ' TV '],
    paymentMethod: 'Credit Card',
    mailingAddress: {
        unit: '1',
        street: 'Example Street',
        city: "St'Johns",
        province: 'NL',
        postalcode: 'A0A0A0',
    },
    phNum: "709-111-1111",
    checkInOut: {
        checkinDatetime: new Date('2023-03-23T19:00:00'),
        checkoutDatetime: new Date('2023-03-26T15:30:00'),
    },
    getAge: function() {
        const today = new Date();
        var age = today.getFullYear() - this.birthDate.getFullYear();
        return age
    },
    getStay: function() {
        var stayMS = this.checkInOut.checkoutDatetime - this.checkInOut.checkinDatetime;
        return stayMS
    },
    getStayDays: function() {
        var stayDays = this.getStay() / 86400000
        return Math.round(stayDays)
    },

}
console.log(customer, customer.getStayDays(), customer.getAge())

var templatestring =
    `${customer.name} has purchased a room in a ${customer.type}. ${customer.name} was born on ${customer.birthDate} and is ${customer.getAge()} years old. ${customer.name} is ${customer.gender}. Room preferences are "${customer.roomPreference}", payment method is ${customer.paymentMethod}. ${customer.name}'s mailing adress is ${customer.mailingAddress.unit} ${customer.mailingAddress.street} ${customer.mailingAddress.city}, ${customer.mailingAddress.province} ${customer.mailingAddress.postalcode}. ${customer.name}'s phone number is ${customer.phNum}. ${customer.name} checked in at ${customer.checkInOut.checkinDatetime} and checked out at ${customer.checkInOut.checkoutDatetime}, for a stay duration of ${customer.getStayDays()} days.
    `

console.log(templatestring)