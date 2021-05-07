import { writable } from 'svelte/store';

const items = writable(JSON.parse(localStorage.getItem("items")) || []);
const itemtags = writable(JSON.parse(localStorage.getItem("itemtags")) || []);

const spells = writable(JSON.parse(localStorage.getItem("spells")) || []);
const characters = writable(JSON.parse(localStorage.getItem("characters")) || {});

items.subscribe(list => {
  localStorage.setItem("items", JSON.stringify(list));
})

itemtags.subscribe(list => {
  localStorage.setItem("itemtags", JSON.stringify(list));
})

spells.subscribe(list => {
  localStorage.setItem("spells", JSON.stringify(list));
})

characters.subscribe(object => {
  localStorage.setItem("characters", JSON.stringify(object));
})

export { items, itemtags, spells, characters }; 