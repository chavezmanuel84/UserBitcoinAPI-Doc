document.getElementById("bitcoin-transfer-button").addEventListener("click", function (e) {
    e.preventDefault();
    const origin_user_token = document.getElementById("origin-user-token").value;
    const dest_user = document.getElementById("dest-user").value;
    const amount = parseFloat(document.getElementById("transfer-amount").value); // Convert to a number
    const apiUrl = "https://8j5baasof2.execute-api.us-west-2.amazonaws.com/production/users/transfer";
 
    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Token": origin_user_token,
        },
        body: JSON.stringify( {"To": dest_user, "Amount": amount} )
    })
    .then((response) => response.text())
    .then((data) => {
        document.getElementById("bitcoin-transfer-response").textContent = data;
    })
    .catch((error) => {
        console.error("Error:", error);
    });
});