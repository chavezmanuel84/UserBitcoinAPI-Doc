document.getElementById("create-user-button").addEventListener("click", function (e) {
    e.preventDefault();
    const username = document.getElementById("create-user-username").value;
    const password = document.getElementById("create-user-password").value;
    const apiUrl = "https://8j5baasof2.execute-api.us-west-2.amazonaws.com/production/users/new";

    // Check if new_password length is greater than 7 characters
    if (password.length > 7) {
        document.getElementById("create-user-response").textContent = "Error: Passowrd must be máximum 7 characters long.";
        return; // Exit the function to prevent the fetch request
    }

    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ "Username": username, "Password": password }),
    })
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("create-user-response").textContent = JSON.stringify(data, null, 2);
    })
    .catch((error) => {
        console.error("Error:", error);
    });
});
