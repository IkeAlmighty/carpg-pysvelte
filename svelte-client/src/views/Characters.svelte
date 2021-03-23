<script>
  import axios from "axios";
  import ItemCard from "../components/ItemCard.svelte";
  import names from '../names';

  let name = undefined;
  let characterClass = undefined;
  let inventory = undefined;

  const createCharacter = (e)=>{  
    e.preventDefault();
    let lastName = names[Math.floor(Math.random()*Math.floor(names.length - 1))]
    name = `${names[Math.floor(Math.random()*Math.floor(names.length - 1))]} ${lastName}`;
    
    inventory = undefined;
    if (characterClass === 'Artifactor' || characterClass === 'NPC') {
      axios.get(`_ENV_API_URI/items?limit=2&spellchance=100`).then(res=>{
        inventory = [];
        res.data.forEach(item=>inventory.push(item));
      });
    }
  }
</script>

<div class="container">
  <h1>Character Creator</h1>
  <form on:submit={createCharacter}>
    <input
      class="inputfield"
      bind:value={name}
      type="text"
      placeholder="Character Name (Currently Randomized)"
    />

    <select class="inputfield" bind:value={characterClass}>
      <!-- <option disable selected hidden value="">Select a Character Class</option> -->
      <option value="Ancient One">Ancient One</option>
      <option value="Military Grunt">Military Grunt</option>
      <option value="Artifactor">Artifactor</option>
      <option value="Medic/Healer">Medic / Healer</option>
      <option value="Diplomat/Linquist">Diplomat / Linquist</option>
      <option value="NPC" selected>Non-Player Character</option>
    </select>

    <input type="submit" value="Create Character" />
  </form>

  <h1>{characterClass}</h1>
  <div>{#if name}{name}{/if}</div>
  <div>
    {#if inventory}
    <u class="d-block my-1">Inventory</u>
      {#each inventory as item}
        <ItemCard item={item} />
      {/each}
    {/if}
  </div>
</div>

<style>
  .inputfield {
    display: block;
    width: 300px;
  }
</style>
