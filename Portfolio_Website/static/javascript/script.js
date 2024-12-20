const filterList = document.querySelector('.control')
const filterButtons = filterList.querySelectorAll('.button');
const skills = document.querySelectorAll('.skill');

console.log("hello")

//defaultFilter =
filterSkills('Frontend')

filterButtons.forEach((button) => {
    button.addEventListener('click', (e) => {
        const filter = e.target.getAttribute('data-filter');
        console.log(filter);
        //change the active button
        updateActiveButton(e.target);
        //filter the list
        filterSkills(filter);
    } )
})

function updateActiveButton(newButton){
    //find the previously active button
    //& remove the active class from it
    filterList.querySelector('.active').classList.remove('active')
    //add the active class to our new button
    newButton.classList.add('active');

}

function filterSkills(skillFilter){
    //get each conference category
    skills.forEach((skill) => {
        const skillCategory = skill.getAttribute('data-category')



        //check if that category matches the filter
        if (skillFilter == 'All'||skillFilter == skillCategory){
            skill.removeAttribute('hidden')
        } else {
            skill.setAttribute('hidden','')
        }
        //if it matches, show that conf
        //if not, hide that conf
    })
}
