const tagInputs = document.querySelectorAll('.symp-tag');
const ul = document.querySelectorAll("ul");
const ul1 = document.querySelector("ul.allerg");
const ul2 = document.querySelector("ul.disab");
let tags = [];
let allergy = [];
let disability = [];

console.log(ul, ul1, ul2);

createTag();
function createTag(){
    ul[0].querySelectorAll("li").forEach(li => li.remove());
    tags.slice().reverse().forEach(tag =>{
        let liTag = `<li>${tag} <i class="remove-icon" onclick="remove(this, '${tag}')">&times;</i></li>`;
        ul.insertAdjacentHTML("afterbegin", liTag);
    });
}

function remove(element, tag){
    let index  = tags.indexOf(tag);
    tags = [...tags.slice(0, index), ...tags.slice(index + 1)];
    element.parentElement.remove();
}

function addTag(e){
    const value = e.target.value;
    if(e.key === ";" || value.indexOf(';') !== -1){
        e.preventDefault();
        let tag = e.target.value.replace(/\s+/g, ' ').replace(/;/g, '');
        if(tag.length > 1 && !tags.includes(tag)){
            if(tags.length < 20){
                tag.split(',').forEach(tag => {
                    tags.push(tag);
                    createTag();
                });
            }
        }
        e.target.value = "";
    }
}

tagInputs[0].addEventListener("keyup", addTag);

createAllergy();
function createAllergy(){
    ul1.querySelectorAll("li").forEach(li => li.remove());
    allergy.slice().reverse().forEach(tag =>{
        let liTag = `<li>${tag} <i class="remove-icon" onclick="removeAllergy(this, '${tag}')">&times;</i></li>`;
        ul1.insertAdjacentHTML("afterbegin", liTag);
    });
}

function removeAllergy(element, tag){
    let index  = allergy.indexOf(tag);
    allergy = [...allergy.slice(0, index), ...allergy.slice(index + 1)];
    element.parentElement.remove();
}

function addTag(e){
    const value = e.target.value;
    if(e.key === ";" || value.indexOf(';') !== -1){
        e.preventDefault();
        let tag = e.target.value.replace(/\s+/g, ' ').replace(/;/g, '');
        if(tag.length > 1 && !allergy.includes(tag)){
            if(allergy.length < 20){
                tag.split(',').forEach(tag => {
                    allergy.push(tag);
                    createAllergy();
                });
            }
        }
        e.target.value = "";
    }
}

tagInputs[1].addEventListener("keyup", addTag);


createDis();
function createDis(){
    ul2.querySelectorAll("li").forEach(li => li.remove());
    disability.slice().reverse().forEach(tag =>{
        let liTag = `<li>${tag} <i class="remove-icon" onclick="removeDis(this, '${tag}')">&times;</i></li>`;
        ul2.insertAdjacentHTML("afterbegin", liTag);
    });
}

function removeDis(element, tag){
    let index  = disability.indexOf(tag);
    disability = [...disability.slice(0, index), ...disability.slice(index + 1)];
    element.parentElement.remove();
}

function addTag(e){
    const value = e.target.value;
    if(e.key === ";" || value.indexOf(';') !== -1){
        e.preventDefault();
        let tag = e.target.value.replace(/\s+/g, ' ').replace(/;/g, '');
        if(tag.length > 1 && !disability.includes(tag)){
            if(disability.length < 20){
                tag.split(',').forEach(tag => {
                    disability.push(tag);
                    createDis();
                });
            }
        }
        e.target.value = "";
    }
}

tagInputs[2].addEventListener("keyup", addTag);
