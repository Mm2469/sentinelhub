async function loadEvents() {
const eventsContainer = document.getElementById("events");

try {
const response = await fetch("http://localhost:5000/events");
const data = await response.json();

if (data.events.length === 0) {
eventsContainer.innerHTML = "<p>No security events detected.</p>";
return;
}

eventsContainer.innerHTML = data.events
.map(event => `
<div>
<strong>${event.event_type}</strong>
<p>Severity: ${event.severity}</p>
<p>Source: ${event.source}</p>
<p>Time: ${event.timestamp}</p>
</div>
`)
.join("");
} catch (error) {
eventsContainer.innerHTML =
"<p>Unable to connect to the SentinelHub backend.</p>";
console.error(error);
}
}

loadEvents();
