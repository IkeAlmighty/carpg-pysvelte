<script>
  import ItemCard from './ItemCard.svelte';
  import { characters } from '../stores';

  export let name;
  export let inventory;
  export let characterClass;
  export let inventoryLoadingMessage;

  function deleteFromStore() {
    // create a list of characters that are not this character:
    let names = Object.keys($characters).filter(key=>(name !== key));
    let otherCharacters = names.map(name=>$characters[name]);

    // reset $characters
    $characters = {}

    // add all characters from the created list under the correct name:
    otherCharacters.forEach(character=>$characters[character.name] = character);
  }
</script>

<div class="container">
 
  <div class="class-title"><h1>{characterClass}</h1></div>
  <div class="delete-button">
    <button 
    on:click={deleteFromStore}>delete</button>
  </div>
  <div class="name">
    {#if name}{name}{/if}
  </div>
  <div class="inventory">
    {#if inventory}
      <u class="d-block my-1">Inventory</u>
      {#each inventory as item}
        <ItemCard {item} />
      {/each}
    {/if}

    {#if inventoryLoadingMessage}
      <strong class="my-1">{inventoryLoadingMessage}</strong>
    {/if}
  </div>
</div>

<style>
    .container {
      display: grid;
      grid-template-areas: "class-title class-title delete-button" "name name name" "inventory inventory inventory";
    }

    .class-title {
      grid-area: class-title;
    }

    .delete-button {
      grid-area: delete-button;
      padding-top: 1.5em;
      text-align: right;
    }

    .name {
      grid-area: name;
      width: 100%;
    }

    .inventory {
      grid-area: inventory;
      width: 100%;
    }
</style>