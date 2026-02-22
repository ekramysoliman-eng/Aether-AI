// Aether AI - Core Interaction Logic
const chatBox = document.getElementById('chat-box');
const userInput = document.querySelector('input');
const syncBtn = document.querySelector('button');

function addMessage(sender, text, colorClass) {
    const msg = document.createElement('div');
    msg.className = colorClass;
    msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
    chatBox.appendChild(msg);
    // Auto-scroll to the latest thought
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function handleSync() {
    const text = userInput.value.trim();
    if (!text) return;

    // 1. Display User Thought
    addMessage('Kimo', text, 'text-slate-300');
    userInput.value = '';

    // 2. Simulate Aether's Quantum Processing
    const responseDelay = 600; // 0.6 seconds for "Quantum Speed" effect
    
    setTimeout(() => {
        // Here, in the full version, we call the Gemini Live API
        const aetherResponse = `Processing "${text}"... Logic synchronized with Aura-AbuDhabi and AEGIS-WATER protocols. State: Optimized.`;
        addMessage('Aether', aetherResponse, 'text-sky-400');
    }, responseDelay);
}

// Trigger on click
syncBtn.addEventListener('click', handleSync);

// Trigger on "Enter" key
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleSync();
});
