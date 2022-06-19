// DATA CLASSES

// Every Data Class in Kotlin needs to fulfill the following requirements -

// The primary constructor must have at least one parameter
// All the parameters declared in the primary constructor need to be marked as val or var.
// Data classes cannot be abstract, open, sealed or inner.

data class User(val id: Long, val name: String)


func fun main(args: Array<String>) {
    val user = User(1, "Denis")

    // Getting a property
    val name = user.name

    // Setting a Property

    // You cannot set read-only properties
    user.id = 2	// Error: Val cannot be assigned

    val user1 = User(1, "Denis")
    val user2 = User(1, "Denis")

    println(customer1.equals(customer2))  // Prints true
    // You can also use Kotlin’s Structural equality operator == to check for equality. The == operator internally calls the equals() method -
    println(customer1 == customer) // Prints true

    // Dataclasses have a toString Method
    println("User Details : $user") // Prints User(1,"Denis")

    // Using the copy() Method
    // Copies the customer object into a separate Object 
    // and updates the name. 
    // The advanteg is, that the existing customer object remains unchanged.
  
    val updatedUser = user.copy(name = "Denis Panjuta")
    println("User : $user")
    println("Updated User : $updatedUser")

    // Deconstructing Data Classus
    val user = User(3, "Frank")

    println(user.component1()) // Prints 3
    println(user.component2()) // Prints "Frank"

    val (id, name) = customer
    println("id = $id, name = $name") // Prints "id = 3, name = Frank"
}