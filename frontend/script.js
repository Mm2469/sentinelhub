async function loadEvents() {
try {
const response = await fetch("http://localhost:5000/events");
const data = await response.json();

console.log("Security events:", data.events);
} catch (error) {
console.error("Unable to load security events:", error);
}
}

loadEvents();
