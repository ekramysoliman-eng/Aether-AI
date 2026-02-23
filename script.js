// Function to communicate with the Aether AI Brain on Hugging Face
async function syncWithBrain() {
    const userInput = document.getElementById('user-input').value;
    const responseBox = document.getElementById('aether-response');
    
    // Replace the URL below with your Direct URL from Hugging Face + /chat
    const brainUrl = "https://ekramysoliman-aether-ai-brain.hf.space/chat";

    if (!userInput) {
        alert("Please enter a message for Aether.");
        return;
    }

    responseBox.innerText = "Processing with Sherlock-House logic...";

    try {
        const response = await fetch(brainUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput })
        });

        const data = await response.json();
        
        if (data.response) {
            responseBox.innerText = data.response;
        } else {
            responseBox.innerText = "Error: Brain is offline. Check Hugging Face status.";
        }

    } catch (error) {
        console.error("Connection Error:", error);
        responseBox.innerText = "Failed to reach the brain. Ensure the Space is Public.";
    }
}
