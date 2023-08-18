document.addEventListener("DOMContentLoaded", function() {
    const addCalendarButtons = document.querySelectorAll('.add-calendar-button');
    const addAllToCalendarButton = document.querySelector('.add-all-calendar-button');
    
    addCalendarButtons.forEach(button => {
        button.addEventListener("click", function() {
            const rave_id = button.getAttribute("data-id");
            const xhr = new XMLHttpRequest();
            xhr.open("POST", "/add_to_calendar", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                    // Update the button text or perform other actions as needed
                    button.textContent = "Added to Calendar";
                }
            };
            xhr.send("rave_id=" + encodeURIComponent(rave_id));
        });
        addAllToCalendarButton.style.display = "block";
    });

    // const searchButton = document.querySelector('form button[type="submit"]');
    // searchButton.addEventListener("click", function() {
    //     addAllToCalendarButton.style.display = "block";
    // });

    addAllToCalendarButton.addEventListener("click", function() {
        addAllRavesToCalendar();
        addAllToCalendarButton.textContent = "Done";
        addAllToCalendarButton.disabled = true; // Disable the button after it's clicked
    });

    function addAllRavesToCalendar() {
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/add_all_to_calendar", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                console.log("All raves added to calendar");
                // Optionally, update the button text or perform other actions
                // to indicate that all raves have been added to the calendar
            }
        };
        xhr.send(); // No need to send any data
    }

});