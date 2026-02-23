/**
 * Human Ai - Core Connection Script
 * Mission: Linking GitHub Frontend with Hugging Face Brain
 * Strategy: Sherlock-House Logic Execution
 */

async function syncWithBrain() {
    // 1. Identify Elements
    const userInputField = document.getElementById('user-input');
    const responseBox = document.getElementById('aether-response');
    
    // 2. Debugging: Check if button is alive in the console
    console.log("System Check: Sync button triggered.");

    // 3. Define the Engine URL (Ensure this matches your Direct URL)
    const brainUrl = "https://ekramysoliman-eng-aether-ai.hf.space/chat";

    // 4. Validation: Logical Deduction
    if (!userInputField || !userInputField.value.trim()) {
        console.warn("Input Logic Error: Message is empty.");
        alert("Aether AI requires data to proceed. Please enter a message.");
        return;
    }

    const userMessage = userInputField.value;

    // 5. Visual Feedback: The Processing State
    responseBox.innerText = "Analyzing data with Sherlock-House logic... Please wait.";
    responseBox.style.color = "#00d4ff"; // Quantum Blue

    try {
        // 6. Execution: Sending the request to the Cloud Brain
        console.log("Action: Dispatching request to Hugging Face...");
        
        const response = await fetch(brainUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage })
        });

        // 7. Data Retrieval
        const data = await response.json();

        // 8. Result: Updating the interface with AI Intelligence
        if (data.response) {
            console.log("Success: Intelligence received.");
            responseBox.innerText = data.response;
            responseBox.style.color = "#ffffff";
        } else {
            console.error("Brain Error: No response field in data.");
            responseBox.innerText = "Error: The brain processed the request but returned no thoughts.";
        }

    } catch (error) {
        // 9. Diagnostic: Gregory House Method
        console.error("Connection Fatality:", error);
        responseBox.innerText = "Connection Failed. Diagnosis: Server is offline or URL is incorrect.";
        responseBox.style.color = "#ff4d4d"; // Warning Red
    }
}
