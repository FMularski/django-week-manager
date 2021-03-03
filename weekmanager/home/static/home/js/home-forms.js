$(document).ready(function (){
    const addBtn = document.querySelector('#add-btn');
    const activityForm = document.querySelector('#activity-form');

    addBtn.addEventListener('click', function(){
        activityForm.action = '/home/add/';
    })
})