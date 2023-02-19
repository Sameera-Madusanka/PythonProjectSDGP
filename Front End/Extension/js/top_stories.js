function myFunction() {
    var urls = ["http://localhost/PythonProjectSDGP/Front%20End/Extension/News_Pages/Air%20India%20seals%20record%20order%20for%20almost%20500%20Airbus%20Boeing%20jets.html",
        "http://localhost/PythonProjectSDGP/Front%20End/Extension/query.html",
        "http://localhost/PythonProjectSDGP/Front%20End/Extension/popup.html",
    ];

    var randomIndex = Math.floor(Math.random() * urls.length);
    var randomUrl = urls[randomIndex];
    window.location = randomUrl;
}
