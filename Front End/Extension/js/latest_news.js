function myFunction() {
    var urls = ["file:///Users/ilsara/Desktop/SDGP/PythonProjectSDGP/Front%20End/Extension/News_Pages/Air%20India%20seals%20record%20order%20for%20almost%20500%20Airbus%20Boeing%20jets.html",
        "file:///Users/ilsara/Desktop/SDGP/PythonProjectSDGP/Front%20End/Extension/News_Pages/As%20U.S.%20budget%20fight%20looms,%20Republicans%20flip%20their%20fiscal%20script.html",
        "file:///Users/ilsara/Desktop/SDGP/PythonProjectSDGP/Front%20End/Extension/News_Pages/Ben%20Duckett%20will%20take%20every%20chance%20for%20England,%20while%20New%20Zealand%20overlook%20Trent%20Boult.html",
    "file:///Users/ilsara/Desktop/SDGP/PythonProjectSDGP/Front%20End/Extension/News_Pages/China%20Xi%20calls%20for%20early%20resolution%20of%20Iran%20nuclear%20issue.html",
"file:///Users/ilsara/Desktop/SDGP/PythonProjectSDGP/Front%20End/Extension/News_Pages/Court%20orders%20Trump%20administration%20to%20give%20immigrant%20teens%20abortion%20access.html",
"file:///Users/ilsara/Desktop/SDGP/PythonProjectSDGP/Front%20End/Extension/News_Pages/Earthquake%20fans%20anti-Syrian%20sentiment%20in%20Turkey%20amid%20desperate%20conditions.html"];

    var randomIndex = Math.floor(Math.random() * urls.length);
    var randomUrl = urls[randomIndex];
    window.location = randomUrl;
}
