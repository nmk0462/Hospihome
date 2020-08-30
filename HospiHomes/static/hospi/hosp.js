
function save_edit(id){
    
    fetch(`/edit/${id}`)
.then(response => response.json())
.then(post => {
    // Print email
    cardbody = document.querySelector(`#card-body-${id}`);
    cardbody.innerHTML = `<form id="editform-${post.id}"><div class="form-group"><label for="textarea"><h3>Specialities:</h3></label>
    <textarea class="form-control" id="textarea-${post.id}" rows="2">${post.specs}</textarea><br><label for="textarea1"><h3>Contacts:</h3></label><textarea class="form-control" id="textarea1-${post.id}" rows="1">${post.conts}</textarea><br><label for="textarea2"><h3>Doctors:</h3></label><textarea class="form-control" id="textarea2-${post.id}" rows="2">${post.docts}</textarea><br><button class="btn btn-primary" type="submit">Save</button></form>`;
    // ... do something else with email ...
    const form = document.querySelector(`#editform-${post.id}`);
    form.onsubmit = () => {
        const textare = document.querySelector(`#textarea-${post.id}`).value;
        const textare1 = document.querySelector(`#textarea1-${post.id}`).value;
        const textare2 = document.querySelector(`#textarea2-${post.id}`).value;
        console.log(textare,textare1,textare2)
        fetch(`/edit/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                specs: textare,
                conts:textare1,
                docts:textare2
                
                
            })
          })
        showcontent(`${id}`);
        return false;
    }
});
}

function showcontent(id){
   
    cardbody = document.querySelector(`#card-body-${id}`);
    fetch(`/edit/${id}`)
.then(response => response.json())
.then(post => {
    // Print email
     cardbody.innerHTML = `<p></p>`;
    // ... do something else with email ...
});
}