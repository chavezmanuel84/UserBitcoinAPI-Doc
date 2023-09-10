document.getElementById("get-user-button").addEventListener("click", function (e) {
    e.preventDefault();
    const username = document.getElementById("get-user-username").value;
    const format = document.getElementById("get-format-type").value;
    const token = document.getElementById("get-user-token").value;
    const apiUrl = "https://8j5baasof2.execute-api.us-west-2.amazonaws.com/production/users/"+username+"."+format;
 


    fetch(apiUrl, {
        method: "GET",
        headers: {
            "Token": token,
        }
    })
    .then((response) => response.text())
    .then((data) => {
        document.getElementById("get-user-response").textContent = data;
    })
    .catch((error) => {
        console.error("Error:", error);
    });
});