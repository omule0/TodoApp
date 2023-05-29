const today = new Date();
const calendarCells = document.querySelectorAll('.calendar tbody td');

calendarCells.forEach(cell => {
  const cellDate = new Date(cell.getAttribute('data-date'));
  if (cellDate.getFullYear() === today.getFullYear() &&
      cellDate.getMonth() === today.getMonth() &&
      cellDate.getDate() === today.getDate()) {
    cell.classList.add('today');
  }
});

const addEventForm = document.querySelector('.add-event form');
const eventNameInput = document.querySelector('#event-name');
const eventDateInput = document.querySelector('#event-date');

addEventForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const eventName = eventNameInput.value;
  const eventDate = new Date(eventDateInput.value);
  
  calendarCells.forEach(cell => {
    const cellDate = new Date(cell.getAttribute('data-date'));
    if (cellDate.getFullYear() === eventDate.getFullYear() &&
        cellDate.getMonth() === eventDate.getMonth() &&
        cellDate.getDate() === eventDate.getDate()) {
      cell.classList.add('event');
      cell.innerHTML += '<br>' + eventName;
    }
  });
  
  eventNameInput.value = '';
  eventDateInput.value = '';
});

// Add the addEvent function
function addEvent() {
  // Get the form input values
  var title = document.getElementById("event-title").value;
  var date = document.getElementById("event-date").value;
  var time = document.getElementById("event-time").value;
  var description = document.getElementById("event-description").value;

  // Create a new event element
  var event = document.createElement("div");
  event.classList.add("event");
  event.innerHTML = `<h3>${title}</h3><p>${time}</p><p>${description}</p>`;

  // Find the corresponding date cell in the calendar
  var cell = document.querySelector(`td[data-date="${date}"]`);

  // Add the event to the calendar cell
  cell.appendChild(event);

  // Create a new event element for the events section
  var eventsSection = document.getElementById("events");
  var eventSectionItem = document.createElement("div");
  eventSectionItem.classList.add("event-section-item");
  eventSectionItem.innerHTML = `<h3>${title}</h3><p>${date} at ${time}</p><p>${description}</p>`;

  // Add the event to the events section
  eventsSection.appendChild(eventSectionItem);
}

