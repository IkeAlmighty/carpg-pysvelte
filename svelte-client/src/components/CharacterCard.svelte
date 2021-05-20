<script>
  import ItemCard from "./ItemCard.svelte";
  import IncantationCard from "./IncantationCard.svelte";
  import { characters } from "../stores";

  export let name;
  export let inventory;
  export let incantations;
  export let characterClass;
  export let inventoryLoadingMessage;

  function deleteFromStore() {
    // create a list of characters that are not this character:
    let names = Object.keys($characters).filter((key) => name !== key);
    let otherCharacters = names.map((name) => $characters[name]);

    // reset $characters
    $characters = {};

    // add all characters from the created list under the correct name:
    otherCharacters.forEach(
      (character) => ($characters[character.name] = character)
    );
  }
</script>

<div class="container">
  <div class="name"><h1>{name}</h1></div>
  <div class="delete-button">
    <button on:click={deleteFromStore}>delete</button>
  </div>
  <div class="class-title">{characterClass}</div>
  <div class="inventory">
    {#if inventoryLoadingMessage}
      <strong class="my-1">{inventoryLoadingMessage}</strong>
    {/if}

    {#if inventory && inventory.length > 0}
      <u class="d-block my-1">Inventory</u>
      {#each inventory as item}
        <ItemCard {item} />
      {/each}
    {/if}

    {#if incantations && incantations.length > 0}
      <u class="d-block my-1">Incantations</u>
      {#each incantations as incantation}
        <IncantationCard {incantation} />
      {/each}
    {/if}
  </div>
</div>

<style>
  .container {
    display: grid;
    grid-template-areas:
      "name name delete-button"
      "class-title class-title class-title"
      "inventory inventory inventory"
      "incantations incantations incantations";
  }

  .class-title {
    grid-area: class-title;
    width: 100%;
  }

  .delete-button {
    grid-area: delete-button;
    padding-top: 1.5em;
    text-align: right;
  }

  .name {
    grid-area: name;
  }

  .inventory {
    grid-area: inventory;
    width: 100%;
  }
</style>
