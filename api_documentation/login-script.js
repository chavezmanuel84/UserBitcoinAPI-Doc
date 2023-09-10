document.getElementById("login-button").addEventListener("click", function (e) {
    e.preventDefault();
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;
    const apiUrl = "https://8j5baasof2.execute-api.us-west-2.amazonaws.com/production/users/login";

    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ "Username": username, "Password": password }),
    })
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("login-response").textContent = JSON.stringify(data, null, 2);
    })
    .catch((error) => {
        console.error("Error:", error);
    });
});
