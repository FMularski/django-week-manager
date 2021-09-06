$(document).ready(function(){
    const activities = document.querySelectorAll('.activity');
    const shadowPanel = document.querySelector('#shadow-panel');
    const formPanel = document.querySelector('#form-panel');
    const closeFormBtn = document.querySelector('.close-form-btn');
    const deleteButtons = document.querySelectorAll('.delete-btn'); 
    const addBtn = document.querySelector('#add-btn');
    const titleField = document.querySelector('#title');
    const categoryField = document.querySelector('#category');
    const dateField = document.querySelector('#date');
    const fromField = document.querySelector('#time-start');
    const toField = document.querySelector('#time-end');
    const activityForm = document.querySelector('#activity-form');

    /*******************  HELPER FUNCTIONS **************************/

    function openForm() {
        shadowPanel.classList.add('active');
        formPanel.classList.add('active');
    }

    function closeForm() {
        shadowPanel.classList.remove('active');
        formPanel.classList.remove('active');

        titleField.value = '';
        fromField.value = '';
        toField.value = '';
    }

    function formatTime(timeStr) {
        const pm = timeStr.includes('p.m.');

        timeStr = timeStr.replace(' a.m.', '').replace(' p.m.', '');
        let time = timeStr.split(':');

        if(pm && time[0] != '12') time[0] = (parseInt(time[0]) + 12).toString();

        if (time[0].length == 1) time[0] = '0' + time[0];
        if (time[1].length == 0) time[1] = '00';

        return time[0] + ':' + time[1];
    }

    /**************************************************************************/

    // set form action to create when clicking add button
    addBtn.addEventListener('click', function(){
        openForm();
        activityForm.action = '/create/';
    })

    // - clicking on an activity opens activity form
    // - compare click target with activity -> prevents from opening form on click the delete btn
    // - get id from html tag attribute to build an URL 
    // - get html tag attributes representing activity fields to fill inputs after opening activity form
    activities.forEach( function(activity) {
        activity.addEventListener('click', function(e){
            if(e.target === this) {
                openForm();
                const id = activity.getAttribute('act-id');
                activityForm.action = '/update/' + id + '/';

                titleField.value = this.getAttribute('title');
                categoryField.value = this.getAttribute('category-id');
                dateField.value = this.getAttribute('day-id');
                
                fromField.value = formatTime(this.getAttribute('from'));
                toField.value = formatTime(this.getAttribute('to'));
            }   
        })
    })

    // - get id from html tag attribute to build and URL
    // - give the activity the animation
    // - after animation insert <p> tag if no activities left
    // - call ajax with the built url to remove the activity from the db
    deleteButtons.forEach( function(btn) {
        btn.addEventListener('click', function(){
            const activity = this.parentElement.parentElement;
            const id = activity.getAttribute('act-id');
            const daySection = activity.parentElement;

            activity.style.animation = 'swoosh .5s ease';
            activity.addEventListener('animationend', function (){
                this.remove();

                if (daySection.children.length == 1) {  // if only h2 with day name in the day section (so no activities)
                    const p = document.createElement('p');
                    p.innerHTML = "No activities for this day yet.";
                    daySection.appendChild(p);
                }

                $.ajax({
                    url: '/delete/' + id
                })
            })
        })
    })

    // simply close the form after clicking the X
    closeFormBtn.addEventListener('click', function(){
        closeForm();
    })
})