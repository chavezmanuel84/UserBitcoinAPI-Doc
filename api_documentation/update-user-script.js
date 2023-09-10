document.getElementById("update-user-button").addEventListener("click", function (e) {
    e.preventDefault();
    const new_password = document.getElementById("update-user-password").value;
    const token = document.getElementById("update-user-token").value;
    const apiUrl = "https://8j5baasof2.execute-api.us-west-2.amazonaws.com/production/users/update";
 

    // Check if new_password length is greater than 7 characters
    if (new_password.length > 7) {
        document.getElementById("update-user-response").textContent = "Error: Passowrd must be máximum 7 characters long.";
        return; // Exit the function to prevent the fetch request
    }

    fetch(apiUrl, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
            "Token": token,
        },
        body: JSON.stringify({ "new_password": new_password})
    })
    .then((response) => response.text())
    .then((data) => {
        document.getElementById("update-user-response").textContent = data;
    })
    .catch((error) => {
        console.error("Error:", error);
    });
});