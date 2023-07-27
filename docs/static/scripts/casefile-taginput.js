const tagInputs = document.querySelectorAll('.symp-tag');
const ul = document.querySelectorAll('ul');
export let tags = [];
export let allergy = [];
export let disability = [];

createTag();
function createTag () {
  ul[0].querySelectorAll('li').forEach(li => li.remove());
  tags.slice().reverse().forEach(tag => {
    const liTag = `<li>${tag} <i class="remove-icon" onclick="remove(this, '${tag}')">&times;</i></li>`;
    ul[0].insertAdjacentHTML('afterbegin', liTag);
  });
}

function remove (element, tag) {
  const index = tags.indexOf(tag);
  tags = [...tags.slice(0, index), ...tags.slice(index + 1)];
  element.parentElement.remove();
}

function addTag (e) {
  const value = e.target.value;
  if (e.key === ';' || value.indexOf(';') !== -1) {
    e.preventDefault();
    const tag = e.target.value.replace(/\s+/g, ' ').replace(/;/g, '');
    if (tag.length > 1 && !tags.includes(tag)) {
      if (tags.length < 20) {
        tag.split(',').forEach(tag => {
          tags.push(tag);
          createTag();
        });
      }
    }
    e.target.value = '';
  }
}

tagInputs[0].addEventListener('keyup', addTag);

createAllergy();
function createAllergy () {
  ul[1].querySelectorAll('li').forEach(li => li.remove());
  allergy.slice().reverse().forEach(tag => {
    const liTag = `<li>${tag} <i class="remove-icon" onclick="removeAllergy(this, '${tag}')">&times;</i></li>`;
    ul[1].insertAdjacentHTML('afterbegin', liTag);
  });
}

function removeAllergy (element, tag) {
  const index = allergy.indexOf(tag);
  allergy = [...allergy.slice(0, index), ...allergy.slice(index + 1)];
  element.parentElement.remove();
}

function allergyAddTag (e) {
  const value = e.target.value;
  if (e.key === ';' || value.indexOf(';') !== -1) {
    e.preventDefault();
    const tag = e.target.value.replace(/\s+/g, ' ').replace(/;/g, '');
    if (tag.length > 1 && !allergy.includes(tag)) {
      if (allergy.length < 20) {
        tag.split(',').forEach(tag => {
          allergy.push(tag);
          createAllergy();
        });
      }
    }
    e.target.value = '';
  }
}

tagInputs[1].addEventListener('keyup', allergyAddTag);

createDis();
function createDis () {
  ul[2].querySelectorAll('li').forEach(li => li.remove());
  disability.slice().reverse().forEach(tag => {
    const liTag = `<li>${tag} <i class="remove-icon" onclick="removeDis(this, '${tag}')">&times;</i></li>`;
    ul[2].insertAdjacentHTML('afterbegin', liTag);
  });
}

function removeDis (element, tag) {
  const index = disability.indexOf(tag);
  disability = [...disability.slice(0, index), ...disability.slice(index + 1)];
  element.parentElement.remove();
}

function disAddTag (e) {
  const value = e.target.value;
  if (e.key === ';' || value.indexOf(';') !== -1) {
    e.preventDefault();
    const tag = e.target.value.replace(/\s+/g, ' ').replace(/;/g, '');
    if (tag.length > 1 && !disability.includes(tag)) {
      if (disability.length < 20) {
        tag.split(',').forEach(tag => {
          disability.push(tag);
          createDis();
        });
      }
    }
    e.target.value = '';
  }
}

tagInputs[2].addEventListener('keyup', disAddTag);
