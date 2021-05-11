import { writable } from 'svelte/store';


function createClientStore(init, storeName) {
  let data = writable(JSON.parse(localStorage.getItem(storeName) || init))
  
  data.subscribe(listOrObj => {
    localStorage.setItem(storeName, JSON.stringify(listOrObj))
  })
  
  return data;
}

const items = createClientStore([], "items");
const itemtags = createClientStore([], "itemtags");
const spells = createClientStore([], "spells");
const spelltags = createClientStore([], "spelltags");
const characters = createClientStore({}, "characters");

export { items, itemtags, spells, spelltags, characters }; 