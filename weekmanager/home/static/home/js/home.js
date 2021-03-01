$(document).ready(function(){
    const activities = document.querySelectorAll('.activity');
    const shadowPanel = document.querySelector('#shadow-panel');
    const formPanel = document.querySelector('#form-panel');
    const closeFormBtn = document.querySelector('.close-form-btn');
    const deleteButtons = document.querySelectorAll('.delete-btn'); 
    const addBtn = document.querySelector('#add-btn');

    function openForm() {
        shadowPanel.classList.add('active');
        formPanel.classList.add('active');
    }

    function closeForm() {
        shadowPanel.classList.remove('active');
        formPanel.classList.remove('active');
    }

    addBtn.addEventListener('click', function(){
        openForm();
    })

    activities.forEach( function(activity) {
        activity.addEventListener('click', function(e){
            if(e.target === this)   // prevent from opening form on click the delete btn
                openForm();
        })
    })

    deleteButtons.forEach( function(btn) {
        btn.addEventListener('click', function(){
            const activity = this.parentElement.parentElement;

            activity.style.animation = 'swoosh .5s ease';
            activity.addEventListener('animationend', function (){
                this.remove();
            })
        })
    })

    closeFormBtn.addEventListener('click', function(){
        closeForm();
    })
})