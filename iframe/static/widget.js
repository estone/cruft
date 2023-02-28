var loadForm = document.getElementById("ourWidget");

var theFrame = document.createElement("iframe");

// This is the form html URL
theFrame.src = "http://127.0.0.1:5050/";

theFrame.width = "600";
theFrame.height = "650";
theFrame.frameBorder ="0";
theFrame.scrolling = "0";
theFrame.style.border= "none";
theFrame.style.background = "white";

var theButton = document.createElement("button");
theButton.innerText = "Clicky click";
loadForm.appendChild(theButton);

// We only load the remote iframe form if user clicks on button 
theButton.addEventListener("click", function(){
		// Add Iframe to webpage
		loadForm.appendChild(theFrame);
		// Hide button
		this.style.display = "none";
		})
