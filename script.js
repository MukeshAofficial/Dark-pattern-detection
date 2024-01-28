document.addEventListener('DOMContentLoaded', function () {
    var analyzeButton = document.getElementById('analyzeButton');
    analyzeButton.addEventListener('click', showResults);
});

function showResults() {
    document.getElementById("analysis-section").style.display = "none";
    document.getElementById("result-section").style.display = "block";
}
