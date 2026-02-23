async function syncWithBrain() {
    const userInput = document.getElementById('user-input').value;
    const responseBox = document.getElementById('aether-response');
    
    // REPLACE THIS URL with your actual Direct URL from Hugging Face
    const brainUrl = "https://ekramysoliman-aether-ai-brain.hf.space/chat";

    if (!userInput) return alert("Please type a message.");

    responseBox.innerText = "Processing...";

    try {
        const response = await fetch(brainUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userInput })
        });

        const data = await response.json();
        responseBox.innerText = data.response || "No response received.";
    } catch (error) {
        responseBox.innerText = "Connection Failed. Check if Space is Public.";
    }
}
