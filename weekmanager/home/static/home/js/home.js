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
            const id = this.getAttribute('act-id');
            const activity = this.parentElement.parentElement;
            const daySection = activity.parentElement;

            activity.style.animation = 'swoosh .5s ease';
            activity.addEventListener('animationend', function (){
                this.remove();

                if (daySection.children.length == 1) {
                    const p = document.createElement('p');
                    p.innerHTML = "No activities for this day yet.";
                    daySection.appendChild(p);
                }

                $.ajax({
                    url: '/home/delete/' + id
                })
            })
        })
    })

    closeFormBtn.addEventListener('click', function(){
        closeForm();
    })
})